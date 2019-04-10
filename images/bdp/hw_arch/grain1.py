from bdp import *

BDP = block(r"BDP", alignment='nw', group='tight', group_margin=p(1,1.5), dashed=True)
fig << block(r"psadad")
BDP['tikz'] = prev(r"tikzasdas").right()

fig << BDP

import bdp

bdp.render.render_fig(fig, fout="grain1.png", outdir=".")
