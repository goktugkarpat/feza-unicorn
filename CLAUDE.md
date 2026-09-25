# Feza ve Işıltı – çalışma notları

- Oyun tek dosya: `index.html` (three.js `vendor/three.js`'ten klasik script olarak yüklenir; file:// ile de çalışmalı).
- Anlatıcı cümleleri `index.html` içindeki `LN` bölümünde. Cümle eklenir/değişirse: `python3 serve.py` → tarayıcı konsolunda `__saveLines()` → `python3 gen_voice.py`.
- Test ederken oyunu her zaman `?sessiz` ile aç (kullanıcının Mac'inde ses çalmasın).
- Her değişiklik tamamlanınca GitHub'a gönder: `git add -A && git commit -m "..." && git push` (depo: github.com/goktugkarpat/feza-unicorn, GitHub Pages açık).
