"""Render the profile's original looping Decision Loom and unchanged portrait.

Mechanical portrait placement + procedural geometry, with full-RGB APNG motion
and explicit static desktop/mobile variants. Requires Pillow only.
"""
from argparse import ArgumentParser
from math import sin, cos, pi
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
BG = '#080b0a'
FG = '#f5f5ed'
ACID = '#d8ff4f'

def font(size, weight=500):
    result = ImageFont.truetype(ASSETS / 'fonts' / 'SpaceGrotesk.ttf', size)
    result.set_variation_by_axes([weight])
    return result

def label(draw, xy, text, size=14, fill='#9eaaa0', weight=400):
    draw.text(xy, text, font=font(size, weight), fill=fill)

def artifact(draw, box, phase):
    cx, cy, scale = box
    segments = []
    points = []
    ribbons, steps = 22, 78
    for strand in range(ribbons):
        row = []
        for step in range(steps + 1):
            u = step / steps
            angle = strand / ribbons * 2*pi + u*2*pi*1.4 + phase*2*pi
            radius = 58 + 92*sin(pi*u)**2
            x, y, z = (u-.5)*530, sin(angle)*radius, cos(angle)*radius
            # Perspective camera, with the direction and ends always readable.
            rx = x*.96 + z*.28
            rz = z*.96 - x*.28
            ry = y*.91 + rz*.18
            depth = 820/(820-rz)
            row.append((cx+rx*depth*scale, cy+ry*depth*scale, rz, u))
        points.append(row)
    for strand,row in enumerate(points):
        for step in range(steps):
            a,b = row[step],row[step+1]
            z = (a[2]+b[2])/2
            intensity = max(.12,min(1,(z+160)/300))
            beam = abs(a[3]-phase) < .045
            if beam:
                color = (216,255,79)
            elif strand%6 == 0:
                color = tuple(int(v*intensity) for v in (247,248,229))
            else:
                color = tuple(int(v*intensity) for v in (255,93,49))
            segments.append((z, a, b, color, 2 if beam or strand%6==0 else 1))
        for step in range(0,steps+1,7):
            a=row[step]; b=points[(strand+1)%ribbons][step]
            z=(a[2]+b[2])/2
            intensity=max(.1,min(.55,(z+160)/420))
            color=tuple(int(v*intensity) for v in (245,245,220))
            segments.append((z,a,b,color,1))
    for _,a,b,color,width in sorted(segments,key=lambda item:item[0]):
        draw.line((a[0],a[1],b[0],b[1]),fill=color,width=width)
    # Signal gates share the same authored geometry and direction.
    for end in [-1,1]:
        x=cx+end*282*scale
        y=cy+end*14*scale
        draw.line((x,y-95*scale,x,y+95*scale),fill='#587040',width=1)
        draw.rectangle((x-4,y-4,x+4,y+4),fill=ACID)

def composition(portrait,mobile=False,phase=0):
    width,height=(700,1030) if mobile else (1280,650)
    image=Image.new('RGB',(width,height),BG)
    draw=ImageDraw.Draw(image)
    draw.rectangle((0,0,width-1,height-1),outline='#303b31')
    label(draw,(30,22),'A.K. / REAPERXD67',16,ACID,500)
    label(draw,(width-208,22),'SIGNAL ENGINE / 01',13)
    if mobile:
        label(draw,(30,64),'AMAN KUMAR',66,FG,600)
        label(draw,(33,151),'AI ENGINEER &',25,FG)
        label(draw,(33,185),'FULL-STACK DEVELOPER',25,FG)
        artifact(draw,(350,417,.99),phase)
        label(draw,(35,613),'OBSERVE  /  REASON  /  EXECUTE',16,ACID)
        photo=portrait.resize((240,240),Image.Resampling.LANCZOS)
        image.paste(photo,(32,679))
        draw.rectangle((31,678,272,919),outline='#546149')
        label(draw,(299,704),'Accountable',31,FG,500)
        label(draw,(299,745),'intelligence.',31,FG,500)
        label(draw,(300,815),'BUILDING AT SIP',15,ACID)
        label(draw,(300,846),'FORMER micro1 INTERN',14)
        label(draw,(33,970),'BENGALURU, INDIA  /  AVAILABLE FOR AMBITIOUS BUILDS',13)
    else:
        label(draw,(44,67),'AMAN',106,FG,600)
        label(draw,(44,174),'KUMAR',106,FG,600)
        label(draw,(49,305),'AI ENGINEER & FULL-STACK DEVELOPER',22,ACID,500)
        photo=portrait.resize((213,213),Image.Resampling.LANCZOS)
        image.paste(photo,(48,374))
        draw.rectangle((47,373,261,587),outline='#546149')
        label(draw,(285,390),'Accountable',36,FG,500)
        label(draw,(285,436),'intelligence.',36,FG,500)
        label(draw,(287,512),'BUILDING AT SIP',15,ACID)
        label(draw,(287,542),'FORMER AI ENGINEER INTERN / micro1',13)
        draw.line((615,64,615,585),fill='#233024')
        artifact(draw,(944,304,.98),phase)
        label(draw,(684,565),'OBSERVE  /  REASON  /  EXECUTE',17,ACID)
        label(draw,(49,615),'BENGALURU, INDIA  /  AVAILABLE FOR AMBITIOUS BUILDS',13)
        label(draw,(921,615),'ORIGINAL PROCEDURAL ART',12)
    return image

def render(portrait,mobile=False):
    name='identity-signal-mobile' if mobile else 'identity-signal'
    still=composition(portrait,mobile,.34)
    still.save(ASSETS/f'{name}-still.png',optimize=True)
    frames=[composition(portrait,mobile,i/52) for i in range(52)]
    still.save(ASSETS/f'{name}.png',save_all=True,append_images=frames,default_image=True,duration=90,loop=0,disposal=0,blend=0,optimize=True)
    print(f'{name}: {(ASSETS/f"{name}.png").stat().st_size:,} bytes / 4680ms loop / RGB portrait')

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--portrait',required=True,type=Path)
    args=parser.parse_args()
    photo=Image.open(args.portrait).convert('RGB')
    if photo.width != photo.height: raise ValueError('Use the supplied square portrait without reframing.')
    render(photo)
    render(photo,True)
