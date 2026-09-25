// Offline support: after the first visit the whole game (code, 3D library, all voice clips) is stored on the device.
const CACHE = 'feza-unicorn-v6';
const CORE = ['./', './index.html', './vendor/three.js', './voice/manifest.js', './voice/manifest.json',
  './manifest.webmanifest', './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];
const FRESH = /(\/|index\.html|manifest\.js|manifest\.json|manifest\.webmanifest)$/;   // always try the network first for these

async function syncVoices() {   // make sure every recorded line is on the device
  try {
    const c = await caches.open(CACHE);
    const m = await (await fetch('./voice/manifest.json', { cache: 'no-cache' })).json();
    const files = [...new Set(Object.values(m))].map(f => './voice/' + f);
    for (const f of files) if (!(await c.match(f))) { try { await c.add(f); } catch (e) {} }
  } catch (e) {}
}
self.addEventListener('install', e => e.waitUntil((async () => {
  await (await caches.open(CACHE)).addAll(CORE); await syncVoices(); self.skipWaiting();
})()));
self.addEventListener('activate', e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
  await self.clients.claim();
})()));
self.addEventListener('message', e => { if (e.data === 'sync') e.waitUntil(syncVoices()); });
self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;
  const fresh = req.mode === 'navigate' || FRESH.test(url.pathname);
  e.respondWith((async () => {
    const c = await caches.open(CACHE);
    if (fresh) {
      try { const r = await fetch(req, { cache: 'no-cache' }); if (r.ok) c.put(req.mode === 'navigate' ? './index.html' : req, r.clone()); return r; }
      catch (err) { return (await c.match(req, { ignoreSearch: true })) || (await c.match('./index.html')) || Response.error(); }
    }
    const hit = await c.match(req, { ignoreSearch: true }); if (hit) return hit;
    const r = await fetch(req); if (r.ok) c.put(req, r.clone()); return r;
  })());
});
