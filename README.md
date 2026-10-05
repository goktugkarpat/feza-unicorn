# Feza ve Işıltı – Gökkuşağı Kaydırağı 🦄🌈

5 yaş için hazırlanmış, üç boyutlu, Türkçe seslendirmeli bir çocuk oyunu.
Feza, gökkuşağı unicornu Işıltı'ya biniyor, rengarenk şehirde görevleri tamamlıyor, gökkuşağına tırmanıp kaydıraktan kayar gibi aşağı kayıyor.

## Nasıl açılır

- **Bilgisayarda:** `index.html` dosyasına çift tıklamanız yeterli. Kurulum ya da internet gerekmez.
- **iPad'de / internette:** Depoyu GitHub Pages ile yayınlayın (Settings › Pages › Branch: `main`, klasör: `/ (root)`).
  iPad'de Safari ile https://goktugkarpat.github.io/feza-unicorn/ adresini açıp Paylaş › **Ana Ekrana Ekle** deyin:
  oyun kendi simgesiyle, tam ekran bir uygulama gibi açılır. İlk açılıştan sonra **internet olmadan da** çalışır (`sw.js` her şeyi cihaza kaydeder).

## Nasıl oynanır

- Başta hangi Feza ile oynayacağını seç: **Gökkuşağı Feza** (rengarenk kıyafet) ya da **Feza** (fotoğraftaki tişört). Ekrana ilk dokunuşta müzik başlar.
- Parmağını ekrana koy ve gezdir: Feza parmağın gittiği yere koşar (bilgisayarda fareyle tıklayıp sürükle ya da ok tuşları).
- Sarı **Zıpla** düğmesi (klavyede Boşluk) zıplatır.
- Sol alttaki **mini haritada** aranan şeyler (renkli yıldızlar, elmalar, şekilli balonlar) görünür; sıradaki hedefin etrafında sarı bir halka yanıp söner. Haritadaki hedefe dokununca Feza binaların ve çeşmenin etrafından dolaşarak oraya gider. Sağdaki büyük hedef resmi de sıradaki göreve götürür.
- Kayarken parmağını sağa sola kaydırarak yıldızları topla.
- Şehirde Feza'nın arkadaşları var: **Deniz Ali, Efe, Gün, Asya, Gülru ve Zeynep Ada**. Biri el sallayınca başında 👋 çıkar; ona dokun: Feza el sallar, arkadaşı sevinir, bir yıldız kazanırsın.
- 🔊 düğmesi son görevi tekrar okur, 🎵 müziği açar/kapatır.
- Adresin sonuna `?sessiz` eklersen oyun tamamen sessiz açılır (test için).

## Öğretici bölümler

1. **Renkler:** gökkuşağının 7 rengini sırayla bulma.
2. **Sayma:** Işıltı için elma toplayıp sayma.
3. **Şekiller:** daire, kare, üçgen, yıldız ve kalp şeklindeki balonları bulma.
4. Her görevden sonra şehrin üstünden geçen dev gökkuşağına tırmanırken 1'den 20'ye sayma, tepede bir bilgi,
   sonra halkaların içinden geçerek uzun bir kayış ve yıldız sayma.

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `index.html` | Oyunun giriş ekranı ve görünümü |
| `navigation.js` | Tek dokunuş için güvenli rota ve hızlı geçişte hedef yakalama |
| `game.js` | JavaScript oyun motoru, animasyonlar ve anlatıcı cümleleri |
| `vendor/three.js` | 3D kütüphanesi (three.js r170, MIT lisansı) |
| `voice/*.mp3`, `voice/manifest.js` | Türkçe kadın sesiyle kaydedilmiş anlatıcı cümleleri |
| `gen_voice.py`, `voice/lines.json`, `voice/trimmed.txt` | Cümle değişirse sesleri yeniden üretmek için |
| `manifest.webmanifest`, `sw.js`, `icons/` | iPad'de uygulama gibi açılma, simge ve internetsiz çalışma |
| `serve.py` | İsteğe bağlı yerel sunucu (iPad'i aynı Wi-Fi'dan bağlamak için) |

