# Tilimlo — Linux uchun o‘zbekcha klaviatura

Tilimlo yangi o‘zbek lotin alifbosidagi **ö, ğ, ş, ç** harflarini klaviaturadan bevosita yozish imkonini beradi. Tugmalar joylashuvi foydalanuvchi taqdim etgan Windows klaviatura jadvali asosida ko‘chirilgan.

Loyiha sayti: **[tilimlo.uz](https://tilimlo.uz)**.

**Joriy versiya: `1.0.0~preview3` — sinov versiyasi.** 49 ta tugmaning Windows jadvaliga mosligi tekshirilgan. Debian 12 (Bookworm) va Debian 13 (Trixie) konteynerlarida yangi o‘rnatish, XKB kompilyatsiyasi, qayta o‘rnatish, `xkb-data` yangilanishidan keyingi ro‘yxat va olib tashlash tekshiruvlari muvaffaqiyatli o‘tdi. Grafik ish stolida klaviatura tanlash va amaliy terish, jumladan Kali’da, hali tekshirilmagan. [Avtomatik sinovlar](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/actions/workflows/debian-package.yml).

## Mundarija

1. [Nimalar kerak?](#1-nimalar-kerak)
2. [Paketni yuklab olish](#2-paketni-yuklab-olish)
3. [O‘rnatish](#3-ornatish)
4. [Klaviaturani yoqish](#4-klaviaturani-yoqish)
5. [Harflarni yozish va sinash](#5-harflarni-yozish-va-sinash)
6. [Qo‘shimcha belgilar](#6-qoshimcha-belgilar)
7. [Muammolarni hal qilish](#7-muammolarni-hal-qilish)
8. [Yangilash va olib tashlash](#8-yangilash-va-olib-tashlash)
9. [Manba kodidan paket yig‘ish](#9-manba-kodidan-paket-yigish)

## 1. Nimalar kerak?

- Debian oilasiga mansub Linux va grafik ish stoli.
- Dastur o‘rnatish uchun administrator huquqi: odatda `sudo` orqali.
- Paket va kerakli tizim bog‘liqliklarini yuklash uchun internet.

Maqsadli tizimlar: **Debian 12/13, Ubuntu 22.04/24.04, Linux Mint va shu tizimlarga asoslangan distributivlar**. Debian 12/13 uchun paket o‘rnatilishi konteynerda tekshirilgan; bu ro‘yxatdagi barcha grafik ish stollarida moslik tasdiqlangan degani emas.

Paket `all` arxitekturasida: amd64 va arm64 uchun alohida fayl tanlash shart emas. U grafik dasturlardagi XKB klaviatura tartibini o‘rnatadi; qora ekranli Linux konsoli — **TTY** uchun klaviatura o‘rnatmaydi.

**Bilish kerak:** bu alohida oynasi ochiladigan dastur emas. O‘rnatgandan keyin klaviatura sozlamalarida yangi yozuv paydo bo‘lishi kerak. U matnni tarjima qilmaydi va `sh`ni avtomatik `ş`ga almashtirmaydi. Ishlatish vaqtida internet, Tilimlo hisobi yoki MCP plugin kerak emas.

### Terminal nima va uni qanday ochaman?

Terminal — buyruq yoziladigan dastur. Ilovalar menyusidan **Terminal**, **Konsole** yoki **Xfce Terminal** deb qidiring. Ko‘p tizimlarda `Ctrl` + `Alt` + `T` ham uni ochadi.

Quyidagi kod bloklaridagi buyruqlarni terminalga ko‘chiring va **Enter** bosing. Nusxa ko‘chirish/qo‘yish menyusidan yoki terminaldagi `Ctrl` + `Shift` + `V`dan foydalanishingiz mumkin. `sudo` parol so‘rasa, Linux foydalanuvchingiz parolini yozing: yozayotganingiz ekranda ko‘rinmasligi odatiy holat.

## 2. Paketni yuklab olish

Ikki usuldan **bittasini** tanlang.

### A usul — brauzer orqali

1. [Tilimlo `.deb` paketini yuklab olish](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb) havolasini bosing.
2. Fayl nomi **`tilimlo-keyboard_1.0.0~preview3_all.deb`** ekanini tekshiring.
3. Fayl menejerida yuklangan fayl joylashgan papkani oching. Odatda bu **Downloads / Yuklamalar** papkasi.
4. Papkaning bo‘sh joyida o‘ng tugmani bosib **Open in Terminal / Terminalda ochish**ni tanlang, agar bunday band mavjud bo‘lsa.

Papka nomi tizim tiliga qarab farq qilishi mumkin. Terminal o‘sha papkada ochilganini tekshirish uchun:

```bash
ls -l ./tilimlo-keyboard_1.0.0~preview3_all.deb
```

Fayl nomi va hajmi chiqsa, keyingi bosqichga o‘ting. `No such file or directory` chiqsa, [muammolar bo‘limiga](#7-muammolarni-hal-qilish) qarang.

### B usul — terminal orqali

Bu usul faylni uy papkangiz ichidagi `tilimlo-download` papkasiga saqlaydi. Buyruqlarni tartib bilan bajaring:

```bash
sudo apt update
sudo apt install wget
mkdir -p "$HOME/tilimlo-download"
cd "$HOME/tilimlo-download"
wget -O 'tilimlo-keyboard_1.0.0~preview3_all.deb' 'https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard_1.0.0%7Epreview3_all.deb'
```

Yuklash xatosiz tugashi kerak. Keyingi buyruqlarni shu terminalda bajaring.

## 3. O‘rnatish

### Kali’da preview2 o‘rnatilmagan bo‘lsa

`cannot create ... register-layout.dpkg-new ... No such file or directory` xatosi preview2 paketida papka yozuvlari yetishmaganidan kelib chiqqan. Bu preview3’da tuzatildi. Preview2’ni qayta ishlatmang: yangi `.deb`ni yuklab, quyidagi odatiy o‘rnatish buyrug‘ini bajaring. Papkalarni qo‘lda yaratish shart emas.

`_apt ... Permission denied` ogohlantirishi boshqa masala: APT foydalanuvchining uy papkasidagi faylni cheklangan `_apt` hisobi bilan o‘qiy olmaganini bildiradi. Bu yuqoridagi dpkg xatosining sababi emas. Uy papkangiz huquqlarini o‘zgartirish kerak emas.


### Avvalgi nomdagi paket o‘rnatilgan bo‘lsa

Agar oldingi sinov paketini `tilmoch-keyboard` nomi bilan o‘rnatgan bo‘lsangiz, avval boshqa klaviaturaga o‘ting, eski tartibni Input Sources’dan olib tashlang va `sudo apt remove tilmoch-keyboard`ni bajaring. So‘ng quyidagi yangi Tilimlo paketini o‘rnating. Yangi paket nomi `tilimlo-keyboard`, klaviatura identifikatori `tilimlo`.


Paket joylashgan papkada quyidagini bajaring:

```bash
sudo apt install ./tilimlo-keyboard_1.0.0~preview3_all.deb
```

`./` belgilarini qoldiring: ular APT’ga fayl joriy papkada ekanini bildiradi. Tasdiqlash so‘ralsa, ekrandagi ko‘rsatmaga amal qiling. Paket `xkb-data` va `python3`ga bog‘liq; yetishmasa, APT ularni ham o‘rnatishni taklif qiladi.

O‘rnatilganini tekshiring:

```bash
dpkg-query -W -f='${Status}\n${Version}\n' tilimlo-keyboard
```

Kutiladigan natija:

```text
install ok installed
1.0.0~preview3
```

**Ochiq hujjatlarni saqlang, seansdan chiqing — Log Out — va qayta kiring.** Odatda butun kompyuterni qayta yoqish shart emas. Klaviaturani tanlash uchun keyingi bosqich ham zarur: o‘rnatish uni avtomatik faol qilmaydi.

## 4. Klaviaturani yoqish

Ish stolingizga mos yo‘lni tanlang. Menyu nomlari tizim versiyasi va tiliga qarab farq qilishi mumkin. Qaysi ish stoli ishlayotganini bilmasangiz:

```bash
echo "$XDG_CURRENT_DESKTOP"
```

**Mavjud English/US yoki boshqa klaviaturangizni saqlang.** Tilimlo’ni qo‘shimcha tartib sifatida qo‘shing, shunda ular orasida almashishingiz mumkin.

### GNOME / Ubuntu’ning odatiy ish stoli

1. **Settings → Keyboard → Input Sources**ni oching. Ba’zi versiyalarda bu **Region & Language → Input Sources** ichida bo‘ladi.
2. **+ / Add Input Source**ni bosing.
3. `Uzbek` yoki `Tilimlo` deb qidiring. Kerak bo‘lsa **Other** yoki uch nuqtali qo‘shimcha ro‘yxatni oching.
4. **Uzbek (Tilimlo, new Latin)**ni tanlab, **Add**ni bosing.
5. Yuqori paneldagi til/klaviatura belgisidan Tilimlo’ni tanlang. GNOME’da odatda **Super + Space** keyingi tartibga o‘tadi; Super — Windows logotipli tugma.

Ro‘yxatda ko‘rinmasa, [7-bo‘limdagi GNOME muqobil usulidan](#gnomeda-royxatga-qoshishning-muqobil-usuli) foydalaning.

### KDE Plasma

1. **System Settings**ni oching va `Keyboard` deb qidiring.
2. **Keyboard → Layouts**ga o‘ting. Eski versiyalarda **Input Devices → Keyboard → Layouts** bo‘lishi mumkin.
3. **Configure layouts**ni yoqing, **Add**ni bosing.
4. **Uzbek (Tilimlo, new Latin)**ni topib qo‘shing va **Apply**ni bosing.
5. Paneldagi klaviatura indikatoridan Tilimlo’ni tanlang. Almashish tugmasini shu sozlamalarning o‘zida tanlashingiz mumkin.

### Xfce

1. **Settings → Keyboard → Layout**ni oching.
2. Qo‘lda tartib qo‘shish uchun zarur bo‘lsa **Use system defaults** belgisini olib tashlang.
3. **Add** orqali **Uzbek (Tilimlo, new Latin)**ni qo‘shing.
4. **Change layout option** yoki almashish sozlamasidan qulay tugmalarni tanlang.
5. Tanlangan tugmalar yoki paneldagi klaviatura indikatoridan Tilimlo’ga o‘ting.

### Linux Mint Cinnamon

**System Settings → Keyboard → Layouts**ni oching. **+** orqali `Uzbek` yoki `Tilimlo`ni qidiring va yangi tartibni qo‘shing. Paneldagi klaviatura indikatoridan uni tanlang. Bu yo‘l Cinnamon versiyasiga qarab farq qilishi mumkin va hali amalda tekshirilmagan.

## 5. Harflarni yozish va sinash

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

## 6. Qo‘shimcha belgilar

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

## 7. Muammolarni hal qilish

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

1. O‘rnatish holatini 3-bo‘limdagi `dpkg-query` bilan tekshiring.
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

Bu usul **faqat GNOME** uchun va uni oddiy foydalanuvchi terminalida, **sudo’siz** bajarish kerak. U mavjud klaviaturalar ro‘yxatini saqlab, Tilimlo’ni qo‘shadi. Butun blokni birga ko‘chirib bajaring:

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

## 8. Yangilash va olib tashlash

### Yangilash

Yangi `.deb` versiyasi chiqqanda uni yuklab oling va o‘sha fayl uchun `sudo apt install ./FAYL_NOMI.deb`ni bajaring. `FAYL_NOMI.deb` o‘rniga haqiqiy fayl nomini yozing. Bu loyiha hozircha APT repozitoriysi emas: oddiy `apt upgrade` yangi Tilimlo versiyasini GitHub’dan avtomatik yuklamaydi.

### Olib tashlash

1. Faol klaviaturani English/US yoki boshqa ishlaydigan tartibga almashtiring.
2. **Input Sources / Layouts**dan Tilimlo’ni olib tashlang.
3. Terminalda bajaring:

```bash
sudo apt remove tilimlo-keyboard
```

4. Seansdan chiqib qayta kiring.

Paket boshqa foydalanuvchilarning shaxsiy klaviatura ro‘yxatini avtomatik tahrirlamaydi. Kompyuterda bir nechta hisob bo‘lsa, har bir hisobda Tilimlo yozuvini sozlamalardan olib tashlash kerak bo‘lishi mumkin.

## 9. Manba kodidan paket yig‘ish

Bu bo‘lim dasturchilar uchun; oddiy foydalanishda shart emas.

1. [Manba arxivini yuklab oling](https://github.com/SolijonSolayev/tilimlo-keyboard-linux/raw/refs/heads/main/downloads/tilimlo-keyboard-1.0.0-preview3-source.tar.gz).
2. Arxiv joylashgan papkada quyidagilarni bajaring:

```bash
tar -xzf tilimlo-keyboard-1.0.0-preview3-source.tar.gz
cd tilimlo-keyboard-1.0.0-preview3
python3 build-package.py
```

Natija: `dist/tilimlo-keyboard_1.0.0~preview3_all.deb`. Yig‘ish uchun Python 3.9 yoki yangirog‘i kerak; qo‘shimcha Python kutubxonasi talab qilinmaydi. Yig‘ish buyrug‘iga `sudo` kerak emas.

Repozitoriydagi `src/` papkasidan ham `python3 build-package.py` bilan yig‘ish mumkin. Hosil bo‘ladigan paket va manba arxivi `src/dist/` ichiga yoziladi; asl manba fayllari o‘zgarmaydi. `dist/`, `__pycache__/` va Python kesh fayllari Git’ga kiritilmaydi. Ushbu preview’da skript paket versiyasini o‘zidan oladi; buyrug‘ini bajarish versiyani avtomatik oshirmaydi.

### Fayllar va texnik ma’lumot

| Joylashuv | Nima bor? |
|---|---|
| [`downloads/`](downloads/) | Tayyor `.deb`, manba arxivi va nazorat summalari |
| [`downloads/VALIDATION.txt`](downloads/VALIDATION.txt) | Bajarilgan tekshiruvlar va hali tekshirilmagan jihatlar |
| [`src/tilimlo`](src/tilimlo) | Linux XKB tugmalar tartibi |
| [`src/keymap.json`](src/keymap.json) | Oddiy, Shift va AltGr qatlamlarining aniq xaritasi |
| [`src/windows-layout.json`](src/windows-layout.json) | Windows jadvalidan olingan tugmalar ma’lumoti |
| [`src/register-layout.py`](src/register-layout.py) | Klaviaturani tizim registrlariga qo‘shish kodi |
| [`src/build-package.py`](src/build-package.py) | `.deb` paket yig‘ish skripti |

Layout identifikatori: **`tilimlo`**; standart variant: **`basic`**. Paket `/usr/share/X11/xkb/symbols/tilimlo` faylini o‘rnatadi. Eski desktop’lar bilan ishlash uchun `evdev/base` XML va LST ro‘yxatlariga Tilimlo yozuvini qo‘shadi; olib tashlashda shu yozuv o‘chiriladi. `xkb-data` yangilanishidan keyin ro‘yxatni qayta qo‘shish uchun dpkg trigger qo‘shilgan va Debian 12/13 konteynerlarida tekshirilgan.

Paket hozircha imzolanmagan va rasmiy Debian/Ubuntu repozitoriysiga kiritilmagan.

### Qo‘shimcha rasmiy qo‘llanmalar

- [GNOME: boshqa klaviatura tartiblarini qo‘shish](https://help.gnome.org/gnome-help/keyboard-layouts.html)
- [KDE: klaviatura tartiblari](https://docs.kde.org/stable_kf6/en/plasma-desktop/kcontrol/keyboard/layouts.html)
- [Debian: klaviatura sozlamalari](https://wiki.debian.org/Keyboard)
- [libxkbcommon: maxsus klaviatura konfiguratsiyasi](https://xkbcommon.org/doc/current/custom-configuration.html)
