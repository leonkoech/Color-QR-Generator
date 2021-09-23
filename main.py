from datetime import time
from flask import *
from PIL import ImageColor
import os
import qrcode
from PIL import Image


app = Flask(__name__)


def backgroundColor(bgcr,bgcg,bgcb,bgtransparent ):
    image=Image.open('unprocessed.png')
    # transform image to RGBA
    image = image.convert('RGBA')
    print(image)
    print(image.mode)
    # print(image.getdata()[2])
    newImage = []
    for item in image.getdata():
        if item[:3] == (255,255,255):
            # enter the new color here
            # choose whether transparent or other ccolors
            if(bgtransparent=="checked"):
                newImage.append((255,255,255,0))
            else:
                newImage.append((bgcr,bgcg,bgcb))
        
        else:
            newImage.append(item)
    image.putdata(newImage)
    image.save('unprocessed.png')

def codeColor(cqrr,cprg, cprb,qrtransparent):
    image=Image.open('unprocessed.png')
    # transform image to RGBA
    image = image.convert('RGBA')
    print(image)
    print(image.mode)
    # print(image.getdata()[2])
    newImage = []
    for item in image.getdata():
        if item[:3] == (0,0,0):
            # enter the new color here
            # choose whether transparent or other colors
            if(qrtransparent=="checked"):
                newImage.append((255,255,255,0))
            else:
                newImage.append((cqrr,cprg, cprb))
        
        else:
            newImage.append(item)
    image.putdata(newImage)
    # directory for static folder
    image.save(os.path.join(app.root_path, 'static', 'processed.png'))
    # delete the unprocessed image
    os.remove('unprocessed.png')

def mainfun(inputtext,bgcr,bgcg,bgcb,bgtransparent, cqrr,cprg, cprb,qrtransparent):
    img = qrcode.make(inputtext)
    type(img)  
    img.save("unprocessed.png")
    # if bgr=255 and bgg==255 and bgb
    backgroundColor(bgcr,bgcg,bgcb,bgtransparent)
    codeColor(cqrr,cprg, cprb,qrtransparent)

def reversetuple(str):
    
    str= str.replace('(','')
    str=str.replace(')','')
    strarr=str.split(',')
    return strarr

@app.route('/')
def main():
    # you need this line to render the template
    return render_template('index.html')

@app.route('/', methods=['POST'])
def main_post():
    text = request.form['text']
    bgcolor = ImageColor.getcolor(request.form['bgcolor'], "RGB")
    qrcolor = ImageColor.getcolor(request.form['qrcolor'], "RGB")
    transparentbg = request.form.get('transparentbg')
    transparentqr =  request.form.get('transparentqr')
    # transparentbg = "checked"
    # transparentqr =  "unchecked"
    # processed_text = text.upper()
    print(transparentbg)
    print(transparentqr)
    if request.method == 'POST':
    # do stuff when the form is submitted

    # redirect to end the POST handling
    # the redirect can be to the same route or somewhere else
       
        return redirect(url_for('fetch',input=text,bgcolor=str(bgcolor),qrcolor=str(qrcolor),transparentbg=str(transparentbg),transparentqr=str(transparentqr)))

    # show the form, it wasn't submitted
    # return render_template('cool_form.html')
    return render_template('main')

    # return render_template('processed.html',input=text,bgcolor=str(bgcolor),qrcolor=str(qrcolor))
    # return redirect(url_for('/processed',input=text,bgcolor=str(bgcolor),qrcolor=str(qrcolor)))

@app.route('/processed')
# @app.route('/processed/<input><bgcolor>')
def fetch(input=None,bgcolor=None,qrcolor=None,transparentbg=None,transparentqr=None):
    # url_for('processed.html',input=input,bgcolor=str(bgcolor),qrcolor=str(qrcolor))
   
    input = request.args.get('input', '')
   
    bgcolor = reversetuple( request.args.get('bgcolor',''))
    qrcolor = reversetuple( request.args.get('qrcolor',''))

    bgtransparent = request.args.get('transparentbg','')
    qrtransparent = request.args.get('transparentqr','')
   
    bgcr = int(bgcolor[0])
    bgcg = int(bgcolor[1])
    bgcb = int(bgcolor[2])
    cqrr = int(qrcolor[0])
    cprg = int(qrcolor[1])
    cprb = int(qrcolor[2])
    # if(bgtransparent=='checked'):
    #     bgt=True
        
    # elif(bgtransparent=='unchecked'):
    #     bgt=False
        
    # if(qrtransparent =='checked'):
    #     qrt = True
        
    # elif(qrtransparent =='unchecked'):
    #     qrt=False
        
    # time.sleep(2)
    mainfun(input,bgcr,bgcg,bgcb,bgtransparent, cqrr,cprg, cprb,qrtransparent)
  
    
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')

    return render_template('processed.html')
