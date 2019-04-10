from bdp import *

size = (6, 4)
cascade_classifier = block(r"Cascade Classifier \\ IP Core", size=size)

fig << cascade_classifier

fig << path(cascade_classifier.c(-0.8, 0), cascade_classifier.c(-0.5, 0), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\tiny img_in').align(fig[-1].pos(+1.5), prev().w(-0.3, +1.0))
fig << path(cascade_classifier.c(+0.5, -0.2), cascade_classifier.c(+1.0, -0.2), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\tiny detect_addr').align(fig[-1].pos(+1.5), prev().w(+1.3, +0.7))
fig << path(cascade_classifier.c(+0.5, +0.2), cascade_classifier.c(+1.0, +0.2), routedef='-|', style=('', cap(width=1, length=0.5)), line_width=0.5, double=True, border_width=0.035, color='black')
fig << text(r'\tiny IRQ').align(fig[-1].pos(+1.5), prev().w(-0.3, +1.5))
import bdp

bdp.render.render_fig(fig, fout="top.png", outdir=".")
