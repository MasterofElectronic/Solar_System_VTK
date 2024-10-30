import vtk
import argparse
import json 
from moon import Moon
from planet import Planet
import math


#Funcion de renderizado

def setup_renderer(planets):

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0, 0, 0)

    for planet in planets:
        actor = planet.create_actor()  # Crear el actor para cada planeta
        renderer.AddActor(actor)  # Añadir planeta al renderizador

    return renderer
    

def setup_render_window(renderer):
   
    render_window = vtk.vtkRenderWindow()
    render_window.SetWindowName("Sistema Solar")
    render_window.SetSize(1000, 1000)  
    render_window.AddRenderer(renderer)

    # Interactor
    render_interactor = vtk.vtkRenderWindowInteractor()
    render_interactor.SetRenderWindow(render_window)

    return render_window, render_interactor

#Actualizar la posicion de los planetas
def update_planets(planets, iren, event):
    
    for planet in planets:
        planet.rotate()  # Rotar el planeta
        planet.orbit()   # Trasladar el planeta en su órbita
    
    iren.GetRenderWindow().Render()  # Renderizar de nuevo

def main():

    factor_expancion = 5
    factor_velocidad = 1

    planets = [
        Planet(name="Sol", radius=4.65, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/sun.jpg", position=(0, 0, 0), orbit_radius=0, rotation_speed=0.5*factor_velocidad, orbit_speed=0*factor_velocidad),
        Planet(name="Mercurio", radius=0.017*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/mercury.jpg", position=(0.39, 0, 0), orbit_radius=7, rotation_speed=1.0*factor_velocidad, orbit_speed=4.74*factor_velocidad),
        Planet(name="Venus", radius=0.042*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/venus.jpg", position=(0.72, 0, 0), orbit_radius=10, rotation_speed=0.8*factor_velocidad, orbit_speed=3.5*factor_velocidad),
        Planet(name="Tierra", radius=0.045*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/earth.jpg", position=(1, 0, 0), orbit_radius=13, rotation_speed=0.9*factor_velocidad, orbit_speed=2.98*factor_velocidad),
        Planet(name="Marte", radius=0.024*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/mars.jpg", position=(1.52, 0, 0), orbit_radius=16, rotation_speed=0.95*factor_velocidad, orbit_speed=2.41*factor_velocidad),
        Planet(name="Júpiter", radius=0.5*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/jupiter.jpg", position=(5.2, 0, 0), orbit_radius=30, rotation_speed=2.4*factor_velocidad, orbit_speed=1.31*factor_velocidad),
        Planet(name="Saturno", radius=0.42*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/saturn.jpg", position=(9.58, 0, 0), orbit_radius=40, rotation_speed=2.0*factor_velocidad, orbit_speed=0.97*factor_velocidad),
        Planet(name="Urano", radius=0.18*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/uranus.jpg", position=(19.22, 0, 0), orbit_radius=55, rotation_speed=1.6*factor_velocidad, orbit_speed=0.68*factor_velocidad),
        Planet(name="Neptuno", radius=0.17*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/neptune.jpg", position=(30.05, 0, 0), orbit_radius=70, rotation_speed=1.5*factor_velocidad, orbit_speed=0.54*factor_velocidad),
        
        Planet(name="Luna", radius=0.008*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/moon.jpg", position=(1.00257, 0, 0), orbit_radius=0.6, rotation_speed=0.27, orbit_speed=6.3, sun_position=(13, 0, 0))
    ]

    
    renderer = setup_renderer(planets)

    
    render_window, render_interactor = setup_render_window(renderer)


    render_interactor.Initialize()
    render_interactor.AddObserver('TimerEvent', lambda iren, event: update_planets(planets, iren, event))
    render_interactor.CreateRepeatingTimer(20)  # Crear un temporizador que se repite cada 20 ms (50 FPS aproximadamente)

    
    render_window.Render()
    render_interactor.Start()

if __name__ == "__main__":
    main()