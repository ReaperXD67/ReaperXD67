"""Original README system films. SVG geometry + embedded real local captures.

No browser, remote image, script, foreignObject, or runtime font dependencies.
Pillow mechanically resizes captures; fontTools outlines the existing OFL font.
Run from this repository after installing requirements-showcases.txt.
"""
from pathlib import Path
from io import BytesIO
from base64 import b64encode
from hashlib import sha256
from html import escape
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'output/python-deps'))
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen

ASSETS = ROOT / 'assets'
FONT = instantiateVariableFont(TTFont(ASSETS/'fonts/SpaceGrotesk.ttf'), {'wght': 600}, inplace=False)
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
EM = FONT['head'].unitsPerEm
FG, MUTED, BG = '#f5f5ed', '#b9c3bb', '#0a0e0d'
ORANGE, BLUE, GREEN, ACID = '#ff9f69', '#2949ff', '#79f29c', '#d8ff4f'
PROVENANCE = []

def text(x,y,value,size=24,color=FG,align='start',weight=600):
    # Outlined Space Grotesk gives consistent editorial type inside SVG-as-image.
    scale=size/EM; run=[]; advance=0
    for char in value:
        name=CMAP.get(ord(char),CMAP[ord('?')]); glyph=GLYPHS[name]
        pen=SVGPathPen(GLYPHS); glyph.draw(pen)
        run.append((advance,pen.getCommands())); advance+=glyph.width
    shift=advance*scale*(.5 if align=='middle' else 1 if align=='end' else 0)
    return f'<g fill="{color}" aria-label="{escape(value,quote=True)}" transform="translate({x-shift:.2f} {y}) scale({scale:.5f} {-scale:.5f})">'+''.join(f'<path transform="translate({a} 0)" d="{d}"/>' for a,d in run if d)+'</g>'

