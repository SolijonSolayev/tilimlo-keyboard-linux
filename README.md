# Tilimlo — Linux uchun o‘zbekcha klaviatura

**ö, ğ, ş, ç harflarini klaviaturadan bevosita yozing.** Tilimlo Debian oilasidagi Linux tizimlari uchun o‘zbekcha klaviatura tartibidir.

**Sayt:** [tilimlo.uz](https://tilimlo.uz) · **Versiya:** `1.0.0~preview3` · **Paket:** `tilimlo-keyboard` · **Layout:** `tilimlo`

[Paketni yuklab olish](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb) · [Manba kodi](src/) · [Avtomatik sinovlar](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/actions/workflows/debian-package.yml) · [Muammo bildirish](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/issues)

Tilimlo o‘rnatilgach, tizimingizning klaviatura sozlamalariga **Uzbek (Tilimlo, new Latin)** tartibi qo‘shiladi. Alohida dastur oynasini ochish yoki har safar terminalda buyruq bajarish talab qilinmaydi. Tartibni bir marta tanlab, matn muharriri, brauzer va boshqa grafik ilovalarda yozasiz.

Bu klaviatura tayyor matnni tarjima yoki transliteratsiya qilmaydi: `sh` yozsangiz, u avtomatik `ş`ga aylanmaydi. Belgilar tegishli tugmalar orqali kiritiladi. Ishlatish vaqtida internet, hisob yoki MCP plugin kerak emas.

> **`chmod +x` kerakmi?** `.deb` paketni o‘rnatish uchun **yo‘q**. `python3 build-package.py` bilan paket yig‘ish uchun ham **yo‘q**. [Batafsil izoh](#permissions).

## Mundarija

1. [Moslik va talablar](#requirements)
2. [Tez boshlash](#quick-start)
3. [Yuklash va o‘rnatish usullari](#installation)
4. [Fayl yaxlitligini tekshirish](#checksums)
5. [O‘rnatilganini tekshirish](#verify-install)
6. [Klaviaturani yoqish va almashtirish](#activation)
7. [Asosiy harflarni terish](#typing)
8. [AltGr va qo‘shimcha belgilar](#symbols)
9. [`chmod`, `sudo` va fayl huquqlari](#permissions)
10. [Muammolarni hal qilish](#troubleshooting)
11. [Yangilash va olib tashlash](#maintenance)
12. [Manbadan yig‘ish va loyiha tuzilishi](#development)

<a id="requirements"></a>
## 1. Moslik va talablar

| Muhit | Tekshiruv holati |
|---|---|
| Debian 12 — Bookworm | Konteynerda o‘rnatish, XKB kompilyatsiyasi, qayta o‘rnatish, registrni yangilash va olib tashlash o‘tgan |
| Debian 13 — Trixie | Xuddi shu avtomatik tekshiruvlar o‘tgan |
| Kali Linux | `preview3` ishlashi foydalanuvchi tomonidan tasdiqlangan; aniq Kali versiyasi va ish stoli qayd etilmagan |
| Ubuntu, Linux Mint va boshqa Debian asosidagi tizimlar | Mo‘ljallangan tizimlar; har bir versiya va ish stoli alohida sinovdan o‘tmagan |

Joriy paket **sinov versiyasi**. Konteyner sinovlari grafik ilovalarda barcha tugmalar, Caps Lock va aksent birikmalari tekshirilganini anglatmaydi. Bajarilgan tekshiruvlar [VALIDATION.txt](downloads/VALIDATION.txt)da keltirilgan.

**Kerak bo‘ladi:** grafik ish stoliga ega Debian asosidagi tizim, paket o‘rnatish huquqi va yuklash uchun internet. Zarur bog‘liqliklar — `xkb-data` hamda Python 3.9 yoki yangirog‘i — APT tomonidan o‘rnatiladi.

Paket `all` arxitekturasida: amd64 va arm64 uchun alohida fayl tanlash talab qilinmaydi. Bu arxitekturaga bog‘liq bajariladigan dastur emas, XKB ma’lumotlari va Python yordamchi kodidir. Har bir arxitekturada amaliy sinov o‘tkazilgani da’vo qilinmaydi.

Layout X11/Wayland grafik muhitlari uchun mo‘ljallangan. **TTY matn konsoli**, Windows, macOS, Android va iOS ushbu `.deb` paket bilan sozlanmaydi.

### Buyruqlarni bajarish bo‘yicha qisqa izoh

Ilovalar menyusidan **Terminal**, **Konsole** yoki **Xfce Terminal**ni oching. Ko‘p tizimlarda `Ctrl + Alt + T` ishlaydi. Buyruqni ko‘chirib, terminalga qo‘ying va **Enter** bosing. Terminalda qo‘yish uchun odatda `Ctrl + Shift + V` ishlatiladi.

`sudo` parol so‘rasa, Linux hisobingiz parolini kiriting. Parol yozilayotganda ekranda belgilar ko‘rinmasligi odatiy holat. Kod bloklarida terminalning `$` yoki `#` taklif belgilari keltirilmagan — faqat buyruqlarni ko‘chiring.

<a id="quick-start"></a>
## 2. Tez boshlash

Terminal bilan ishlay olsangiz, quyidagi usul yetarli. Kengroq izoh va boshqa usullar keyingi bo‘limda.

```bash
sudo apt update
sudo apt install wget
wget -O /tmp/tilimlo-keyboard_1.0.0~preview3_all.deb 'https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb'
sudo apt install /tmp/tilimlo-keyboard_1.0.0~preview3_all.deb
```

Buyruqlarni ketma-ket bajaring. Yuklash yoki o‘rnatishda xato chiqsa, keyingi bosqichga o‘tishdan oldin [muammoni tekshiring](#troubleshooting). `apt update` paketlar ro‘yxatini yangilaydi; bu yerda butun tizimni yangilash talab qilinmaydi.

So‘ng:

1. Hujjatlaringizni saqlang, **Log Out** qiling va qayta kiring.
2. **Keyboard / Input Sources / Layouts** sozlamalaridan **Uzbek (Tilimlo, new Latin)**ni qo‘shing.
3. Paneldagi klaviatura indikatoridan Tilimloni tanlang.
4. Matn muharririda `[`, `]`, `;`, `'` tugmalarini bosing: **`öğşç`** chiqishi kerak.

`/tmp` vaqtinchalik papka; kompyuter qayta yoqilganda yuklangan `.deb` o‘chishi mumkin. Bu o‘rnatilgan klaviaturani olib tashlamaydi.

<a id="installation"></a>
## 3. Yuklash va o‘rnatish usullari

Quyidagi usullardan **bittasini tanlang**. Bir paketni barcha usullar bilan ketma-ket o‘rnatish shart emas. APT usuli bog‘liqliklarni ham boshqargani uchun tavsiya etiladi.

### A. Brauzer orqali yuklash va APT bilan o‘rnatish

1. [Tayyor `.deb` paketni yuklab oling](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb).
2. Fayl menejerida u saqlangan papkani oching. Odatda bu **Downloads / Yuklamalar** bo‘ladi, ammo nomi tizim tiliga qarab farqlanadi.
3. Papkaning bo‘sh joyida o‘ng tugmani bosib **Open in Terminal / Terminalda ochish**ni tanlang, agar shu imkoniyat mavjud bo‘lsa.
4. Fayl mavjudligini tekshiring va o‘rnating:

```bash
ls -l ./tilimlo-keyboard_1.0.0~preview3_all.deb
sudo apt install ./tilimlo-keyboard_1.0.0~preview3_all.deb
```

`./` — joriy papka degani. Uni qoldiring: bu APT’ga mahalliy faylni o‘rnatish kerakligini bildiradi. Brauzer nomga `(1)` qo‘shgan bo‘lsa, buyruqda faylning haqiqiy nomini qo‘shtirnoq ichida yozing yoki fayl nomini asl holiga qaytaring.

### B. Terminal orqali yuklash: Wget yoki cURL

Wget bilan to‘liq yo‘l [Tez boshlash](#quick-start) bo‘limida berilgan. Agar cURL ishlatmoqchi bo‘lsangiz:

```bash
sudo apt update
sudo apt install curl
curl -fL 'https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb' -o /tmp/tilimlo-keyboard_1.0.0~preview3_all.deb
sudo apt install /tmp/tilimlo-keyboard_1.0.0~preview3_all.deb
```

`-L` GitHub’ning yo‘naltirishlarini kuzatadi, `-f` HTTP xatosida yuklashni xato bilan tugatadi, `-o` saqlanadigan faylni belgilaydi. Yuklash muvaffaqiyatsiz tugasa, o‘rnatish buyrug‘ini bajarmang.

### C. Grafik paket o‘rnatuvchisi orqali

Bu usul tizimingizda mahalliy `.deb` fayllarni ochadigan dastur mavjud bo‘lsa ishlaydi:

1. `.deb` faylni yuklab oling.
2. Faylni ikki marta bosing yoki **Open With** orqali **GDebi**, **QApt** yoxud `.deb`ni qo‘llaydigan dastur markazini tanlang.
3. Paket nomi **tilimlo-keyboard** ekanini tekshirib, **Install**ni bosing.
4. Administrator parolini kiriting va o‘rnatish tugashini kuting.

Fayl arxiv menejerida ochilsa, undan fayllarni tizimga qo‘lda ko‘chirmang. Yuqoridagi APT usulidan foydalaning. Grafik o‘rnatuvchilarning mavjudligi va ishlashi distributivga bog‘liq; bu usul alohida tekshirilmagan.

### D. `dpkg` orqali — tajribali foydalanuvchilar uchun

Paket joylashgan papkada:

```bash
sudo dpkg -i ./tilimlo-keyboard_1.0.0~preview3_all.deb
```

`dpkg` bog‘liqliklarni internetdan o‘zi yuklamaydi. Aynan yetishmayotgan bog‘liqlik haqida xato chiqsa, APT taklif qiladigan o‘zgarishlarni ko‘rib, quyidagini bajaring:

```bash
sudo apt --fix-broken install
```

Bu buyruq boshqa tugallanmagan paket amallarini ham tuzatishni taklif qilishi mumkin. Shu sababli yangi foydalanuvchilar uchun `apt install ./...deb` usuli qulayroq.

### Internet bo‘lmagan kompyuterga o‘rnatish

`.deb`ni boshqa kompyuterda yuklab, USB orqali ko‘chirish mumkin. Ammo nishon tizimda `xkb-data` va mos Python hali o‘rnatilmagan bo‘lsa, ularning paketlari ham kerak bo‘ladi. Bitta `.deb` barcha tizimlar uchun to‘liq oflayn to‘plam emas.

<a id="checksums"></a>
## 4. Fayl yaxlitligini tekshirish

Bu bosqich ixtiyoriy. U yuklangan fayl repozitoriydagi nazorat summasiga mosligini tekshiradi. Paket va summa faylini **bir papkaga**, asl nomlari bilan saqlang. Masalan:

```bash
mkdir -p "$HOME/tilimlo-download"
cd "$HOME/tilimlo-download"
wget -O 'tilimlo-keyboard_1.0.0~preview3_all.deb' 'https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb'
wget -O SHA256SUMS.txt 'https://raw.githubusercontent.com/SolijonSolayev/tilimlo-keyboard-linux/main/downloads/SHA256SUMS.txt'
sha256sum --ignore-missing -c SHA256SUMS.txt
```

Kutiladigan natija:

```text
tilimlo-keyboard_1.0.0~preview3_all.deb: OK
```

`--ignore-missing` yuklanmagan manba arxivini tekshirishdan tashlab o‘tadi. Paket uchun `OK` chiqishini tekshiring. `FAILED` chiqsa, faylni qayta yuklang. Nazorat summasi raqamli imzo o‘rnini bosmaydi; paket hozircha imzolanmagan.

<a id="verify-install"></a>
## 5. O‘rnatilganini tekshirish

Qaysi usul bilan o‘rnatganingizdan qat’i nazar, terminalda:

```bash
dpkg-query -W -f='${Status}\n${Version}\n' tilimlo-keyboard
```

Kutiladigan natija:

```text
install ok installed
1.0.0~preview3
```

Bu paket o‘rnatilganini bildiradi. U hali faol klaviatura sifatida tanlanganini bildirmaydi. Keyingi bo‘limni ham bajaring.

<a id="activation"></a>
## 6. Klaviaturani yoqish va almashtirish

Ish stolingizga mos yo‘lni tanlang. Menyu nomlari tizim versiyasi va tiliga qarab farq qilishi mumkin. Qaysi ish stoli ishlayotganini bilmasangiz:

```bash
echo "$XDG_CURRENT_DESKTOP"
```

**Mavjud English/US yoki boshqa klaviaturangizni saqlang.** Tilimloni qo‘shimcha tartib sifatida qo‘shing, shunda ular orasida almashishingiz mumkin.

### GNOME / Ubuntu’ning odatiy ish stoli

1. **Settings → Keyboard → Input Sources**ni oching. Ba’zi versiyalarda bu **Region & Language → Input Sources** ichida bo‘ladi.
2. **+ / Add Input Source**ni bosing.
3. `Uzbek` yoki `Tilimlo` deb qidiring. Kerak bo‘lsa **Other** yoki uch nuqtali qo‘shimcha ro‘yxatni oching.
4. **Uzbek (Tilimlo, new Latin)**ni tanlab, **Add**ni bosing.
5. Yuqori paneldagi til/klaviatura belgisidan Tilimloni tanlang. GNOME’da odatda **Super + Space** keyingi tartibga o‘tadi; Super — Windows logotipli tugma.

Ro‘yxatda ko‘rinmasa, [GNOME uchun muqobil usuldan](#gnomeda-royxatga-qoshishning-muqobil-usuli) foydalaning.

### KDE Plasma

1. **System Settings**ni oching va `Keyboard` deb qidiring.
2. **Keyboard → Layouts**ga o‘ting. Eski versiyalarda **Input Devices → Keyboard → Layouts** bo‘lishi mumkin.
3. **Configure layouts**ni yoqing, **Add**ni bosing.
4. **Uzbek (Tilimlo, new Latin)**ni topib qo‘shing va **Apply**ni bosing.
5. Paneldagi klaviatura indikatoridan Tilimloni tanlang. Almashish tugmasini shu sozlamalarning o‘zida tanlashingiz mumkin.

### Xfce — Kali va boshqa tizimlar

1. **Settings → Keyboard → Layout**ni oching.
2. Qo‘lda tartib qo‘shish uchun zarur bo‘lsa **Use system defaults** belgisini olib tashlang.
3. **Add** orqali **Uzbek (Tilimlo, new Latin)**ni qo‘shing.
4. **Change layout option** yoki almashish sozlamasidan qulay tugmalarni tanlang.
5. Tanlangan tugmalar yoki paneldagi klaviatura indikatoridan Tilimloga o‘ting.

### Linux Mint Cinnamon

**System Settings → Keyboard → Layouts**ni oching. **+** orqali `Uzbek` yoki `Tilimlo`ni qidiring va yangi tartibni qo‘shing. Paneldagi klaviatura indikatoridan uni tanlang. Bu yo‘l Cinnamon versiyasiga qarab farq qilishi mumkin va alohida amaliy sinovdan o‘tkazilmagan.

<a id="typing"></a>
## 7. Asosiy harflarni terish

Oddiy matn muharririni oching va faol klaviatura **Tilimlo** ekanini tekshiring. Quyidagi tugmalar nomlari **US inglizcha klaviaturada bosilgan belgilar** bo‘yicha berilgan:

| Klaviaturadagi tugma | Oddiy bosish | Shift bilan |
|---|---|---|
| `[` — P harfining o‘ngidagi birinchi tugma | ö | Ö |
| `]` — P harfining o‘ngidagi ikkinchi tugma | ğ | Ğ |
| `;` — L harfining o‘ngidagi birinchi tugma | ş | Ş |
| `'` — L harfining o‘ngidagi ikkinchi tugma | ç | Ç |

1. Shu to‘rtta tugmani navbat bilan bosing: **`öğşç`** chiqishi kerak.
2. Shift’ni bosib turib takrorlang: **`ÖĞŞÇ`** chiqishi kerak.
3. Quyidagi gapni o‘zingiz terib ko‘ring:

```text
Özbekiston şaharlari gözal. Men özbekça yaxşi yoza olaman.
```

Gapni shunchaki nusxalab qo‘yish klaviaturani tekshirmaydi: harflarni tugmalardan terish kerak.

**Caps Lock** asosiy harflarning katta-kichikligini boshqarish uchun mo‘ljallangan. Aniq natijani sinovda tekshiring; katta harf yozishning sodda usuli — **Shift + harf**.

<a id="symbols"></a>
## 8. AltGr va qo‘shimcha belgilar

**AltGr — klaviaturaning o‘ng tomonidagi Alt tugmasi.** Quyidagi jadvalda tugmalar birga bosiladi. Masalan, `AltGr + [` yozish uchun o‘ng Alt’ni bosib turib `[` tugmasini bosing.

| Tugma | Oddiy | Shift | AltGr | AltGr + Shift |
|---|---|---|---|---|
| `[` | ö | Ö | `[` | `{` |
| `]` | ğ | Ğ | `]` | `}` |
| `;` | ş | Ş | … | — bo‘sh |
| `'` | ç | Ç | `'` | `` ` `` |
| `\` | `;` | `:` | `\` | `\|` |
| `` ` `` | ’ | `"` | ‘ | `~` |
| `,` | `,` | “ | `<` | « |
| `.` | `.` | ” | `>` | » |
| `-` | `-` | `_` | – | — |
| `=` | `=` | `+` | ≠ | ± |
| `I` | i | I | ı | İ |
| `U` | u | U | ü | Ü |
| `2` | 2 | `@` | ™ | € |
| `3` | 3 | `#` | £ | № |
| `8` | 8 | `*` | • | ° |
| `9` | 9 | `(` | ‘ | — bo‘sh |
| `0` | 0 | `)` | ’ | — bo‘sh |
| `G` | g | G | © | — bo‘sh |
| `R` | r | R | ® | — bo‘sh |
| Space | oddiy bo‘shliq | oddiy bo‘shliq | uzilmaydigan bo‘shliq | — bo‘sh |

**“— bo‘sh”** — shu qatlam uchun maxsus belgi belgilanmagan. `-` tugmasining oxirgi ustunidagi **—** esa haqiqiy uzun tire.

`AltGr + E`, `AltGr + N` va `AltGr + 6` mos ravishda acute, tilde va circumflex aksentlari uchun **dead key** vazifasini bajaradi. Bunday tugmadan keyin belgi darhol chiqmasligi mumkin: u keyingi harfni kutadi. Birikmalar natijasi Linux ilovasi va kiritish tizimiga bog‘liq; Windows bilan to‘liq bir xillik tekshirilmagan.

<a id="permissions"></a>
## 9. `chmod`, `sudo` va fayl huquqlari

**Oddiy o‘rnatish va foydalanishda `chmod +x` bajarmaysiz.** `.deb` — ishga tushiriladigan skript emas, paket menejeri ochadigan arxiv. Uning ichidagi yordamchi kod uchun kerakli bajarish huquqlari paketning o‘zida belgilangan.

| Amal | `chmod +x` kerakmi? | To‘g‘ri yo‘l |
|---|---|---|
| `.deb` paketni o‘rnatish | Yo‘q | `sudo apt install ./tilimlo-keyboard_1.0.0~preview3_all.deb` |
| Klaviaturadan foydalanish | Yo‘q | Sozlamalardan Tilimloni tanlash |
| Python skripti orqali paket yig‘ish | Yo‘q | `python3 build-package.py` |
| `tar.gz` manba arxivini ochish | Yo‘q | `tar -xzf ARXIV_NOMI.tar.gz` |
| Boshqa loyihadagi skriptni `./script.sh` bilan bevosita bajarish | Bajarish huquqi yo‘q bo‘lsa, kerak bo‘lishi mumkin | Skriptning hujjatiga amal qilinadi; bu loyihada `install.sh` yo‘q |

`chmod +x` faylga bajarish ruxsatini beradi. U administrator huquqini bermaydi, yetishmayotgan bog‘liqliklarni o‘rnatmaydi va `.deb` ichidagi xatoni tuzatmaydi. Tushuntirish: [GNU chmod qo‘llanmasi](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html).

Repozitoriydagi `build-package.py` **`python3 build-package.py`** bilan bajariladi. Uni `./build-package.py` tarzida ishga tushirish uchun huquqlarni o‘zgartirishga hojat yo‘q. `register-layout.py`ni ham odatiy o‘rnatishda qo‘lda ishga tushirmang — uni paket menejeri chaqiradi.

**`sudo` faqat tizim paketini o‘rnatish yoki olib tashlash kabi amallarda kerak.** Yuklash, faylni tekshirish, paket yig‘ish va GNOME’ning shaxsiy klaviatura sozlamalarini o‘zgartirish odatiy foydalanuvchi sifatida bajariladi.

`Permission denied` ko‘rsangiz, avval qaysi buyruq va qaysi faylga tegishli ekanini tekshiring. Bu yo‘riqnomadagi amallar uchun `chmod 777`, uy papkasini hammaga ochish yoki tizim papkalariga ommaviy bajarish huquqi berish kerak emas.

<a id="troubleshooting"></a>
## 10. Muammolarni hal qilish

### Eski preview2 paketidagi `register-layout.dpkg-new` xatosi

`cannot create ... register-layout.dpkg-new ... No such file or directory` preview2 arxivida kerakli papka yozuvlari bo‘lmagani sababli chiqqan. Bu **preview3’da tuzatilgan**. Paket papkalarini qo‘lda yaratish yoki `chmod` qo‘llash shart emas: [Tez boshlash](#quick-start) orqali yangi paketni o‘rnating.

### `_apt ... Permission denied` ogohlantirishi

APT uy papkangizdagi `.deb`ni cheklangan `_apt` hisobi bilan o‘qiy olmasa, `Download is performed unsandboxed as root` ogohlantirishi chiqishi mumkin. Bu har doim o‘rnatish muvaffaqiyatsiz tugaganini anglatmaydi: yakuniy holatni `dpkg-query` bilan tekshiring.

[Tez boshlash](#quick-start) usulida fayl `/tmp`ga saqlanadi. Uy papkangizning huquqlarini o‘zgartirish kerak emas. Agar boshqa `dpkg` xatosi ham bo‘lsa, aynan o‘sha xato matnini alohida tekshiring.

### “No such file or directory” yoki paket topilmadi

Terminal paket saqlangan papkada emas yoki fayl nomi boshqacha. Joriy papka va paketlarni tekshiring:

```bash
pwd
ls -l *.deb
```

Fayl menejerida kerakli papkani ochib, **Open in Terminal**dan foydalaning. Brauzer takroriy yuklashda nomga `(1)` qo‘shgan bo‘lsa, buyruqda aynan o‘sha nomni qo‘shtirnoq ichida yozing yoki fayl nomini asl holiga qaytaring.

### Administrator huquqi yoki parol bilan muammo

`sudo` uchun o‘z Linux hisobingiz paroli kerak. Hisobingizda administrator huquqi bo‘lmasa, tizim administratoriga murojaat qiling. Bu GitHub yoki Tilimlo paroli emas.

### O‘rnatilgan, lekin klaviatura ro‘yxatida yo‘q

1. O‘rnatish holatini 5-bo‘limdagi `dpkg-query` bilan tekshiring.
2. Seansdan chiqib qayta kiring; Settings’ni qayta oching.
3. `Uzbek` va `Tilimlo`ni qidiring, **Other** bo‘limini ham tekshiring.
4. Layout fayli mavjudligini tekshiring:

```bash
ls -l /usr/share/X11/xkb/symbols/tilimlo
```

Fayl yo‘q bo‘lsa, paket joylashgan papkada qayta o‘rnating:

```bash
sudo apt install --reinstall ./tilimlo-keyboard_1.0.0~preview3_all.deb
```

#### GNOME’da ro‘yxatga qo‘shishning muqobil usuli

Bu usul **faqat GNOME** uchun va uni oddiy foydalanuvchi terminalida, **sudo’siz** bajarish kerak. U mavjud klaviaturalar ro‘yxatini saqlab, Tilimloni qo‘shadi. Butun blokni birga ko‘chirib bajaring:

```bash
python3 - <<'PY'
import ast
import subprocess

schema = 'org.gnome.desktop.input-sources'
text = subprocess.check_output(
    ['gsettings', 'get', schema, 'sources'], text=True
)
sources = ast.literal_eval(text.removeprefix('@a(ss) ').strip())
if ('xkb', 'tilimlo') not in sources:
    sources.append(('xkb', 'tilimlo'))
    subprocess.run(
        ['gsettings', 'set', schema, 'sources', repr(sources)], check=True
    )
print('Tilimlo ro‘yxatda. Paneldan yoki Super+Space bilan tanlang.')
PY
```

Kam ishlatiladigan manbalarni ko‘rsatish GNOME’ning rasmiy tavsiyalarida ham bor: zarur bo‘lsa `gsettings set org.gnome.desktop.input-sources show-all-sources true`ni bajaring va Settings’ni qayta oching.

### Tugmalar hali ham inglizcha belgilar chiqaryapti

Paketni o‘rnatishning o‘zi yetmaydi. Paneldagi indikator orqali **Tilimlo**ni faol tanlang. Ochiq matn muharririni qayta ishga tushirib sinang. Boshqa klaviatura faol bo‘lsa, `[` tugmasi `ö` yozmaydi.

### AltGr ishlamayapti

O‘ng Alt’dan foydalaning. Avval `AltGr + [` kombinatsiyasini sinang: `[` chiqishi kutiladi. Desktop’dagi boshqa qisqartma o‘ng Alt’ni egallamaganini tekshiring. Virtual mashina yoki masofaviy ish stolida tugmani asosiy tizim ushlab qolishi mumkin.

### “setxkbmap does not work in Wayland”

Seans turini tekshiring:

```bash
echo "$XDG_SESSION_TYPE"
```

`wayland` chiqsa, klaviaturani desktop’ning **Input Sources / Layouts** sozlamalaridan tanlang. `setxkbmap` Wayland klaviaturasini boshqarmaydi.

Faqat **X11** seansida vaqtinchalik sinash mumkin:

```bash
setxkbmap -layout tilimlo
```

Bu joriy faol tartibni almashtiradi, doimiy o‘rnatish usuli emas. US inglizcha tartibga vaqtinchalik qaytish:

```bash
setxkbmap -layout us
```

### XKB kompilyatsiyasini tekshirish

Oddiy bosqichlar yordam bermasa, xatoni aniqlash uchun:

```bash
sudo apt install libxkbcommon-tools
xkbcli compile-keymap --layout tilimlo > /tmp/tilimlo.xkb
```

Xato chiqmasa, layout shu tizimdagi XKB kompilyatorida yig‘ilgan bo‘ladi. Bu barcha ilovalarda terish tekshiruvi o‘rnini bosmaydi. Xato chiqsa, uning matnini saqlang.

### Muammo haqida xabar berish

[GitHub Issues](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/issues) orqali quyidagilarni yozing:

- distributiv va versiya;
- ish stoli: GNOME, KDE, Xfce yoki Cinnamon;
- seans: X11 yoki Wayland;
- qaysi tugma bosildi, nima chiqishi kerak edi va nima chiqdi;
- terminal xatosi bo‘lsa, uning aniq matni.

Tizim haqidagi ma’lumotni quyidagilar bilan ko‘rish mumkin:

```bash
cat /etc/os-release
echo "$XDG_CURRENT_DESKTOP"
echo "$XDG_SESSION_TYPE"
dpkg-query -W tilimlo-keyboard
```

<a id="maintenance"></a>
## 11. Yangilash va olib tashlash

### Yangi versiyaga o‘tish

Yangi `.deb` chiqqanda uni [downloads/](downloads/) yoki yangilangan README havolasidan oling va `sudo apt install ./FAYL_NOMI.deb` bilan o‘rnating. `FAYL_NOMI.deb` o‘rniga yuklangan faylning haqiqiy nomi yoziladi. Odatda eski Tilimlo paketini avval o‘chirish talab qilinmaydi.

Loyiha hozircha APT repozitoriysi emas. `apt update` va `apt upgrade` GitHub’dan yangi Tilimlo versiyasini avtomatik yuklamaydi.

Yangilangandan keyin seansdan chiqib qayta kiring. Paket versiyasini [5-bo‘lim](#verify-install) yordamida tekshiring.

### Oldingi nomdagi paketdan ko‘chish

Bu faqat dastlabki `tilmoch-keyboard` paketini o‘rnatganlar uchun:

1. Boshqa ishlaydigan klaviaturaga o‘ting.
2. Sozlamalardagi eski tartibni ro‘yxatdan olib tashlang.
3. `sudo apt remove tilmoch-keyboard`ni bajaring.
4. Joriy `tilimlo-keyboard` paketini ushbu qo‘llanma bo‘yicha o‘rnating.

### Tilimloni olib tashlash

1. Paneldan English/US yoki boshqa ishlaydigan klaviaturaga o‘ting.
2. **Input Sources / Layouts** sozlamalaridan Tilimloni olib tashlang.
3. Terminalda bajaring:

```bash
sudo apt remove tilimlo-keyboard
```

4. Seansdan chiqib qayta kiring.

Paket o‘z layout fayli va tizim ro‘yxatidagi yozuvini olib tashlaydi. U foydalanuvchilarning shaxsiy Input Sources ro‘yxatini avtomatik tahrirlamaydi. Kompyuterda bir nechta hisob bo‘lsa, har bir hisobda Tilimlo yozuvini sozlamalardan olib tashlang.

Yuklab olingan `.deb`ni keyin o‘chirishingiz mumkin; u o‘rnatilgan paketdan alohida fayldir. `.deb`ni o‘chirishning o‘zi klaviaturani tizimdan olib tashlamaydi.

<a id="development"></a>
## 12. Manbadan yig‘ish va loyiha tuzilishi

Bu bo‘lim dasturchilar uchun. Faqat klaviaturadan foydalanmoqchi bo‘lsangiz, tayyor `.deb` yetarli.

### A. Tayyor manba arxividan yig‘ish

1. [Manba arxivini yuklab oling](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard-1.0.0-preview3-source.tar.gz).
2. Terminalni arxiv joylashgan papkada oching.
3. Quyidagilarni bajaring:

```bash
tar -xzf tilimlo-keyboard-1.0.0-preview3-source.tar.gz
cd tilimlo-keyboard-1.0.0-preview3
python3 build-package.py
```

Natija `dist/`ga yoziladi. Joriy versiya uchun paket:

```text
dist/tilimlo-keyboard_1.0.0~preview3_all.deb
```

Yig‘ish uchun **Python 3.10 yoki yangirog‘i** kerak; qo‘shimcha Python kutubxonasi talab qilinmaydi. Bu talab paketni ishlatishdagi Python 3.9 talabidan farq qiladi. Skript `Path.write_text(..., newline=...)` imkoniyatidan foydalanadi. `sudo` va `chmod +x` kerak emas.

Yig‘ilgan paketni shu papkadan o‘rnatish:

```bash
sudo apt install ./dist/tilimlo-keyboard_1.0.0~preview3_all.deb
```

### B. GitHub repozitoriysidan yig‘ish

```bash
sudo apt update
sudo apt install git python3
git clone https://github.com/SolijonSolayev/tilimlo-keyboard-linux.git
cd tilimlo-keyboard-linux/src
python3 --version
python3 build-package.py
```

`python3 --version` natijasi 3.10 yoki yangiroq ekanini tekshiring. Mavjud tizim Python’ini qo‘lda almashtirish talab qilinmaydi: eski tizimda tayyor `.deb`dan foydalanish mumkin.

Natijalar `src/dist/` ichida bo‘ladi; asl manba fayllari o‘zgarmaydi. Skript paket versiyasini o‘zidan oladi — uni ishga tushirish versiyani avtomatik oshirmaydi.

### Papkalar nimaga kerak?

```text
tilimlo-keyboard-linux/
├── README.md                  # Asosiy foydalanish qo‘llanmasi
├── downloads/                 # Yuklab olish uchun tayyor fayllar
│   ├── *.deb                  # O‘rnatiladigan paket
│   ├── *-source.tar.gz        # Manba kodining siqilgan nusxasi
│   ├── SHA256SUMS.txt         # Fayllarning nazorat summalari
│   └── VALIDATION.txt         # Tekshiruvlar va ularning chegaralari
├── src/                       # Paketni yaratadigan manbalar
│   ├── build-package.py       # Paket va manba arxivini yig‘ish
│   ├── register-layout.py     # Tizim klaviatura ro‘yxatini yangilash
│   ├── windows-layout.json    # Dastlabki Windows tugmalar jadvali
│   ├── keymap.json            # Hosil qilingan belgilar xaritasi
│   └── tilimlo                # Hosil qilingan XKB layout fayli
└── .github/workflows/         # Debian avtomatik sinovlari
```

**Oddiy foydalanuvchi uchun:** `downloads/`dagi `.deb` va shu README yetarli.

**Dasturchi uchun:** `build-package.py` XKB fayli va `keymap.json`ni `windows-layout.json` asosida qayta hosil qiladi. Faqat `src/tilimlo`ni tahrirlash yig‘iladigan paketni o‘zgartirmaydi; joriy yig‘ish skriptining ma’lumot manbasini hisobga olish kerak. Tugmalar tartibi foydalanuvchi taqdim etgan Windows jadvalidan ko‘chirilgan.

### Tizimga nima o‘rnatiladi?

| Joylashuv | Vazifasi |
|---|---|
| `/usr/share/X11/xkb/symbols/tilimlo` | Tugmalarning XKB tartibi |
| `/usr/lib/tilimlo-keyboard/register-layout` | Paket menejeri chaqiradigan registr yordamchisi |
| `/usr/share/doc/tilimlo-keyboard/` | Paket bilan keladigan qisqa ma’lumot va belgilar xaritasi |

Layout identifikatori **`tilimlo`**, standart variant **`basic`**. Eski X11/Wayland desktop sozlamalari bilan ishlash uchun paket `evdev/base` XML va LST ro‘yxatlariga belgilangan Tilimlo yozuvini qo‘shadi. Boshqa tartiblarning yozuvlari saqlanadi. `xkb-data` qayta o‘rnatilganda ro‘yxatni tiklash uchun dpkg trigger ishlatiladi.

Debian 12 va 13 konteynerlaridagi avtomatik sinovlar yangi o‘rnatish, yuklanadigan paketni qayta yig‘ilgan paket bilan solishtirish, XKB kompilyatsiyasi, qayta o‘rnatish, trigger va olib tashlashni tekshiradi. Ular grafik ish stolida tugmalarni qo‘lda bosish sinovining o‘rnini bosmaydi.

### Rasmiy ma’lumotnomalar

- [GNOME: klaviatura tartiblarini qo‘shish](https://help.gnome.org/gnome-help/keyboard-layouts.html)
- [KDE Plasma: klaviatura tartiblari](https://docs.kde.org/stable_kf6/en/plasma-desktop/kcontrol/keyboard/layouts.html)
- [Debian: klaviatura sozlamalari](https://wiki.debian.org/Keyboard)
- [GNU Coreutils: chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)
- [libxkbcommon: maxsus klaviatura konfiguratsiyasi](https://xkbcommon.org/doc/current/custom-configuration.html)

Savol yoki xato uchun [GitHub Issues](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/issues)dan foydalaning. Versiya, distributiv, ish stoli va xatoning aniq matnini keltiring.

