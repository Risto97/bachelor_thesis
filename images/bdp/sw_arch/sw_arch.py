from bdp import *

xml_parser_size = (20,2)
python_class_size = (20,1.5)
classifier_size = (8, 1.5)

xml_parser = block(r"Python xmltodict parser", size=xml_parser_size)
python_cascade_model = block(r"Python cascade model", size=python_class_size).align(xml_parser.c(-python_class_size[0]//2, 2))

python_classifier = block(r"Python classifier", size=classifier_size).align(python_cascade_model.c(-.425,python_class_size[1]))
c_header_gen = block(r"C header gen", size=classifier_size).right(python_classifier)
c_classifier = block(r"C classifier", size=classifier_size).below(c_header_gen)

fig << xml_parser << python_cascade_model << python_classifier << c_header_gen  << c_classifier

cap.length = 1
cap.width = 1
path.line_width = 0.5
path.double = True

fig << path(xml_parser.c(0, -1.25), xml_parser.c(0, -0.5), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\footnotesize{XML model}').align(fig[-1].pos(-0.5), prev().w(0.3, +0.5))
fig << path(xml_parser.c(0, 0.5), python_cascade_model.c(0, -0.5), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << path(python_cascade_model.c(0, 0.65), python_classifier.c(0, -0.5), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')

fig << path(python_cascade_model.c(0, 0.65), c_header_gen.c(0, -0.5), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << path(python_classifier.c(0, 0.5), python_classifier.c(0, 2.9), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\footnotesize{Detected coords}').align(fig[-1].pos(+1.5), prev().w(0.3, +0.5))

fig << path(c_header_gen.c(0, 0.5), c_classifier.c(0, -0.5), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << path(c_classifier.c(0, 0.5), c_classifier.c(0, 1.25), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\footnotesize{Detected coords}').align(fig[-1].pos(+1.5), prev().w(0.3, +0.5))

import bdp

bdp.render.render_fig(fig, fout="sw_arch1.png", outdir="." )
