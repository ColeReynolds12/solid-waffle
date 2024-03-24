import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = (8, 8)
plt.rcParams["font.size"] = 14

def ref_traj_linear(t, t_f, r_i, r_f):
    v = (r_f - r_i)/t_f
    if t < t_f:
        return r_i + v*t
    return r_f

class Swarm:

    def __init__(self, node_ammount:int, ref_traj = None) -> None:
        self.node_ammount = node_ammount
        if ref_traj is None:
            self.ref_traj = lambda a,b,c,d: 0
        else:
            self.ref_traj = ref_traj
        self.node_list = []
        self.create_swarm()
    
    def create_swarm(self):
        self.node_list.append(Reference(0))
        for n in range(1,self.node_ammount):
            self.node_list.append(Subordinant(n))
    
class Node:

    def __init__(self, slot_number, location = None) -> None:
        self.slot_number = slot_number
        if location is None:
            self.location = np.array([0,0,0])
        else:
            self.location = location
    
    def make_reference(self):
        pass
    
    def make_subordinant(self):
        pass

class Reference(Node):

    def __init__(self, slot_number, location = None) -> None:
        super().__init__(slot_number, location)
        pass

class Subordinant(Node):
    def __init__(self, slot_number, location = None) -> None:
        super().__init__(slot_number, location)
        pass

test_swarm = Swarm(3)
print([x.location for x in test_swarm.node_list])