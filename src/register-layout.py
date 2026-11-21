#!/usr/bin/python3
"""Legacy X11/Wayland registry integration, repeated after xkb-data upgrades."""
import os
import re
import stat
import sys
import tempfile
from pathlib import Path
import xml.etree.ElementTree as ET

START = '<!-- tilimlo-keyboard: begin -->'
END = '<!-- tilimlo-keyboard: end -->'
ENTRY = '''<layout>
  <configItem>
    <name>tilimlo</name><shortDescription>uz</shortDescription>
    <description>Uzbek (Tilimlo, new Latin)</description>
    <languageList><iso639Id>uzb</iso639Id></languageList>
  </configItem>
</layout>'''

def xml_content(text, install):
    text = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', text, flags=re.S)
    root = ET.fromstring(text)
    if install:
        if root.find("./layoutList/layout/configItem/[name='tilimlo']") is not None:
            raise RuntimeError('An unrelated tilimlo layout already exists')
        if '</layoutList>' not in text:
            raise RuntimeError('Missing layoutList')
        text = text.replace('</layoutList>', START + '\n' + ENTRY + '\n' + END + '\n</layoutList>', 1)
    ET.fromstring(text)
    return text

def lst_content(text, install):
    text = re.sub(r'^\s+tilimlo\s+Uzbek \(Tilimlo, new Latin\)\r?\n?', '', text, flags=re.M)
    if install:
        if re.search(r'^\s+tilimlo\s', text, flags=re.M):
            raise RuntimeError('An unrelated tilimlo layout already exists')
        text, n = re.subn(r'(^!\s+layout\s*\n)', r'\1  tilimlo         Uzbek (Tilimlo, new Latin)\n', text, count=1, flags=re.M)
        if n != 1:
            raise RuntimeError('Missing layout section')
    return text

def update(path, install):
    # Resolve distro symlinks rather than replacing them.
    path = path.resolve()
    old = path.read_text(encoding='utf-8')
    new = xml_content(old, install) if path.suffix == '.xml' else lst_content(old, install)
    if new == old:
        return
    mode = stat.S_IMODE(path.stat().st_mode)
    fd, temporary = tempfile.mkstemp(prefix='.tilimlo-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='\n') as out:
            out.write(new)
            out.flush()
            os.fsync(out.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def main():
    if sys.argv[1:] not in (['install'], ['remove']):
        raise SystemExit('Usage: register-layout install|remove')
    install = sys.argv[1] == 'install'
    seen = set()
    for name in ('evdev.xml', 'base.xml', 'evdev.lst', 'base.lst'):
        path = Path('/usr/share/X11/xkb/rules') / name
        if path.exists() and path.resolve() not in seen:
            update(path, install)
            seen.add(path.resolve())

if __name__ == '__main__':
    main()
