import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
SRC = OUT / 'tilmoch-keyboard-1.0.0-preview1'
SRC.mkdir(parents=True, exist_ok=True)
data = json.loads((ROOT / 'windows-layout.json').read_text(encoding='utf-8'))

# PC/AT set-1 scan codes -> stable XKB physical key names.
scans = {0x29:'TLDE', 0x0c:'AE11',0x0d:'AE12',0x1a:'AD11',0x1b:'AD12',0x2b:'BKSL',0x27:'AC10',0x28:'AC11',0x33:'AB08',0x34:'AB09',0x35:'AB10',0x56:'LSGT',0x39:'SPCE'}
for first, names in [(2,[f'AE{i:02}' for i in range(1,11)]),(0x10,[f'AD{i:02}' for i in range(1,11)]),(0x1e,[f'AC{i:02}' for i in range(1,10)]),(0x2c,[f'AB{i:02}' for i in range(1,8)])]:
    scans.update({first+i:n for i,n in enumerate(names)})
vk_rows = {r['vk']:r for r in data['rows'] if r['vk'] != 255}
vk_scans = {s['scan']:s['vk'] & 255 for s in data['scans']}
dead = {69:'dead_acute',78:'dead_tilde',54:'dead_circumflex'}

def keysym(c, vk):
    if c == 0xf001: return dead[vk]
    if c == 0xf000: return 'NoSymbol'
    if c == 32: return 'space'
    return f'U{c:04X}'

lines = ['// Recovered from Tilmoch Windows 1.0.0 keyboard tables.', 'default partial alphanumeric_keys', 'xkb_symbols "basic" {', '    include "us(basic)"', '    name[Group1] = "Uzbek (Tilmoch, new Latin)";']
mapping=[]
for scan, name in sorted(scans.items()):
    vk=vk_scans[scan]
    row=vk_rows[vk]
    chars=[row['chars'][i] for i in (0,1,3,4)]
    syms=[keysym(c,vk) for c in chars]
    # ALPHABETIC preserves Shift/Caps for primary letters. SEMIALPHABETIC
    # deliberately leaves AltGr brackets and punctuation unaffected by Caps.
    kind='FOUR_LEVEL_SEMIALPHABETIC' if row['attr'] & 1 else 'FOUR_LEVEL'
    if row['attr'] & 1 and chars[2] < 0xf000 and chr(chars[2]).isalpha() and chr(chars[3]).isalpha():
        kind='FOUR_LEVEL_ALPHABETIC'
    lines.append(f'    key <{name}> {{ type[Group1]="{kind}", [ {", ".join(syms)} ] }};')
    mapping.append({'key':name,'scan':scan,'vk':vk,'unicode':chars,'symbols':syms})
lines.extend(['    include "level3(ralt_switch)"','};',''])
symbols='\n'.join(lines)
(SRC/'tilmoch').write_text(symbols,encoding='utf-8',newline='\n')
(SRC/'keymap.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(SRC/'register-layout.py').write_bytes((ROOT/'register-layout.py').read_bytes())

readme='''# Tilmoch Uzbek Keyboard — Debian preview 1

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
\\           ;       :       \\       |
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
'''
(SRC/'README.txt').write_text(readme,encoding='utf-8',newline='\n')
(OUT/'Tilmoch-Debian-README.txt').write_text(readme,encoding='utf-8',newline='\n')

def tar_gz(files):
    buf=io.BytesIO()
    with tarfile.open(fileobj=buf,mode='w',format=tarfile.USTAR_FORMAT) as tar:
        for name, content, mode in files:
            content=content.encode() if isinstance(content,str) else content
            info=tarfile.TarInfo('./'+name);info.size=len(content);info.mode=mode;info.mtime=0
            info.uid=info.gid=0;info.uname=info.gname='root'
            tar.addfile(info,io.BytesIO(content))
    return gzip.compress(buf.getvalue(),mtime=0)

payload=[('usr/share/X11/xkb/symbols/tilmoch',symbols,0o644),('usr/lib/tilmoch-keyboard/register-layout',(SRC/'register-layout.py').read_text(encoding='utf-8'),0o755),('usr/share/doc/tilmoch-keyboard/README',readme,0o644),('usr/share/doc/tilmoch-keyboard/keymap.json',(SRC/'keymap.json').read_text(encoding='utf-8'),0o644)]
control='''Package: tilmoch-keyboard
Version: 1.0.0~preview1
Section: x11
Priority: optional
Architecture: all
Maintainer: Tilmoch Keyboard Packaging <maintainer@example.invalid>
Depends: xkb-data, python3 (>= 3.9)
Description: Tilmoch Uzbek new Latin keyboard layout (preview)
 XKB layout preserving the Tilmoch Windows 1.0.0 physical key positions.
 Includes AltGr symbols and legacy desktop registry integration.
 Runtime validation on Debian desktop systems is still pending.
'''
postinst='''#!/bin/sh
set -eu
case "$1" in
    configure|triggered) /usr/lib/tilmoch-keyboard/register-layout install ;;
esac
exit 0
'''
# postrm must be self-contained: package data has already been removed.
postrm=(SRC/'register-layout.py').read_text(encoding='utf-8').replace('    main()\n',"    if sys.argv[1:] and sys.argv[1] in ('remove', 'purge', 'disappear'):\n        sys.argv = [sys.argv[0], 'remove']\n        main()\n")
triggers=''.join('interest-noawait /usr/share/X11/xkb/rules/'+n+'\n' for n in ('evdev.xml','base.xml','evdev.lst','base.lst'))
md5=''.join(hashlib.md5(c.encode() if isinstance(c,str) else c).hexdigest()+'  '+n+'\n' for n,c,_ in payload)
metadata=[('control',control,0o644),('postinst',postinst,0o755),('postrm',postrm,0o755),('triggers',triggers,0o644),('md5sums',md5,0o644)]

def ar_entry(name,content):
    header=f'{name+"/":<16}{0:<12}{0:<6}{0:<6}{"100644":<8}{len(content):<10}`\n'.encode('ascii')
    assert len(header)==60
    return header+content+(b'\n' if len(content)%2 else b'')

deb=b'!<arch>\n'+b''.join(ar_entry(n,c) for n,c in [('debian-binary',b'2.0\n'),('control.tar.gz',tar_gz(metadata)),('data.tar.gz',tar_gz(payload))])
target=OUT/'tilmoch-keyboard_1.0.0~preview1_all.deb';target.write_bytes(deb)
# Preserve portable build inputs. No Windows binaries are redistributed.
for name in ('build-package.py','windows-layout.json'):
    (SRC/name).write_bytes((ROOT/name).read_bytes())
(OUT/'tilmoch-keyboard-1.0.0-preview1-source.tar.gz').write_bytes(tar_gz([(SRC.name+'/'+p.name,p.read_bytes(),0o644) for p in sorted(SRC.iterdir()) if p.is_file()]))
(OUT/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in (target,OUT/'tilmoch-keyboard-1.0.0-preview1-source.tar.gz')),encoding='ascii')
print(target)
print('Mapped physical keys:',len(mapping))
