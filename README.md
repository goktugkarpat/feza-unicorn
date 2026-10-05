# Feza ve Işıltı – Gökkuşağı Kaydırağı 🦄🌈

5 yaşındaki Feza için yapılmış, üç boyutlu, Türkçe seslendirmeli bir oyun.
Feza, gökkuşağı unicornu **Işıltı**'ya biniyor; rengârenk bir şehirde yıldız, elma ve şekilli balon topluyor,
sonra şehrin üstüne uzanan kocaman gökkuşağına tırmanıp tepeden aşağı kaydıraktan kayar gibi süzülüyor.
Şehirde çeşme, oyun parkı, uçuşan balonlar, uçan sıcak hava balonları ve Feza'nın gerçek arkadaşları var.
Her şey sakin ve neşelidir: yarış, süre, kaybetmek, korkutucu bir şey yoktur; yanlış bir şeye dokunulursa
anlatıcı nazikçe doğrusunu hatırlatır. Oyun sonsuz döner: bir gökkuşağı kayışından sonra sıradaki görev başlar.

## Nasıl açılır

- **Bilgisayarda:** `index.html` dosyasına çift tıklamanız yeterli. Kurulum ya da internet gerekmez.
- **İnternette:** https://goktugkarpat.github.io/feza-unicorn/ adresinden açılır.
- **iPad'de:** Safari ile yukarıdaki adresi açıp Paylaş › **Ana Ekrana Ekle** deyin.
  Oyun kendi simgesiyle, tam ekran bir uygulama gibi açılır. İlk açılıştan sonra **internet olmadan da** çalışır
  (`sw.js` oyunu ve bütün seslendirmeleri cihaza kaydeder).
- Aynı Wi-Fi'daki iPad'de denemek için Mac'te `python3 serve.py` çalıştırıp yazdığı adresi iPad'de açabilirsiniz.
- **Sessiz açmak** için adresin sonuna `?sessiz` ekleyin (ör. `index.html?sessiz`). Ne müzik ne anlatıcı çalar;
  altyazılar yine görünür.

## Nasıl oynanır

- **Başlangıç:** İki Feza kartı görürsün: **Gökkuşağı Feza** (rengârenk kıyafet) ve **Feza** (fotoğraftaki bulutlu, uçaklı, yıldızlı tişört).
  Birine dokun (ya da klavyede ← → ile seç, Boşluk veya Enter'a bas). İlk dokunuşta müzik başlar.
- **Giriş:** Kamera şehrin üstünden Feza'ya iner. Anlatıcı Feza'yı karşılar ve Işıltı'yı gösterir.
  Feza önce yürüyerek Işıltı'nın yanına gider; yaklaşınca Işıltı'ya biner. Sonrası Işıltı ile sürüş ve görevlerdir.
- **Görev akışı:** Sırayla üç görev gelir: renkler, sayma, şekiller (ayrıntıları aşağıda). Görev bitince gökkuşağı
  parlar, başlangıçtaki yıldızlı daireye gidip tırmanılır, tepede kayılır, inişte çocuklar alkışlar,
  sonra bir sonraki görev başlar. Oyun hiç bitmeden bu sırayla döner.
- **Görev kutusu:** Sol üstte görevin adı ve ilerleme simgeleri durur (7 yıldız, elmalar ya da şekiller); bulununca simge renklenir.
- **Altyazı:** Anlatıcının söylediği cümle altta yazı olarak da görünür.
- **Yıldız sayacı:** Sağ üstteki ⭐ sayacı kayarken topladığın yıldızları ve arkadaşlara verdiğin selamları sayar.
- **Düğmeler:** 🔊 anlatıcının son söylediğini ya da yapılacak işi tekrar eder; 🎵 müziği açar ve kapatır;
  sarı **Zıpla** düğmesi Işıltı'yı (ya da yürürken Feza'yı) zıplatır.
  Hedefi olan görevlerde sağda **🦄 ➜** düğmesi çıkar; hedef resmine dokununca Işıltı hedefe kendiliğinden gider.
- **İpuçları:** Bir süre bir şey yapılmazsa anlatıcı sarı Zıpla düğmesini hatırlatır; daha da beklenirse haritaya bakmayı ve sıradaki işi söyler.
- Oyun kayıt tutmaz; her açılışta baştan başlar.

