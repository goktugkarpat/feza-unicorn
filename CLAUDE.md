# Feza ve Işıltı – çalışma notları

- Oyun girişi `index.html`, oyun kodu `game.js` (three.js `vendor/three.js`'ten klasik script olarak yüklenir; file:// ile de çalışmalı).
- Anlatıcı cümleleri `game.js` içindeki `LN` bölümünde. Cümle eklenir/değişirse: `python3 serve.py` → tarayıcı konsolunda `__saveLines()` → `python3 gen_voice.py`.
- Test ederken oyunu her zaman `?sessiz` ile aç (kullanıcının Mac'inde ses çalmasın).
- GitHub'a SADECE kullanıcı "GitHub'a gönder" dediğinde gönder: `git add -A && git commit -m "..." && git push` (depo: github.com/goktugkarpat/feza-unicorn, GitHub Pages açık: https://goktugkarpat.github.io/feza-unicorn/). Aradaki değişiklikleri kendiliğinden push etme.
- iPad uygulaması: `manifest.webmanifest`, `sw.js` (internetsiz çalışma; önemli değişiklikte `CACHE` sürümünü artır), `icons/`. Simge `index.html?sessiz&ikon` sayfasının 1024x1024 ekran görüntüsünden üretilir.

- Grafikler fiziksel malzemeler, yerel çizimli dokular ve assets/surfaces.js içindeki CC0 yüzey taramalarını kullanır; sabit parçaları birleştirme ve ortak geometri sahipliği korunur. navigation.js tek dokunuş rotasını ve hareket boyunca hedef yakalamayı sağlar. Sürükleme/klavye otomatik rotayı iptal eder. Sessiz mod Audio/AudioContext oluşturmaz; anlatım yalnız kayıtlı Türkçe seslerle yapılır. iPad çözünürlüğünü koşu sırasında değiştirme. Runtime değişince sw.js içerik sürümü yenilenir; önbellek yalnız feza-unicorn- önekini temizler.

- v12: assets/surfaces.js gömülü veri URL’leri içerir; game.js bu görselleri yükledikten sonra sahneyi kurar. Dış URL’den çalışma anında kaplama isteme; file:// ve çevrimdışı desteğini koru. Kaynakları ASSET-LICENSES.md içinde tut.
- Mini harita boyutları #hud CSS değişkenlerinden yönetilir; altyazı ve dokunma alanlarıyla çakışmamalı. Arkadaş selamları tek seferlik, en az 90 saniye aralıklı ve dururken gelir. Şekil balonu geometrileri geo() önbelleğinde paylaşılır; toplarken ortak geometrileri dispose etme.
