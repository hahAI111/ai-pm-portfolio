from pathlib import Path
import imageio.v2 as imageio
from PIL import Image, ImageDraw, ImageFont

W,H,FPS=1280,720,24
OUT=Path("ai-pm-portfolio-demo.mp4")

def f(n,b=False):
    try:return ImageFont.truetype("arialbd.ttf" if b else "arial.ttf",n)
    except:return ImageFont.load_default()

def frame(title,subtitle,items,accent="#ffb000"):
    im=Image.new("RGB",(W,H),"#0b1220");d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,110),fill="#111f35")
    d.text((55,25),title,font=f(39,True),fill="white")
    d.text((57,77),subtitle,font=f(19),fill="#aec7e8")
    y=155
    for head,body in items:
        d.rounded_rectangle((65,y,1215,y+105),radius=18,fill="#182b47",outline="#315276",width=2)
        d.text((92,y+18),head,font=f(26,True),fill=accent)
        d.text((92,y+58),body,font=f(21),fill="#e1edff")
        y+=125
    d.text((55,678),"Independent AI Product Portfolio | Synthetic demonstration data",font=f(15),fill="#7793b8")
    return im

scenes=[
("Global Seller Growth","Three working AI Product MVPs",[("1. Opportunity Discovery","Find, size, and prioritize seller-growth opportunities"),("2. Seller Growth Copilot","Diagnose blockers and recommend actions"),("3. Support Automation","Triage tickets with human-in-the-loop safety")]),
("Marketplace Opportunity Discovery","From raw data to roadmap decisions",[("Marketplace GMV","USD 582,200 | synthetic demonstration data"),("Opportunity scoring","Growth momentum + conversion + listing + ads + inventory"),("Product decision","Prioritize the seller segment with highest actionable upside")]),
("AI Seller Growth Copilot","Explain why seller performance changed",[("Growth diagnosis","Conversion issue | 92% confidence"),("Evidence","Traffic stable; conversion rate down 21%"),("Recommended actions","Improve listing copy, test promotion, optimize keywords")]),
("Product Learning Loop","Measure more than model usage",[("Recommendation","Seller receives evidence-backed next steps"),("Action completion","Seller confirms implementation"),("Outcome measurement","Track conversion, ROAS, and sales movement")]),
("AI Seller Support Automation","Safe response generation",[("Ticket classification","Classify request and estimate confidence"),("Grounded guidance","Retrieve approved seller-support content"),("Policy guardrail","Sensitive questions are routed to human review")]),
("AI Safety Guardrail","Human review required",[("Policy-sensitive request","Do not make or publish a change before review"),("Safe response","Draft a holding response using approved guidance"),("Quality metric","Measure escalation recall and human overrides")],"#ff8595"),
("Portfolio Summary","Built for AI Product Management",[("Technology","Python, Streamlit, Azure AI Foundry"),("Product practice","PRD, metrics, experiments, transparent logic"),("Repository","github.com/hahAI111/ai-pm-portfolio")]),
]
frames=[]
for title,sub,items,*color in scenes:
    im=frame(title,sub,items,color[0] if color else "#ffb000")
    frames += [im]*(FPS*9)
imageio.mimsave(OUT,frames,fps=FPS,codec="libx264",quality=8)
print(OUT.resolve())
