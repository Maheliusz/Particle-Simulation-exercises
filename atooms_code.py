from atooms.system import System, Particle, Cell
from atooms.backends.dryrun import DryRun
from atooms.simulation import Simulation
import numpy
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RandomWalk(object):

    def __init__(self, system, delta=1.0):
        self.system = system
        self.delta = delta

    def run(self, steps):
        for i in range(steps):
            for particle in self.system.particle:
                move = numpy.array([float(random.randint(0,2)) 
                                  for _ in range(len(particle.position))])
                move *= self.delta
                particle.position += move
                
class NotSoRandomWalk(object):

    def __init__(self, system, delta=1.0):
        self.system = system
        self.delta = delta

    def run(self, steps):
        for i in range(steps):
            for nr, particle in enumerate(self.system.particle):
                #TODO: dodaj zmianę pozycji w każdym kroku o wartość [nr+1] w każdym kierunku
                pass
                
#callback function, called by atooms after specified amount of steps
def callback(sim, initial_position, db=None):
    positions = numpy.array([x.position for x in sim.system.particle])
    #TODO: narysuj pozycje punktów w każdym kroku
    # hint: ax2d.scatter(?,?,label=sim.current_step), ax3d.scatter(?,?,?,label=sim.current_step)


ax2d = plt.subplot(121)
ax3d = plt.subplot(122, projection='3d')

system = System(particle=[Particle(position=[10.0, 10.0, 10.0]) 
                          for _ in range(10)])

simulation = Simulation(RandomWalk(system))
simulation.add(callback, 5, initial_position=[p.position.copy() for p in
                                          system.particle])
simulation.run(10)
simulation.run(10)
simulation.run(10)
plt.show()