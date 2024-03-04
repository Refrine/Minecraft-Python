from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

#игрок
player = FirstPersonController(
    mouse_sensivity = Vec2(100,100),
    positon = (0,5,0)
    
)


ground = Entity(
    model='Plane',
    scale= (100,1,100),
    texture = 'grass',
    texture_scale=(10,10),
    collider='box'
    
)

app.run()