## Kontroller

- **Parmakla (iPad, telefon):** Parmağını ekranda **koy ve sürükle**; Feza ya da Işıltı parmağının altındaki yere koşar,
  parmağını kaydırdıkça peşinden gelir. Parmağı kaldırınca durur.
- **Tek dokunuşla gezinme:** Ekranda görünen bir hedefe (yıldız, elma, balon) dokununca Işıltı binaların, ağaçların ve çeşmenin
  çevresinden dolaşarak oraya kendisi gider. **Mini haritadaki** hedefe ya da herhangi bir yere dokununca da aynı şekilde gider.
  Gidiş sırasında ekrana yeniden dokunup sürüklersen ya da yön tuşuna basarsan kontrolü sen geri alırsın.
  Hızlı koşarken bile hedef kaçmaz: yolu hedefin yakınından geçen koşu hedefi toplar.
- **Zıplama:** Sarı Zıpla düğmesi. Işıltı Feza'dan daha yükseğe zıplar.
- **Kayarken:** Parmağını ekranda sağa sola kaydır; Işıltı parmağının olduğu yöndeki şeride geçer.
- **Bilgisayarda:** Fareyle tıklayıp sürükleyerek de aynı şekilde oynanır. Yedek olarak **ok tuşları** (ya da **W A S D**) yürütür,
  **Boşluk** ya da Enter zıplatır; tepede Boşluk kaymayı başlatır, kayarken ← → şerit değiştirir.
- Ekran dokunmalarıyla sayfa kaymaz, yakınlaşmaz; oyun alanı sabit kalır.

## Feza'nın dünyası: Gökkuşağı Şehri

- **Işıltı:** Tüyleri, yelesi ve kuyruğu gökkuşağı renklerinde bir unicorn. Yürürken, koşarken, zıplarken ve kayarken farklı hareket eder;
  kulakları ve yelesi kıpırdar. Koşarken ardında rengârenk pırıltılar saçar ve nal sesi duyulur.
- **Şehir:** Ortada pastel desenli yuvarlak bir **meydan** ve ortasında yıldızlı bir **çeşme** (su fışkırır, havuzun yüzeyi dalgalanır) vardır.
  Meydandan geçen uzun bir **cadde** ve yan sokaklar boyunca renkli **kuleler**, çatılı **evler**, **ağaçlar**, **çiçek bahçeleri** ve **lambalar** sıralanır.
  Cadde üstünde **balonlardan yapılmış gökkuşağı kemerleri** ve havada uçuşan serbest balonlar bulunur.
  Gökyüzünde bulutlar süzülür, uzakta üç tane renkli **sıcak hava balonu** dönüp durur. Şehrin çevresinde çalı sınırı ve uzak tepeler vardır.
- **Oyun parkı:** Şehirde dağınık ve gökkuşağının indiği parkta **salıncaklar, tahterevalliler, atlıkarınca** ve top oynayan çocuklar vardır.
  Salıncakta sallanan, tahterevalliye binen, atlıkarıncada dönen çocuklar görülür; bazı çocuklar zıplar, balon tutar, koşar.
- **Büyük gökkuşağı:** Şehrin en güney ucundan en kuzey ucuna kadar uzanan dev bir kemerdir; yedi renk şeridi vardır.
  Görevler ilerledikçe renkler parlar. Hazır olmayan gökkuşağı silik, yarı saydam bir hayalet gibi görünür.
  Kameraya çok yaklaşınca gökkuşağı gerçeği gibi saydamlaşır.
- **Kameranın önündeki binalar:** Bir bina Feza ile kamera arasına girerse Feza binanın arkasında parlak bir gölge olarak görünür;
  kameranın içinde kaldığı bina çizilmez.
- **Yüzeyler:** Taş, ahşap, kiremit ve çim yüzeylerinde pastel renklere uyarlanmış gerçek doku fotoğrafları kullanılır (kaynaklar aşağıda).

## Arkadaşlar

Feza'nın gerçek arkadaşları şehirde durur ve adlarıyla anılır: **Deniz Ali, Efe, Gün, Asya, Gülru ve Zeynep Ada**.
Hepsinin kendi saçı, kıyafeti ve ayakkabısı vardır. Asya ve Gülru balon tutar, Efe ve Deniz Ali zıplar, Zeynep Ada balon tutar, Gün durur.

