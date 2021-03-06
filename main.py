import threading
import ursina
from calc import *
from gui import Simulation
from planet import Planet, Sky



class Main:
    def __init__(self,  app,  planet_list=[]):
        # SET BASIC VARIABLES FOR ursina -------------------------------------------------------
        self.app = app

        ursina.window.title = 'planet simulation'  # set meta data for app
        ursina.window.borderless = True
        ursina.window.fullscreen = True
        ursina.window.exit_button.visible = False
        ursina.window.fps_counter.enabled = True

        self.planet_list = planet_list  # list of all planets in the simulation

        # CREATION OF SUN  ---------------------------------------------------------------------

        Planet(file_name='/textures/sun', planet_name="sun", planet_diameter=2.5, plannr=0)

        # CREATION OF SKY ----------------------------------------------------------------------

        Sky()

        # CREATION OF SIMULATION ---------------------------------------------------------------

        simulation = Simulation(self.planet_list)

        # CREATION OF THREADS ------------------------------------------------------------------

        for planet in self.planet_list:
            # For every planet, there is a thread, which calculates the current Position of its planet
            calc = Calc(planet)
            temp = threading.Thread(target=calc.get_coords, args=(planet,))
            temp.start()

        # STARTS THE SIMULATION ---------------------------------------------------------------
        # runs simulation.update() constantly
        self.app.run()
