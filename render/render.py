#!/usr/bin/env python3
"""Video Forge renderer: jobs/<job>/{scenes.html,script.json} -> out/<job>.mp4
Voice: Kokoro ONNX (local). Frames: Playwright, one JPEG per frame. Mux: ffmpeg."""
import sys, os, json, base64, subprocess, urllib.request, time
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
from playwright.sync_api import sync_playwright

job=sys.argv[1]; root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jd=os.path.join(root,'jobs',job); out=os.path.join(root,'out'); os.makedirs(out,exist_ok=True)
work=os.path.join(root,'work',job); os.makedirs(os.path.join(work,'frames'),exist_ok=True)
cfg=json.load(open(os.path.join(jd,'script.json')))
FPS=cfg.get('fps',30); sr=24000

# 1. voice
k=Kokoro(os.path.join(root,'models','kokoro-v1.0.onnx'),os.path.join(root,'models','voices-v1.0.bin'))
lens={}; parts=[]
for sc in cfg['scenes']:
    a,r=k.create(sc['text'],voice=cfg.get('voice','bm_george'),speed=cfg.get('speed',1.0),lang=cfg.get('lang','en-us'))
    a=np.concatenate([np.zeros(int(sr*0.4)),a,np.zeros(int(sr*0.6))])
    L=len(a)/sr+sc.get('hold',1.0); lens[sc['id']]=L
    need=int(L*sr); a=np.concatenate([a,np.zeros(max(0,need-len(a)))])[:need]; parts.append(a)
    print('vo',sc['id'],round(L,2),flush=True)
sf.write(os.path.join(work,'vo.wav'),np.concatenate(parts),sr)

# 2. html with logo inlined
html=open(os.path.join(jd,'scenes.html')).read()
def logo_png():
    from PIL import Image
    import io
    last=None
    for u in cfg.get('logo_urls',[cfg.get('logo_url')]):
        if not u: continue
        try:
            data=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
            im=Image.open(io.BytesIO(data)).convert('RGBA')
            px=np.array(im).astype(int)
            # if effectively no transparency, knock out near-white background
            if px[...,3].min()>250:
                lum=px[...,:3].mean(axis=2); px[...,3]=np.where(lum>235,0,255)
            # if the artwork is light (white wordmark), make it black
            opaque=px[...,3]>128
            if opaque.any() and px[...,:3][opaque].mean()>128:
                px[...,:3][opaque]=0
            im=Image.fromarray(px.astype('uint8'),'RGBA')
            bbox=im.getbbox(); im=im.crop(bbox) if bbox else im
            buf=io.BytesIO(); im.save(buf,'PNG'); print('logo from',u,im.size,flush=True); return buf.getvalue()
        except Exception as e: last=e; print('logo fail',u,e,flush=True)
    raise last
if 'LOGO_SRC' in html:
    html=html.replace('LOGO_SRC','data:image/png;base64,'+base64.b64encode(logo_png()).decode())
html=html.replace('file:///root/.fonts/','file://'+os.path.expanduser('~/.fonts/'))
built=os.path.join(work,'scenes.built.html'); open(built,'w').write(html)

# 3. frames
n=0; t0=time.time()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1920,"height":1080})
    pg.goto('file://'+built); pg.wait_for_timeout(800)
    for sc in cfg['scenes']:
        nf=int(round(lens[sc['id']]*FPS))
        for i in range(nf):
            pg.evaluate(f"render('{sc['id']}',{i/FPS})")
            pg.screenshot(path=os.path.join(work,'frames',f'f{n:05d}.jpg'),type='jpeg',quality=92); n+=1
        print('frames',sc['id'],nf,'elapsed',round(time.time()-t0),flush=True)
    b.close()

# 4. mux
mp4=os.path.join(out,f'{job}.mp4')
subprocess.check_call(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',os.path.join(work,'frames','f%05d.jpg'),
  '-i',os.path.join(work,'vo.wav'),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',mp4])
print('done',mp4,os.path.getsize(mp4))