- Feza bir arkadaşının yanında kısa süre durup bekleyince, o arkadaş el sallar ve başında **👋** simgesi çıkar.
  Anlatıcı onun adını söyleyip dokunmanı ister.
- Arkadaşa dokunursan Feza el sallar, arkadaşı sevinip zıplar, kalpler uçuşur, anlatıcı ona cevap verir ve bir ⭐ kazanırsın.
- Selam daveti sakindir: her arkadaş **yalnız bir kez** çağırır, davetler arasında en az 90 saniye geçer.
  Görev hedefi yakındayken, Feza hareket ederken ya da anlatıcı konuşurken davet gelmez; hareket başlayınca kapanır.
- İstersen herhangi bir zaman bir çocuğa dokunup selam verebilirsin; adı olmayan çocuklar da gülümseyip zıplar.
  Şehirde bunlardan başka adı olmayan çocuklar da vardır.

## Görevler ve öğretici bölümler

Görevler sırayla **renkler → sayma → şekiller** diye döner. Her görevde anlatıcı önce kısa bir hikâye anlatır.
Hedefler şehirdeki sokak ve meydan noktalarında rastgele yerleşir ve her seferinde farklıdır.
Görev hedefleri renkli bir halo ile parlar; sıradaki hedefte ayrıca küçük bir ışık işareti vardır.

### 1. Renkler 🌈
- Hikâye: "Gökkuşağının renkleri kaybolmuş." Şehre yedi renkli yıldız dağılır.
- Yıldızlar **kırmızı, turuncu, sarı, yeşil, mavi, lacivert, mor** sırasıyla bulunur. Anlatıcı sıradaki rengi söyler.
- Doğru yıldızı toplayınca renk adı bir benzetmeyle söylenir (ör. kırmızı "çilek", turuncu "portakal", sarı "güneş",
  yeşil "çimenler", mavi "gökyüzü", lacivert "gece", mor "üzüm" gibi) ve gökkuşağının o şeridi parlar.
- Yanlış renge dokunursan yıldız kaybolmaz; anlatıcı o yıldızın rengini ve şimdi aranan rengi söyler.
- Yedi renk bitince anlatıcı renkleri sırayla sayar ve Feza'yı gökkuşağının başına çağırır.

### 2. Sayma 🍎
- Hikâye: Işıltı çok acıkmıştır. Feza ona elma toplar.
- İlk sayma görevinde **5 elma** vardır; sonraki sayma görevlerinde elma sayısı 3 ile 7 arasında değişir.
- Her elmada anlatıcı sayıyı söyler (bir, iki, üç…), ardından kaç elma kaldığını bildirir; sondan bir önce "son bir elma" der.
- Hepsi toplanınca toplam sayı söylenir. 5 elmada anlatıcı bir elin beş parmağını da sayar.
  Işıltı elmaları yer, kalpler çıkar ve gökkuşağı tamamen belirir.

### 3. Şekiller 🎈
- Hikâye: Çocukların şekilli balonları uçup gitmiştir.
- Beş balon vardır: **daire, kare, üçgen, yıldız ve kalp**. Sıra her seferinde karışıktır.
- Anlatıcı her şeklin bir özelliğini söyler (daire yuvarlaktır ve köşesi yoktur; karenin dört kenarı, üçgenin üç köşesi, yıldızın beş ucu vardır; kalp sevgiyi anlatır).
- Yanlış balona dokunursan anlatıcı hangi şekle dokunduğunu ve şimdi hangisinin arandığını söyler.
- Bütün balonlar bulununca çocuklar mutlu olur ve gökkuşağı belirir.

### Övgü
"Aferin Feza", "Harikasın", "Bravo", "Çok güzel" ve "Süpersin Feza" gibi sözler her doğru cevapta değil,
**ara sıra** (üç dört başarıda bir) ve hep aynı söz olmadan söylenir.

## Gökkuşağına tırmanış ve kaydırak

1. **Hazır olunca:** Görev bitince başlangıçtaki daire ve yıldız sarı yanıp söner; haritada da yıldız belirir.
   Hazır değilken oraya gidersen anlatıcı önce görevi bitirmeyi hatırlatır.
