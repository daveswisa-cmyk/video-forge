#!/usr/bin/env python3
"""Video Forge thumbnail: jobs/<job>/thumb.html -> out/<job>-thumb.jpg (1280x720).
Renders thumb.html at 1920x1080 in Playwright with the logo inlined the same way
render.py does, then downscales with PIL. Run: python3 render/thumb.py <job>"""
import sys, os, json, base64, urllib.request, io
import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

job=sys.argv[1]; root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jd=os.path.join(root,'jobs',job); out=os.path.join(root,'out'); os.makedirs(out,exist_ok=True)
work=os.path.join(root,'work',job); os.makedirs(work,exist_ok=True)
cfg=json.load(open(os.path.join(jd,'script.json')))

def logo_png():
    last=None
    for u in cfg.get('logo_urls',[cfg.get('logo_url')]):
        if not u: continue
        try:
            data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
            im=Image.open(io.BytesIO(data)).convert('RGBA')
            px=np.array(im).astype(int)
            if px[...,3].min()>250:
                lum=px[...,:3].mean(axis=2); px[...,3]=np.where(lum>235,0,255)
            opaque=px[...,3]>128
            if opaque.any() and px[...,:3][opaque].mean()>128:
                px[...,:3][opaque]=0
            im=Image.fromarray(px.astype('uint8'),'RGBA')
            bbox=im.getbbox(); im=im.crop(bbox) if bbox else im
            buf=io.BytesIO(); im.save(buf,'PNG'); print('logo from',u,im.size,flush=True); return buf.getvalue()
        except Exception as e: last=e; print('logo fail',u,e,flush=True)
    raise last

html=open(os.path.join(jd,'thumb.html')).read()
if 'LOGO_SRC' in html:
    html=html.replace('LOGO_SRC','data:image/png;base64,'+base64.b64encode(logo_png()).decode())
html=html.replace('file:///root/.fonts/','file://'+os.path.expanduser('~/.fonts/'))
built=os.path.join(work,'thumb.built.html'); open(built,'w').write(html)

big=os.path.join(work,'thumb-1920.png')
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto('file://'+built); pg.wait_for_timeout(1200)
    pg.screenshot(path=big, type='png'); b.close()

dst=os.path.join(out,f'{job}-thumb.jpg')
Image.open(big).convert('RGB').resize((1280,720),Image.LANCZOS).save(dst,'JPEG',quality=92,optimize=True)
print('done',dst,os.path.getsize(dst))
