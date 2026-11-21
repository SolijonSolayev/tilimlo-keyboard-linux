# Tilmoch Uzbek Keyboard — Debian preview 1

Debian oilasi uchun XKB klaviatura tartibi. Paket arxitekturasi: all
(amd64, arm64 va boshqa arxitekturalarda bir xil ma’lumot fayllari).
Maqsad: Debian 12/13, Ubuntu 22.04/24.04 va ularga asoslangan desktop tizimlar.
Bu distributivlarda amaliy sinov hali o‘tkazilmagan. Linux konsoli (TTY) uchun emas.

## O‘rnatish

Yuklangan .deb joylashgan papkada:

    sudo apt install ./tilmoch-keyboard_1.0.0~preview1_all.deb

Seansdan chiqib, qayta kiring. Keyboard / Input Sources sozlamasida
“Uzbek (Tilmoch, new Latin)” ni qo‘shing. Qidiruv: Uzbek yoki Tilmoch.
GNOME’da kerak bo‘lsa “Other” bo‘limini oching.
Avval mavjud klaviaturangizni saqlab, Tilmoch’ni qo‘shimcha tartib sifatida sinang.

GNOME’da ro‘yxatga qo‘shishning muqobil yo‘li (sudo ishlatmang):

    python3 - <<'PY'
    import ast, subprocess
    schema = 'org.gnome.desktop.input-sources'
    text = subprocess.check_output(['gsettings', 'get', schema, 'sources'], text=True)
    sources = ast.literal_eval(text.removeprefix('@a(ss) ').strip())
    if ('xkb', 'tilmoch') not in sources:
        sources.append(('xkb', 'tilmoch'))
        subprocess.run(['gsettings', 'set', schema, 'sources', repr(sources)], check=True)
    PY

X11’da tezkor yoqish (faqat shu seansning faol tartibini o‘zgartiradi):

    setxkbmap -layout tilmoch

Wayland’da setxkbmap o‘rniga desktop’ning Input Sources sozlamasidan foydalaning.
Desktop yangi tartibni ko‘rmasa, avval qayta kirilganini tekshiring.

## Tugmalar (US yozuvlari bo‘yicha)

Tugma       Oddiy   Shift   AltGr   AltGr+Shift
[           ö       Ö       [       {
]           ğ       Ğ       ]       }
;           ş       Ş       …       ∅
'           ç       Ç       '       `
\           ;       :       \       |
`           ’       "       ‘       ~
,           ,       “       <       «
.           .       ”       >       »
-           -       _       –       —
=           =       +       ≠       ±
I           i       I       ı       İ
U           u       U       ü       Ü
2           2       @       ™       €
3           3       #       £       №
8           8       *       •       °

Jadvaldagi ∅ bo‘sh qatlamni anglatadi: aniq xarita keymap.json’da.
AltGr = o‘ng Alt. Caps Lock asosiy harflarga ishlaydi.
AltGr+E, AltGr+N, AltGr+6: acute, tilde, circumflex dead keys.
Ulardan keyingi kompozitsiya Linux ilovasi/input method’iga bog‘liq;
Windows’dagi barcha kompozitsiyalar bilan aynan bir xil ekani kafolatlanmaydi.
Ctrl qisqartmalari Linux/XKB va ilova qoidalariga amal qiladi.
Bu transliterator emas: “sh” avtomatik “ş”ga aylanmaydi.
Internet yoki Tilmoch MCP kerak emas.

## Olib tashlash

Avval boshqa klaviaturaga o‘ting va Input Sources’dan Tilmoch’ni olib tashlang:

    sudo apt remove tilmoch-keyboard

So‘ng seansdan chiqib qayta kiring.

## Texnik ma’lumot

Layout identifikatori: tilmoch; variant: basic.
Paket o‘z symbols/tilmoch faylini o‘rnatadi. Eski X11/Wayland desktop’lar uchun
evdev/base XML va LST registrlariga faqat Tilmoch yozuvini qo‘shadi; o‘chirganda
shu yozuvni olib tashlaydi. xkb-data yangilanganda dpkg trigger uni qayta qo‘shadi.
Paket foydalanuvchining faol klaviaturasini avtomatik almashtirmaydi.

Linux’da paketni o‘rnatgandan keyin kompilyatsiya tekshiruvi:

    sudo apt install libxkbcommon-tools
    xkbcli compile-keymap --layout tilmoch > /tmp/tilmoch.xkb

Manba fayllari va qayta yig‘ish skripti source arxivida.
Paket imzolanmagan, ommaviy repozitoriyga joylanmagan.
