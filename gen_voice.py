"""Records every narrator line in voice/lines.json with a natural Turkish female voice.

Requires:  python3 -m pip install edge-tts
Run:       python3 gen_voice.py
Only missing lines are generated; voice/manifest.json maps text -> mp3 file.
"""
import asyncio
import hashlib
import json
import os
import re
import shutil
import subprocess

import edge_tts

VOICE = "tr-TR-EmelNeural"
RATE = "-8%"      # a little slower = calmer
PITCH = "+2Hz"
# How words should *sound* (subtitle keeps the normal spelling). "unicorn" → English pronunciation.
PRONOUNCE = [(r"(?i)unicorn", "yunikorn")]


def spoken(text):
    for pat, rep in PRONOUNCE:
        text = re.sub(pat, rep, text)
    return text


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voice")


def fname(text):
    return hashlib.md5(f"{VOICE}|{RATE}|{PITCH}|{spoken(text)}".encode()).hexdigest()[:12] + ".mp3"


def trim_all(files):
    """Cut leading/trailing silence (needs ffmpeg) so reactions and counting feel instant."""
    if not shutil.which("ffmpeg"):
        return
    done_path = os.path.join(ROOT, "trimmed.txt")
    done = set(open(done_path).read().split()) if os.path.exists(done_path) else set()
    todo = [f for f in files if f not in done and os.path.exists(os.path.join(ROOT, f))]
    af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,"
          "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.12,areverse")
    for f in todo:
        src = os.path.join(ROOT, f)
        tmp = src + ".tmp.mp3"
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af", af, "-b:a", "64k", tmp])
        if r.returncode == 0 and os.path.getsize(tmp) > 1000:
            os.replace(tmp, src)
            done.add(f)
        elif os.path.exists(tmp):
            os.remove(tmp)
    open(done_path, "w").write("\n".join(sorted(done & set(files))))
    print(f"trimmed {len(todo)} files")


async def main():
    lines = json.load(open(os.path.join(ROOT, "lines.json"), encoding="utf-8"))
    sem = asyncio.Semaphore(6)
    manifest, todo = {}, []
    for t in lines:
        manifest[t] = fname(t)
        if not os.path.exists(os.path.join(ROOT, manifest[t])):
            todo.append(t)

    async def one(t):
        async with sem:
            for attempt in range(4):
                try:
                    await edge_tts.Communicate(spoken(t), VOICE, rate=RATE, pitch=PITCH).save(os.path.join(ROOT, manifest[t]))
                    return
                except Exception as e:  # network hiccup: retry
                    if attempt == 3:
                        print("FAILED:", t, e)
                    await asyncio.sleep(1 + attempt)

    print(f"{len(lines)} lines, {len(todo)} to record…")
    await asyncio.gather(*(one(t) for t in todo))
    trim_all(set(manifest.values()))
    manifest = {t: f for t, f in manifest.items() if os.path.exists(os.path.join(ROOT, f))}
    keep = set(manifest.values())
    for f in os.listdir(ROOT):  # drop recordings of lines that no longer exist
        if f.endswith(".mp3") and f not in keep:
            os.remove(os.path.join(ROOT, f))
    json.dump(manifest, open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    # same data as a classic script, so it also loads when index.html is double-clicked (file://)
    with open(os.path.join(ROOT, "manifest.js"), "w", encoding="utf-8") as f:
        f.write("window.VOICE_MANIFEST = " + json.dumps(manifest, ensure_ascii=False) + ";\n")
    print(f"done: {len(manifest)} lines in manifest")


asyncio.run(main())
