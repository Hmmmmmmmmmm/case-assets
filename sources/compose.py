"""Rebuild icons: python3 sources/compose.py. Requires Pillow >= 11."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, json

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['info','success','failure','question','urgent','review','reminder','blocked']
FONT = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(n):
    try: return ImageFont.truetype(FONT,n)
    except OSError: return ImageFont.truetype('DejaVuSans-Bold.ttf',n)
base = Image.open(ROOT/'sources/case-3d-base.png').convert('RGBA')
# Identical base transform leaves clear upper and lower right badge zones.
base = base.crop(base.getbbox()).resize((410,410),Image.Resampling.LANCZOS)
colors = {'success':'#24984c','failure':'#dc343d','question':'#dc343d','urgent':'#dc343d','review':'#237bd1','reminder':'#237bd1','blocked':'#c93c32'}
masters=[]
for name in NAMES:
    im=Image.new('RGBA',(512,512)); im.alpha_composite(base,(18,70))
    d=ImageDraw.Draw(im)
    ink='#252525'
    # Small mouths and eyebrows retain original eyes, glasses, body and bow tie.
    if name=='success': d.arc((183,316,255,351),0,180,fill=ink,width=7)
    elif name in ('failure','blocked'): d.arc((183,336,255,365),180,360,fill=ink,width=6)
    elif name in ('urgent','question'): d.ellipse((212,327,229,348),outline=ink,width=5)
    elif name in ('review','reminder'): d.line((208,342,233,342),fill=ink,width=5)
    if name in ('urgent','blocked'):
        d.line((153,174,180,186),fill=ink,width=5); d.line((262,186,288,174),fill=ink,width=5)
    if name=='question': d.line((266,168,292,162),fill=ink,width=5)
    if name!='info':
        # Supersampled cartoon markers: thick dark contour and white sticker edge.
        scale=3
        badge=Image.new('RGBA',(216*scale,216*scale))
        bd=ImageDraw.Draw(badge)
        def pts(seq): return [(int(x*scale),int(y*scale)) for x,y in seq]
        def line(seq,fill,width): bd.line(pts(seq),fill=fill,width=width*scale,joint='curve')
        col=colors[name]
        if name in ('success','failure','reminder'):
            bd.ellipse((8*scale,8*scale,208*scale,208*scale),fill=ink)
            bd.ellipse((16*scale,16*scale,200*scale,200*scale),fill=col)
            if name=='success':
                points=[(49,106),(89,143),(166,65)]
                line(points,ink,26); line(points,'white',15)
            elif name=='failure':
                for points in [[(66,65),(151,151)],[(151,65),(66,151)]]:
                    line(points,ink,26); line(points,'white',15)
            else:
                bd.ellipse((42*scale,42*scale,174*scale,174*scale),outline=ink,width=16*scale)
                bd.ellipse((42*scale,42*scale,174*scale,174*scale),outline='white',width=8*scale)
                line([(108,65),(108,108),(140,129)],ink,20)
                line([(108,65),(108,108),(140,129)],'white',10)
        elif name=='blocked':
            vertices=[(108+101*math.cos(math.radians(22.5+k*45)),108+101*math.sin(math.radians(22.5+k*45))) for k in range(8)]
            bd.polygon(pts(vertices),fill=col,outline=ink,width=8*scale)
            bd.text((108*scale,108*scale),'BLOCKED',font=font(35*scale),anchor='mm',fill='white',stroke_width=1*scale,stroke_fill=ink)
        else:
            bd.text((108*scale,103*scale),'?' if name=='question' else '!',font=font(225*scale),anchor='mm',fill=col,stroke_width=5*scale,stroke_fill=ink)
        # A white contour follows the marker itself; no rectangular background.
        from PIL import ImageFilter
        alpha=badge.getchannel('A')
        border=alpha.filter(ImageFilter.MaxFilter(25))
        sticker=Image.new('RGBA',badge.size,'white'); sticker.putalpha(border)
        sticker.alpha_composite(badge)
        sticker=sticker.resize((216,216),Image.Resampling.LANCZOS)
        im.alpha_composite(sticker,(292,292) if name in ('success','failure','blocked') else (292,0))
    im.save(ROOT/f'logos/case-{name}.png',optimize=True)
    im.resize((256,256),Image.Resampling.LANCZOS).save(ROOT/f'logos/256/case-{name}.png',optimize=True)
    masters.append(im)
sheet=Image.new('RGB',(1024,620),'#f0f2f5'); sd=ImageDraw.Draw(sheet)
for i,(name,im) in enumerate(zip(NAMES,masters)):
    x=(i%4)*256; y=(i//4)*310
    sheet.paste(im.resize((240,240),Image.Resampling.LANCZOS),(x+8,y+5),im.resize((240,240),Image.Resampling.LANCZOS))
    sd.text((x+128,y+264),name,font=font(22),anchor='mm',fill='#222222')
    small=im.resize((64,64),Image.Resampling.LANCZOS)
    sheet.paste(small,(x+184,y+240),small)
sheet.save(ROOT/'previews/case-icon-contact-sheet.png',optimize=True)
results=[]
for p in sorted((ROOT/'logos').rglob('*.png')):
    im=Image.open(p); im.verify(); im=Image.open(p)
    assert im.mode=='RGBA' and im.size in [(512,512),(256,256)]
    assert im.getpixel((0,0))[3]==0
    results.append({'file':str(p.relative_to(ROOT)),'size':im.size,'bytes':p.stat().st_size})
(ROOT/'sources/validation.json').write_text(json.dumps(results,indent=2)+'\n')