def line(x1,y1,x2,y2,color='#3c4741',width=2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'

def rect(x,y,w,h,color,stroke='none',radius=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color}" stroke="{stroke}"/>'

def pulse(path,color,dur=8,begin=0,r=6):
    return f'<circle data-motion="packet" r="{r}" fill="{color}"><animateMotion path="{path}" dur="{dur}s" begin="-{begin}s" repeatCount="indefinite"/></circle>'

def emphasis(x,y,w,h,color,phase=0):
    # Large mechanism emphasis, shared 12-second choreography; labels never fade.
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" opacity=".06" stroke="{color}" stroke-width="3"><animate attributeName="opacity" values=".06;.36;.36;.06;.06" keyTimes="0;.06;.22;.28;1" dur="12s" begin="-{phase}s" repeatCount="indefinite"/></rect>'

def flow(path,color='#d8ff4f',dur=8):
    return f'<path d="{path}" fill="none" stroke="{color}" stroke-width="3" stroke-dasharray="8 18"><animate attributeName="stroke-dashoffset" values="0;-104" dur="{dur}s" repeatCount="indefinite"/></path>'

def title_status(title,status,w,accent):
    return text(38,70,title,54)+text(w-38,66,status,22,accent,'end')

def capture(name,max_width=1100):
    source=ASSETS/'captures'/name
    raw=source.read_bytes(); img=Image.open(BytesIO(raw)).convert('RGB')
    img.thumbnail((max_width,1000),Image.Resampling.LANCZOS)
    out=BytesIO(); img.save(out,'JPEG',quality=88,optimize=True,subsampling=0)
    data=out.getvalue()
    if not any(p['source']==f'public/assets/{name}' for p in PROVENANCE):
        PROVENANCE.append({'source':f'public/assets/{name}','committed_input':f'assets/captures/{name}','source_sha256':sha256(raw).hexdigest(),'source_dimensions':list(Image.open(BytesIO(raw)).size),'embedded_encoding':'JPEG quality 88, 4:4:4, resized only','embedded_sha256':sha256(data).hexdigest(),'embedded_dimensions':list(img.size),'interpretation':'Existing real product capture; not a live session or current production telemetry.'})
    return 'data:image/jpeg;base64,'+b64encode(data).decode()

ATLAS=capture('atlaslm-landing.png')
KARIX=capture('karixmc-live.png')

def image(uri,x,y,w,h,sweep=False):
    body=f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid meet" href="{uri}"/>'
    if sweep:
        # A visibly framed optical pass over a complete, unchanged capture.
        ident=f'capture-{x}-{y}'
        body=f'<defs><clipPath id="{ident}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs><g clip-path="url(#{ident})">'+body+f'<rect data-motion="sweep" x="{x-100}" y="{y}" width="80" height="{h}" fill="#d8ff4f" opacity=".10"><animate attributeName="x" values="{x-100};{x+w+100};{x+w+100}" keyTimes="0;.62;1" dur="12s" repeatCount="indefinite"/></rect></g>'
    return body

def document(w,h,title,desc,body,bg=BG):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>'+rect(0,0,w,h,bg)+body+'</svg>'

def agent(mobile=False):
    w,h=(600,1060) if mobile else (1280,660)
    s=''
    if mobile:
        s+=text(32,72,'AUTONOMOUS',54)+text(32,130,'PERSONAL AGENT',54)
        s+=text(32,184,'LOCAL ALPHA / ARCHITECTURE STUDY',24,ORANGE)
        s+=text(32,248,'One owner.',44)+text(32,300,'One inspectable action.',40)
        # Vertical owned-execution spine, with a visibly separate stale lane.
        for n,(y,label,note) in enumerate([(400,'TASK + OUTBOX','one transaction'),(590,'OWNED LEASE','heartbeat + token'),(840,'DURABLE RECEIPT','recorded side effect')]):
            s+=rect(48,y,365,100,'#171813','#624735')
            s+=emphasis(48,y,365,100,ORANGE,[0,8,4][n])
            s+=text(70,y+41,label,30)+text(70,y+78,note,25,MUTED)
        path='M230 500V590M230 690V840'; s+=flow(path,ORANGE,8)
        s+=pulse('M230 500V590',ORANGE,8)+pulse('M230 690V840',ORANGE,8,4)
        s+=line(455,600,455,780,'#b95c43',3)+emphasis(404,740,104,70,ORANGE,4)+line(405,780,505,780,ORANGE,5)
        s+=text(455,555,'STALE',27,ORANGE,'middle')+text(455,815,'STOP',27,ORANGE,'middle')
        s+=pulse('M455 600V770',ORANGE,8,3)
        s+=text(32,1005,'Stale completion is rejected.',29,ORANGE)
    else:
        s+=text(42,90,'AUTONOMOUS',60)+text(42,154,'PERSONAL AGENT',60)
        s+=text(42,208,'LOCAL ALPHA / ARCHITECTURE STUDY',23,ORANGE)
        s+=text(42,310,'One owner.',47)+text(42,366,'One action.',47)+text(42,422,'One audit trail.',47)
        s+=text(42,572,'Stale completion',31,ORANGE)+text(42,612,'meets a hard boundary.',31,ORANGE)
        # A visible timeline rather than simulated terminal logs.
        for n,(x,y,width,label,note) in enumerate([(505,218,200,'TASK + OUTBOX','one transaction'),(778,218,203,'OWNED LEASE','heartbeat + token'),(1050,218,190,'RECEIPT','recorded effect')]):
            s+=rect(x,y,width,105,'#181a15','#62503b')+emphasis(x,y,width,105,ORANGE,[0,8,4][n])+text(x+19,y+42,label,24)+text(x+19,y+79,note,20,MUTED)
        s+=line(705,270,778,270,ORANGE,3)+line(981,270,1050,270,ORANGE,3)
        s+=pulse('M705 270H778',ORANGE,8)+pulse('M981 270H1050',ORANGE,8,4)
        s+=rect(565,420,260,90,'#1c1511','#6b4937')+text(590,455,'OLD WORKER',26,ORANGE)+text(590,488,'ownership token mismatch',19,MUTED)
        s+=flow('M825 464H1006',ORANGE,8)+pulse('M825 464H1006',ORANGE,8,1)
        s+=emphasis(1001,411,239,107,ORANGE,4)+line(1010,425,1010,505,ORANGE,5)+text(1040,455,'REJECTED',28,ORANGE)+text(1040,490,'no stale write',22,MUTED)
        s+=line(879,323,879,365,'#5d5c48',2)+line(879,365,1010,365,'#5d5c48',2)+line(1010,365,1010,416,'#5d5c48',2)
        s+=text(505,606,'ILLUSTRATIVE SOURCE EXPLANATION / NOT A LIVE RUN',21,MUTED)
    return document(w,h,'Autonomous Personal Agent — owned execution','Original architecture study. Task and outbox share a transaction; owned leases and durable receipts make execution recoverable. A stale worker completion stops at its ownership boundary. Illustrative source explanation, not live telemetry.',s)

def atlas(mobile=False):
    w,h=(600,1140) if mobile else (1280,720)
    s=''
    if mobile:
        s+=text(30,74,'AtlasLM',64,'#121715')+text(570,70,'LIVE',28,BLUE,'end')
        s+=image(ATLAS,25,115,550,348,sweep=True)
        s+=text(30,522,'Evidence before eloquence.',35,'#121715')
        # Recompose vertically; do not shrink the desktop diagram.
        s+=emphasis(50,568,180,142,BLUE,0)+emphasis(370,568,180,142,BLUE,0)
        s+=text(125,606,'DENSE',30,BLUE,'middle')+text(468,606,'BM25',30,BLUE,'middle')
        for i in range(6):
            yy=635+i*15
            a=f'M95 {yy}C95 735 175 770 300 790';b=f'M505 {yy}C505 735 425 770 300 790'
            s+=line(75,yy,125,yy,BLUE,3)+line(475,yy,525,yy,BLUE,3)
            s+=f'<path d="{a}" fill="none" stroke="#a1b0ff" stroke-width="1.5"/><path d="{b}" fill="none" stroke="#a1b0ff" stroke-width="1.5"/>'
            if i%2==0: s+=pulse(a,BLUE,8,i)+pulse(b,BLUE,8,i+2)
        s+=rect(150,770,300,76,BLUE)+emphasis(150,770,300,76,'#ffffff',8)+text(300,818,'RRF + RERANK',30,'#ffffff','middle')
        s+=flow('M300 846V920',BLUE,8)
        s+=rect(95,920,410,99,'#d8ff4f')+emphasis(95,920,410,99,BLUE,4)+text(300,963,'SUFFICIENCY GATE',31,'#121715','middle')+text(300,998,'generate + citation audit',25,'#121715','middle')
        s+=text(30,1090,'Weak evidence can stop the answer.',28,'#303c35')
    else:
        s+=text(40,85,'AtlasLM',76,'#121715')+text(1240,70,'LIVE / DOCUMENT INTELLIGENCE',24,BLUE,'end')
        s+=image(ATLAS,35,135,765,485,sweep=True)
        s+=text(850,168,'Evidence before',39,'#121715')+text(850,214,'eloquence.',39,'#121715')
        s+=emphasis(840,255,160,170,BLUE,0)+emphasis(1045,255,160,170,BLUE,0)
        s+=text(890,290,'DENSE',24,BLUE)+text(1165,290,'BM25',24,BLUE,'end')
        for i in range(7):
            yy=315+i*17
            a=f'M865 {yy}C865 446 935 470 1020 476'; b=f'M1180 {yy}C1180 446 1100 470 1020 476'
            s+=f'<path d="{a}" fill="none" stroke="#94a2f2" stroke-width="1.5"/><path d="{b}" fill="none" stroke="#94a2f2" stroke-width="1.5"/>'
            if i%2==0:s+=pulse(a,BLUE,8,i)+pulse(b,BLUE,8,i+2)
        s+=rect(850,455,350,60,BLUE)+emphasis(850,455,350,60,'#ffffff',8)+text(1025,495,'RRF + RERANK',27,'#ffffff','middle')
        s+=flow('M1025 515V552',BLUE,8)
        s+=rect(850,552,350,58,ACID)+emphasis(850,552,350,58,BLUE,4)+text(1025,590,'SUFFICIENCY GATE',25,'#121715','middle')
        s+=emphasis(835,621,375,46,BLUE,4)+text(1025,650,'GENERATE → CITATION AUDIT',23,BLUE,'middle')
        s+=text(40,681,'REAL LANDING CAPTURE / SOURCE-BASED RETRIEVAL STUDY',22,'#46524b')
    return document(w,h,'AtlasLM — evidence before eloquence','Real AtlasLM landing-page capture, mechanically resized and embedded. An illustrative document stream shows dense and BM25 retrieval converging through reciprocal-rank fusion and reranking. Sufficiency gates generation; citations remain inspectable. Not live telemetry.',s,'#e8e9ff')

def karix(mobile=False):
    w,h=(600,1170) if mobile else (1280,1000)
    s=''
    if mobile:
        s+=text(30,75,'KARIXMC',66)+text(30,123,'MINEPULSE / LIVE ON VPS',28,GREEN)
        s+=image(KARIX,22,165,556,348,sweep=True)
        s+=text(30,572,'Play crosses a',45)+text(30,625,'trust boundary.',45)
        for n,(y,label,note) in enumerate([(700,'PAPER PLUGIN','HMAC + nonce'),(855,'API + LEDGER','server-side rewards'),(1010,'RECEIPT JOURNAL','remember delivery')]):
            s+=rect(45,y,510,93,'#111d16','#3e7750')+emphasis(45,y,510,93,GREEN,[0,8,4][n])+text(70,y+40,label,31,GREEN)+text(70,y+76,note,26,MUTED)
        s+=flow('M300 793V855',GREEN,6)+flow('M300 948V1010',GREEN,6)
        s+=pulse('M300 793V855',GREEN,6)+pulse('M300 948V1010',GREEN,6,3)
        s+=flow('M555 1055H580V744H555',GREEN,12)+pulse('M555 1055H580V744H555',GREEN,12,8,4)
        s+=text(30,1145,'Receipt returns. Delivery is remembered.',26,GREEN)
    else:
        s+=text(40,87,'KARIXMC',76)+text(1240,75,'MINEPULSE / LIVE ON VPS',25,GREEN,'end')
        # Real capture owns the stage; the lower band exposes its boundary.
        s+=image(KARIX,30,120,1220,593,sweep=True)
        s+=text(40,759,'Play crosses a trust boundary.',40)
        labels=[(40,'PAPER PLUGIN','HMAC + nonce'),(455,'API + LEDGER','server-side rewards'),(925,'RECEIPT JOURNAL','remember delivery')]
        for n,(x,label,note) in enumerate(labels):
            s+=emphasis(x-8,786,300,103,GREEN,[0,8,4][n])+text(x,825,label,29,GREEN)+text(x,865,note,24,MUTED)
        s+=flow('M340 822H430',GREEN,6)+flow('M775 822H900',GREEN,6)
        s+=pulse('M340 822H430',GREEN,6)+pulse('M775 822H900',GREEN,6,3)
        s+=flow('M1070 900V925H185V900',GREEN,12)+pulse('M1070 900V925H185V900',GREEN,12,8,5)
        s+=text(600,952,'RECORDED RECEIPT RETURNS',22,GREEN,'middle')
        s+=text(40,985,'REAL SITE CAPTURE / ILLUSTRATIVE SIGNED EVENT + RECORDED RECEIPT',20,MUTED)
    return document(w,h,'MinePulse / KarixMC — game-to-web trust boundary','Real existing KarixMC site capture, mechanically resized and embedded. Signed Paper-plugin events cross to the API and server-side ledger; a plugin-side receipt journal remembers delivered commands. Source-based animated explanation, not live telemetry.',s)

def work_index(mobile=False):
    w,h=(600,890) if mobile else (1280,460)
    s=text(32 if mobile else 42,70,'MORE SYSTEMS. OTHER CONSTRAINTS.',30 if mobile else 41)
    items=[('ROLLFORWARD','Intent survives the network.','#ff9f69'),('REVIVE','Recovery you can explain.','#79f29c'),('ATLASFORGE AI','A pipeline with a spend boundary.','#b9a6ff')]
    for i,(name,summary,color) in enumerate(items):
        y=(150+i*235) if mobile else (135+i*105)
        s+=line(32,y-14,w-32,y-14,'#37443b',1)
        s+=text(32,y+42,name,43 if mobile else 38,color)
        s+=text(32 if mobile else 440,y+(90 if mobile else 40),summary,27 if mobile else 29)
        base=y+(143 if mobile else 75)
        if i==0:
            s+=flow(f'M32 {base}H{w-70}',color,6)+pulse(f'M32 {base}H{w-70}',color,7)
        elif i==1:
            for j in range(6):s+=rect(32+j*(72 if mobile else 180),base-5,45 if mobile else 112,5,color)
            s+=pulse(f'M32 {base-2}H{w-70}',color,9)
        else:
            for j in range(8):s+=line(32+j*(60 if mobile else 150),base-10,32+j*(60 if mobile else 150),base+10,color,2)
            s+=flow(f'M32 {base}H{w-70}',color,11)
    return document(w,h,'More systems: ROLLFORWARD, Revive, AtlasForge AI','Original visual index. ROLLFORWARD preserves optimistic intent across network failure. Revive is an explainable payment-recovery prototype with demo payment outcomes. AtlasForge AI is a bounded-spend video pipeline. Lines are authored motion, not live measurements.',s)

def capability(mobile=False):
    w,h=(600,700) if mobile else (1280,370)
    s=text(32 if mobile else 42,78,'FROM MODEL TO RELIABLE PRODUCT.',31 if mobile else 47)
    cols=[('AI SYSTEMS',['Agents / RAG / evaluation','PyTorch / OpenRouter']),('APPLICATIONS',['Python / TypeScript / Java','FastAPI / Next.js / React']),('DATA + DELIVERY',['Postgres / Redis / Qdrant','Docker / Linux / Vercel'])]
    for i,(name,rows) in enumerate(cols):
        x=32 if mobile else 42+i*415;y=150+i*175 if mobile else 175
        s+=text(x,y,name,30 if mobile else 28,ACID)
        for j,row in enumerate(rows):s+=text(x,y+48+j*41,row,27 if mobile else 25)
    return document(w,h,'Working stack: AI systems, applications, data and delivery','Visible working tools, without skill scores: agents, RAG, evaluation, PyTorch, OpenRouter, Python, TypeScript, Java, FastAPI, Next.js, React, PostgreSQL, Redis, Qdrant, Docker, Linux and Vercel. Full current stack remains in ordinary Markdown.',s)

def still(svg):
    # Every base state is complete; removing SMIL produces a real zero-motion still.
    svg=re.sub(r'<circle\b[^>]*data-motion="packet"[^>]*>.*?</circle>','',svg,flags=re.S)
    svg=re.sub(r'<rect\b[^>]*data-motion="sweep"[^>]*>.*?</rect>','',svg,flags=re.S)
    return re.sub(r'<(?:animateMotion|animateTransform|animate)\b[^>]*(?:/>|>.*?</(?:animateMotion|animateTransform|animate)>)','',svg,flags=re.S)

for name,renderer in [('showcase-agent',agent),('showcase-atlaslm',atlas),('showcase-karixmc',karix),('showcase-build-index',work_index),('showcase-capabilities',capability)]:
    for mobile in (False,True):
        variant=name+('-mobile' if mobile else '')
        svg=renderer(mobile)
        (ASSETS/f'{variant}.svg').write_text(svg,encoding='utf8')
        (ASSETS/f'{variant}-still.svg').write_text(still(svg),encoding='utf8')
(ASSETS/'showcase-provenance.json').write_text(json.dumps({'generated':'2026-10-27','author':'Original A.K. profile compositions','font':'Existing Space Grotesk, SIL OFL notice assets/fonts/SPACE-GROTESK-LICENSE.txt','captures':PROVENANCE,'motion':'Source explanations, not current runtime traces or measured outcomes.','requirements':{'Pillow':'13.0.0','fonttools':'4.60.1'}},indent=2)+'\n',encoding='utf8')
print('Rendered five authored showcases, desktop/mobile and zero-motion variants; real captures embedded with digests.')