## Cümleleri değiştirmek

Oyundaki tüm cümleler `game.js` içindeki `LN` bölümündedir. Bir cümleyi değiştirdikten sonra:

```bash
python3 -m pip install edge-tts
python3 serve.py          # açık bırakın, tarayıcıda http://localhost:8765 açın
# tarayıcı konsolunda:  __saveLines()
python3 gen_voice.py      # sadece yeni/değişen cümleleri seslendirir
```

`ffmpeg` kuruluysa (`brew install ffmpeg`) kayıtların başındaki/sonundaki sessizlik otomatik kırpılır.
Okunuşu düzeltilecek kelimeler `gen_voice.py` içindeki `PRONOUNCE` listesindedir (ör. unicorn → "yunikorn").

Sesler Microsoft Edge'in çevrimiçi "tr-TR-EmelNeural" sesiyle üretilir.

## Grafik ve kontrol yenilikleri

Yumuşak fiziksel ışık ve ortak gökyüzü yansıması kullanılır. Taş, ahşap, kiremit ve çim yüzeylerinde Poly Haven’dan alınmış CC0 kaplamalar pastel renklere uyarlanır; ayrıntılı ağaçlar ve çiçekler ortak geometriyle çizilir. Işıltı'nın yürüyüşü hızıyla uyumludur. Ekrandaki hedefe, haritaya veya hedef düğmesine dokunarak otomatik koşulur; sürükleme ve klavye her zaman kontrolü geri alır. Hareket boyunca hedef yakalama hızlı koşuda hedef atlamayı önler. iPad çözünürlüğü oyun sırasında değişmez. `?sessiz` ses öğesi veya AudioContext oluşturmaz.


## Şehir cilası (v12)

- Evlerde iki çatı biçimi, yuvarlak çatı pencereleri, kemerli girişler, küçük sütunlar, köşe taşları ve baca kapakları; kulelerde kat silmeleri, kaburgalar ve taç ayrıntıları bulunur.
- Feza’nın kıyafet kenarları ve ayakkabıları ayrıntılandırıldı. Işıltı’nın kulakları ve yelesi hareket eder; yürüyüş, zıplama ve kayma pozları yumuşak geçişlerle birleşir. Ağaçların dalları ve kökleri görünür.
- Mini harita bilgisayarda 205×260, tablette 225×285 piksel oldu. Dar telefon ve yatay ekranlarda kontrollerle çakışmayacak şekilde uyarlanır.
- Çocuklar Feza yanlarından geçerken sürekli el sallamaz. Selam daveti yalnız Feza kısa süre durunca, anlatıcı ve yakın görev hedefi uygunken çıkar; her arkadaş bir kez davet eder, davetler arasında en az 90 saniye vardır. El sallama kısa sürer, davet hareket başlayınca kapanır. İstenirse arkadaşlara dokunarak hâlâ selam verilebilir.
- Görev nesneleri şehri kaplayan uzun ışık sütunları yerine renkli halolarla ve sıradaki hedefte küçük bir işaretle gösterilir. Çeşmenin yüzeyinde yumuşak halkalar, kenarlarında heykelsi ayrıntılar vardır.
- Yeni yüzeyler toplam yaklaşık 475 KB’lık tek yerel pakette bulunur (`assets/surfaces.js`). İnternet isteği olmadan ve `file://` ile açılır; çevrimdışı önbelleğe dahil edilir. Kaynaklar: [ASSET-LICENSES.md](ASSET-LICENSES.md).
- Gökkuşağı başlangıcına otomatik rotayı engelleyen geniş dairesel çarpışma alanı gerçek ayak biçimine daraltıldı. Şekilli balonlar yeni görevlerde aynı geometriyi tekrar kullanır.
