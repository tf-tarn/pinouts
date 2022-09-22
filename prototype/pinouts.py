#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 07.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
from svgwrite import mm



# A4 is 210 × 297
# allow 20mm margin
# 180 x 277
# ASPECT RATIO = 1.5 (132x197 for 16 pins)
# pin length = 11/66 * width (22 pixels)
# pitch = same as length
ASPECT = 1.5
def ic(n_pins):
    dwg = svgwrite.Drawing(filename='test.svg', debug=True)

    w = 20
    h = ASPECT * w

    x = 10
    y = 10

    pin_pitch = 11.0 * w / 66.0

    dwg.add(dwg.rect(insert=(x*mm, y*mm), size=(w*mm, h*mm), fill='white', stroke='black', stroke_width=3))
    for i in range(0, 8):
        py = y + (i + 1) * pin_pitch
        dwg.add(dwg.line(start=((x - pin_pitch) * mm, py * mm), end=(x * mm, py * mm), stroke='black', stroke_width=3))
        dwg.add(dwg.line(start=((w + x + pin_pitch) * mm, py * mm), end=((w + x) * mm, py * mm), stroke='black', stroke_width=3))

    dwg.save()

# dwg = svgwrite.Drawing('test.svg', profile='tiny')
# dwg.add(dwg.line((0, 0), (10, 9), stroke=svgwrite.rgb(10, 10, 16, '%')))
# dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))


def basic_shapes(name):
    dwg = svgwrite.Drawing(filename='test.svg', debug=True)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(20):
        hlines.add(dwg.line(start=(2*cm, (2+y)*cm), end=(18*cm, (2+y)*cm)))
    vlines = dwg.add(dwg.g(id='vline', stroke='blue'))
    for x in range(17):
        vlines.add(dwg.line(start=((2+x)*cm, 2*cm), end=((2+x)*cm, 21*cm)))
    shapes = dwg.add(dwg.g(id='shapes', fill='red'))

    # set presentation attributes at object creation as SVG-Attributes
    circle = dwg.circle(center=(15*cm, 8*cm), r='2.5cm', stroke='blue', stroke_width=3)
    circle['class'] = 'class1 class2'
    shapes.add(circle)

    # override the 'fill' attribute of the parent group 'shapes'
    shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(45*mm, 45*mm),
                        fill='blue', stroke='red', stroke_width=3))

    # or set presentation attributes by helper functions of the Presentation-Mixin
    ellipse = shapes.add(dwg.ellipse(center=(10*cm, 15*cm), r=('5cm', '10mm')))
    ellipse.fill('green', opacity=0.5).stroke('black', width=5).dasharray([20, 20])
    dwg.save()


if __name__ == '__main__':
    ic(16)
