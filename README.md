# Feza ve Işıltı – Gökkuşağı Kaydırağı 🦄🌈

5 yaş için hazırlanmış, üç boyutlu, Türkçe seslendirmeli bir çocuk oyunu.
Feza, gökkuşağı unicornu Işıltı'ya biniyor, rengarenk şehirde görevleri tamamlıyor, gökkuşağına tırmanıp kaydıraktan kayar gibi aşağı kayıyor.

## Nasıl açılır

- **Bilgisayarda:** `index.html` dosyasına çift tıklamanız yeterli. Kurulum ya da internet gerekmez.
- **iPad'de / internette:** Depoyu GitHub Pages ile yayınlayın (Settings › Pages › Branch: `main`, klasör: `/ (root)`).
  iPad'de Safari ile https://goktugkarpat.github.io/feza-unicorn/ adresini açıp Paylaş › **Ana Ekrana Ekle** deyin:
  oyun kendi simgesiyle, tam ekran bir uygulama gibi açılır. İlk açılıştan sonra **internet olmadan da** çalışır (`sw.js` her şeyi cihaza kaydeder).

## Nasıl oynanır

- Başta hangi Feza ile oynayacağını seç: **Gökkuşağı Feza** (rengarenk kıyafet) ya da **Sade Feza** (fotoğraftaki tişört). Ekrana ilk dokunuşta müzik başlar.
- Parmağını ekrana koy ve gezdir: Feza parmağın gittiği yere koşar (bilgisayarda fareyle tıklayıp sürükle ya da ok tuşları).
- Sarı **Zıpla** düğmesi (klavyede Boşluk) zıplatır.
- Sol alttaki **mini haritada** aranan şeyler (renkli yıldızlar, elmalar, şekilli balonlar) görünür; sıradaki hedefin etrafında sarı bir halka yanıp söner. Harita sadece yol gösterir, oraya Feza kendisi gider.
- Kayarken parmağını sağa sola kaydırarak yıldızları topla.
- Şehirde Feza'nın arkadaşları var: **Deniz Ali, Efe, Gün, Asya, Gülru ve Zeynep Ada**. Biri el sallayınca başında 👋 çıkar; ona dokun: Feza el sallar, arkadaşı sevinir, bir yıldız kazanırsın.
- 🔊 düğmesi son görevi tekrar okur, 🎵 müziği açar/kapatır.
- Adresin sonuna `?sessiz` eklersen oyun tamamen sessiz açılır (test için).

## Öğretici bölümler

1. **Renkler:** gökkuşağının 7 rengini sırayla bulma.
2. **Sayma:** Işıltı için elma toplayıp sayma.
3. **Şekiller:** daire, kare, üçgen, yıldız ve kalp şeklindeki balonları bulma.
4. Her görevden sonra tırmanırken 1'den 10'a sayma, tepede bir bilgi, kayarken yıldız sayma.

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | Oyunun tamamı |
| `vendor/three.js` | 3D kütüphanesi (three.js r170, MIT lisansı) |
| `voice/*.mp3`, `voice/manifest.js` | Türkçe kadın sesiyle kaydedilmiş anlatıcı cümleleri |
| `gen_voice.py`, `voice/lines.json`, `voice/trimmed.txt` | Cümle değişirse sesleri yeniden üretmek için |
| `manifest.webmanifest`, `sw.js`, `icons/` | iPad'de uygulama gibi açılma, simge ve internetsiz çalışma |
| `serve.py` | İsteğe bağlı yerel sunucu (iPad'i aynı Wi-Fi'dan bağlamak için) |

## Cümleleri değiştirmek

Oyundaki tüm cümleler `index.html` içindeki `LN` bölümündedir. Bir cümleyi değiştirdikten sonra:

```bash
python3 -m pip install edge-tts
python3 serve.py          # açık bırakın, tarayıcıda http://localhost:8765 açın
# tarayıcı konsolunda:  __saveLines()
python3 gen_voice.py      # sadece yeni/değişen cümleleri seslendirir
```

`ffmpeg` kuruluysa (`brew install ffmpeg`) kayıtların başındaki/sonundaki sessizlik otomatik kırpılır.
Okunuşu düzeltilecek kelimeler `gen_voice.py` içindeki `PRONOUNCE` listesindedir (ör. unicorn → "yunikorn").

Sesler Microsoft Edge'in çevrimiçi "tr-TR-EmelNeural" sesiyle üretilir.