2. **Tırmanış:** Yıldızlı daireye girince Işıltı gökkuşağına tırmanmaya başlar. Yol boyunca yanlarda **1'den 20'ye** kadar numaralı levhalar vardır.
   Işıltı her levhaya varınca anlatıcı o sayıyı söyler; sayma seslendirmeyle birlikte ilerler, sıçrayan levha renkli pırıltıya dönüşür.
3. **Tepe:** Anlatıcı gökkuşağının tepesinde olduğunuzu söyler, şehrin küçük göründüğünü anlatır ve
   bir **"Biliyor musun?"** bilgisi verir (gökkuşağı, bulutlar, güneş ve renkler hakkında; sırayla döner). Sonra Feza el sallar ve **Kay! 🌈** düğmesi çıkar.
   Düğmeye (ya da ekrana, ya da Boşluk'a) basınca kayış başlar; bir süre basılmazsa kayış kendiliğinden başlar.
4. **Kayış:** Işıltı eğim boyunca giderek hızlanır; uzun, süzülen bir yolculuktur. Parmağını ekranda sağa sola kaydırarak
   yedi şeritten birine geç. Yolda **altın yıldızlar** vardır; topladıkça ⭐ sayacı artar ve anlatıcı yıldızları sayar (en çok 20).
   Rengârenk **halkaların** içinden geçersin. Anlatıcı yolda üç kez neşeyle seslenir. Kayarken rüzgâr sesi duyulur.
5. **İniş:** Kayış parktaki çocukların yanında biter; konfeti patlar, çocuklar alkışlar, anlatıcı topladığın yıldızları söyler.
   Gökkuşağı yavaşça kaybolur ve sıradaki görev başlar.

## Mini harita

Sol altta şehrin kuşbakışı çizimi durur.
- Üstünde **aranan şeyler** görünür: renkli yıldızlar, elmalar, şekilli balonlar. Sıradaki hedefin etrafında **sarı bir halka** yanıp söner.
- **Büyük gökkuşağı** haritada çizilidir; hazır değilken silik, hazırken parlak görünür. Başlangıç daireye giden yol yanıp sönen sarı yıldızla gösterilir.
- Feza ve Işıltı pembe bir işaretle görünür; yön oku nereye baktığını gösterir. Yürürken hem Feza (👦) hem Işıltı (🦄) ayrı gösterilir.
- Haritadaki bir hedefe ya da boş bir yere dokununca Işıltı oraya binaların etrafından dolaşarak gider.
- Harita kayarken ve tırmanırken kaybolur; ekran boyutuna göre küçülüp büyür ve diğer düğmelerle çakışmaz.

## Mola ve ayarlar

Oyunda mola menüsü, zorluk seçeneği ya da ayar ekranı yoktur; çocuğun karşısına seçim çıkmaz. Ayarlar şunlardır:

- **Hangi Feza:** Başlangıçta Gökkuşağı Feza ya da Feza seçilir.
- **🎵 Müzik:** Sağ üstteki düğmeyle açılıp kapanır. Anlatıcı konuşurken müzik kendiliğinden kısılır.
- **🔊 Tekrar söyle:** Son söylenen ya da yapılacak işi yeniden anlatır.
- **Sessiz açma:** Adrese `?sessiz` eklenir. Bu modda hiç ses çıkmaz.
- **Hareket azaltma:** Cihazın "hareketi azalt" ayarı açıksa kamera dönüşleri ve su dalgası gibi süs hareketleri durur, animasyonlar kapanır.
- **Ekran ayarı:** Dokunmatik cihazda oyun, akıcı kalması için biraz daha düşük çözünürlükte çizilir ve oyun sırasında bu değişmez.
  Dar ya da yatay ekranlarda düğmeler ve harita birbirine karışmayacak şekilde yeniden düzenlenir.
- **Tam ekran:** Dokunmatik cihazda başlarken oyun tam ekran olmaya çalışır; iPad'de Ana Ekrana eklenmişse zaten tam ekran açılır.

## Dosyalar

| Dosya / klasör | Ne işe yarar |
|---|---|
| `index.html` | Oyunun giriş ekranı, düğmeler ve görünüm |
| `game.js` | Oyunun ana kodu: şehir, Feza, Işıltı, çocuklar, görevler, kaydırak, harita, müzik ve anlatıcı cümleleri |
| `navigation.js` | Tek dokunuşla güvenli rota bulma (binaları ve çeşmeyi dolaşır) ve hızlı koşuda hedef yakalama |
| `assets/surfaces.js` | Taş, ahşap, kiremit ve çim yüzeyleri (dosyaya gömülü küçük resimler) |
| `vendor/three.js` | 3D kütüphanesi (three.js r170, MIT lisansı) |
| `voice/*.mp3`, `voice/manifest.js`, `voice/manifest.json` | Türkçe kadın sesiyle kaydedilmiş anlatıcı cümleleri (227 kayıt) ve hangi cümlenin hangi dosya olduğunu gösteren liste |
| `voice/lines.json` | Oyunda söylenen bütün cümlelerin listesi |
| `voice/trimmed.txt` | Başı sonu kırpılmış kayıtların listesi |
| `gen_voice.py` | Cümle değişirse sesleri yeniden kaydeder |
| `manifest.webmanifest`, `sw.js`, `icons/` | iPad'de uygulama gibi açılma, simge (180, 192 ve 512 piksel) ve internetsiz çalışma |
| `serve.py` | Yerel sunucu; iPad'i aynı Wi-Fi'dan bağlamak ve cümle listesini kaydetmek için |
| `yayinla.command` | Çift tıklayınca değişiklikleri GitHub'a gönderir |
| `ASSET-LICENSES.md` | Yüzey dokularının kaynakları ve lisansları |

## Sesler

Anlatıcı **tr-TR-EmelNeural** adlı doğal Türkçe kadın sesidir (Microsoft Edge'in çevrimiçi sesi). Bütün cümleler önceden kaydedilmiş mp3'lerdir;
tarayıcının kendi yabancı aksanlı sesi kullanılmaz. Kayıtların başındaki ve sonundaki sessizlik kırpılır, böylece tepkiler ve sayma anında duyulur.
Müzik, nal sesi, yıldız zili, rüzgâr gibi diğer sesler oyunun içinde üretilir; ayrı ses dosyası yoktur.

## Cümleleri değiştirmek

Oyundaki tüm cümleler `game.js` içindeki `LN` bölümündedir (sayıları, renk adlarını, arkadaş adlarını içeren cümle kalıpları da buradan üretilir).
Bir cümleyi değiştirdikten ya da cümle ekledikten sonra:

```bash
python3 -m pip install edge-tts
python3 serve.py          # açık bırakın, tarayıcıda http://localhost:8765 açın
# tarayıcının konsolunda:  __saveLines()
python3 gen_voice.py      # sadece eksik cümleleri seslendirir (internet gerekir)
```

`__saveLines()` oyundaki bütün cümleleri `voice/lines.json` dosyasına yazar; `gen_voice.py` yalnız henüz kaydı olmayanları seslendirir,
listede kalmayan cümlelerin kayıtlarını siler ve `voice/manifest.js` ile `voice/manifest.json` dosyalarını günceller.
`ffmpeg` kuruluysa (`brew install ffmpeg`) kayıtların başındaki ve sonundaki sessizlik otomatik kırpılır.

Okunuşu düzeltilecek kelimeler `gen_voice.py` içindeki **`PRONOUNCE`** listesindedir (ekranda yazı aynı kalır, yalnız söylenişi değişir).
Şu an listede **unicorn → "yunikorn"** vardır. Ses motoru "Aa" gibi kısa büyük harfli sözcükleri kısaltma sanabilir;
cümle eklerken böyle sözcükler yerine "Bak bak", "Vay" gibi sözler kullanın.

## Kaynaklar ve lisanslar

- **three.js** (r170): MIT lisansı, `vendor/three.js`.
- **Yüzey dokuları:** [Poly Haven](https://polyhaven.com/license) kaynaklarından, CC0 1.0 lisansıyla: Stone Wall 02, Wood Planks, Roof Tiles 14, Leafy Grass.
  Pastel renklere uyarlanıp 512 piksele küçültülmüş hâlleri `assets/surfaces.js` içindedir. Ayrıntılar ve üretici adları: [ASSET-LICENSES.md](ASSET-LICENSES.md).
- **Anlatıcı sesi:** Microsoft Edge tr-TR-EmelNeural sesiyle üretilmiş kayıtlar.
- Feza, Işıltı, çocuklar, şehir, müzik ve ses efektleri bu oyun için kodla çizilmiş ve üretilmiştir.
