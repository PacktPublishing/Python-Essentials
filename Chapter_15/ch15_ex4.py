#!/usr/bin/env python3
'''Python Essentials

Chapter 15, Example Set 4
'''

from flask import Flask, make_response, render_template, request
import urllib.parse
from jinja2 import Template
from PIL import Image, ImageDraw, ImageColor
import tempfile

spiral_app = Flask(__name__)

@spiral_app.route('/', methods=('GET',) )
def index_get():
    return render_template('index.html')

@spiral_app.route('/', methods=('POST',) )
def index_post():
    spiral_app.logger.debug( 'Input = {0!r}'.format(request.form) )
    errors = {}
    try:
        angle = float(request.form.get('angle'))
    except Exception as ex:
        errors['angle_error']= "Angle {0!r} isn't valid".format(request.form['angle'])
        angle= None
    try:
        incr = float(request.form.get('incr'))
    except Exception as ex:
        errors['incr_error']= "Increment {0!r} isn't valid".format(request.form['incr'])
        incr= None
    try:
        size = float(request.form.get('size'))
    except Exception as ex:
        errors['size_error']= "Size {0!r} isn't valid".format(request.form['size'])
        size= None
    if errors:
        spiral_app.logger.error( errors )
        return render_template('index.html', angle=angle, incr=incr, size=size, **errors )
    spiral_app.logger.info( 'Input incr={incr!r}, size={size!r}, angle={angle!r}'.format(
        incr=incr, angle=angle, size=size) )
    fields_q = urllib.parse.urlencode({'angle':angle, 'incr':incr/100, 'size':size})
    spiral_app.logger.debug( 'path = {0!r}'.format(fields_q) )
    image_path = '/image/{fields_q}'.format( fields_q=fields_q )
    return render_template('index.html', image_path=image_path, angle=angle, incr=incr, size=size )

@spiral_app.route('/image/<spec>', methods=('GET',))
def image(spec):
    """Example URL:

    http://127.0.0.1:5000/image/size=10&angle=65.0&incr=1.05
    """
    spec_uq= urllib.parse.unquote_plus(spec)
    spec_dict = urllib.parse.parse_qs(spec_uq)
    spiral_app.logger.info( 'image spec {0!r}'.format(spec_dict) )
    try:
        angle= float(spec_dict['angle'][0])
        incr= float(spec_dict['incr'][0])
        size= int(spec_dict['size'][0])
    except Exception as e:
        return make_response('URL "{0}" is invalid'.format(spec), 403)

    # Working dir should be under Apache Home
    _, temp_name = tempfile.mkstemp('.png')

    im = Image.new('RGB', (400, 300), color=ImageColor.getrgb('white'))
    pen= Pen(im)
    spiral(pen, angle=angle, incr=incr, size=size)
    im.save(temp_name, format='png')

    # Should redirect so that Apache serves the image.
    spiral_app.logger.debug( 'image file {0!r}'.format(temp_name) )
    with open(temp_name, 'rb' ) as image_file:
        data = image_file.read()
    return (data, 200, {'Content-Type':'image/png'})

# Replacement for turtle using Pillow
from math import radians, sin, cos

class Screen:
    def __init__(self, image):
        self.image= image
    def screensize(self):
        return self.image.size

class Pen:
    def __init__(self, image):
        self.screen= Screen(image)
        self.draw= ImageDraw.Draw( image )
        w, h = image.size
        self.x =  w//2
        self.y =  h//2
        self.angle = 0.0
        self.color= ImageColor.getrgb('black')
    def pos(self):
        return self.x, self.y
    def getscreen(self):
        return self.screen
    def speed(self,*args):
        pass
    def right(self,degrees):
        self.angle += radians(degrees)
    def left(self,degrees):
        self.angle -= radians(degrees)
    def forward(self,distance):
        dx = distance*cos(self.angle)
        dy = distance*sin(self.angle)
        self.draw.line( [(self.x,self.y), (self.x+dx, self.y+dy)], fill=self.color )
        self.x += dx
        self.y += dy

def on_screen(pen):
    x, y = pen.pos()
    w, h = pen.getscreen().screensize()
    return -w <= x < w and -h <= y < h

def spiral(pen, angle, incr, size=10):
    pen.speed(10)
    count= 100
    while on_screen(pen) and count and size > 1:
        pen.right(angle)
        pen.forward(size)
        size *= incr
        count -= 1

if __name__ == '__main__':
    spiral_app.run(debug=True)
