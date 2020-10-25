from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()  # App erstellen

window.title = 'Planetensimulation'  # 'Meta-Daten' der App setzen
window.borderless = True
window.fullscreen = True
window.exit_button.visible = True
window.fps_counter.enabled = True


class Planet(Entity):
    def __init__(self, color, speed=1, mass=1, diameter=1, x=0, y=0, z=0):  # Entity wird erstellt, indem die init-Methode der Entity-Klasse aufgerufen wird
        super().__init__(
            model='sphere',  # Planet soll ballförmig sein
            color=color,  # farbe des Planeten wird festgelegt
            collision=True,
            collider='sphere'
            # TODO: Texturen hinzufügen
        )
        self.speed = speed
        self.mass = mass
        self.scale = Vec3(diameter, diameter, diameter)
        self.x = x
        self.y = y
        self.z = z

    def set_coords(self, x, y, z):  # Koordinaten eines Planeten setzen
        self.x = x
        self.y = y
        self.z = z


planet = Planet(color=color.orange)
planet.set_coords(9,0,9)
player = FirstPersonController()  # First-Person-Controller wird erstellt (prä-fabrizierte Klasse, modifiziert, dass das Springen und die Schwerkraft nicht mehr existieren und man sich mit shift und space auf und ab bewegen kann)
app.run()