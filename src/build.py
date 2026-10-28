"""בונה את index.html מתוך template.html והתמונות (הכול בקובץ אחד).
הרצה: python3 src/build.py
כדי להוסיף זמר: לשים תמונה בשם bg-<שם>.jpg בתיקיית images ולהוסיף שורה ל-SINGERS ב-template.html.
"""
import base64, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
WEBHOOK = 'https://hook.eu2.make.com/2jsyf7iwjh6c4u9n7lpx1re46y2bbj2e'
def uri(name, mt):
    with open(os.path.join(HERE, 'images', name), 'rb') as f:
        return 'data:%s;base64,%s' % (mt, base64.b64encode(f.read()).decode())
t = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
bgs = sorted(f[:-4] for f in os.listdir(os.path.join(HERE, 'images')) if f.startswith('bg-') and f.endswith('.jpg'))
css = '\n'.join('.%s{background-image:url(%s)}' % (b, uri(b + '.jpg', 'image/jpeg')) for b in bgs)
t = t.replace('__BG_CSS__', css).replace('__IMG_LOGO__', uri('logo-white.png', 'image/png')).replace('__WEBHOOK_URL__', WEBHOOK)
assert not re.findall(r'__[A-Z_]+__', t)
open(os.path.join(HERE, '..', 'index.html'), 'w', encoding='utf-8').write(t)
print('built index.html with', bgs)
