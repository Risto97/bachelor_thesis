from pygears import Intf, gear
from pygears.typing import Uint, Array
from pygears.common.serialize import serialize
from pygears.common import shred, dreg

from pygears.cookbook.verif import directed
from pygears.sim import sim
from pygears.sim.modules.drv import drv
from pygears.sim.modules.verilator import SimVerilated

# @gear
# # def wrap(din):
#     print(din.dtype)
#     dout = din | dreg | serialize | dreg

#     return dout

seq = [(4,3,5,6, 9, 1,2, 3)]

serialize(din=drv(t=Array[Uint[4], 8], seq=seq), sim_cls=SimVerilated) | shred
