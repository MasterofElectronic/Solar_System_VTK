import math
import vtk
import json 
from moon import Moon
from planet import Planet
import sys


#luces
# def setupt_light(renderer):

#     positions = [
#         (0, 0, 10), (0, 0, -10), (10, 0, 0), (-10, 0, 0),
#         (0, 10, 0), (0, -10, 0), (10, 10, 10), (-10, -10, -10)
#     ]

#     for pos in positions:
#         light = vtk.vtkLight()
#         light.SetLightTypeToSceneLight()
#         light.SetPosition(pos) #el sol
#         light.SetPositional(True)
#         #light.SetConeAngle(180)
#         light.SetFocalPoint(0,0,0)
#         light.SetIntensity(0.5)
#         renderer.AddLight(light)
#         light.SwitchOn()

#     return light

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)



def create_planets_from_json(descriptor):
    sun_data = descriptor["Sun"]
    sun_size = float(sun_data["size"])  # Escalamos el tamaño para que sea manejable
    scale_factor_size = sun_size / 1000000  
    scale_factor_orbit = sun_size / 1e8

    planets = []
    # Crear el Sol
    sol = Planet(name="sun", 
                 radius=sun_size / scale_factor_size, 
                 texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/sun.jpg", 
                 position=(0, 0, 0), 
                 orbit_radius=0, 
                 rotation_speed=1, 
                 orbit_speed=0)
    planets.append(sol)

    print(sun_size)

    

    # Crear planetas y satélites
    for planet_name, planet_data in sun_data["planets"].items():
        planet_radius = float(planet_data["size"]) * scale_factor_size
        orbit_radius = float(planet_data["orbit"]) * scale_factor_orbit + sun_size
        period = float(planet_data["period"])
        rotation_speed = 1 / period


        planet = Planet(
            name=planet_name, 
            radius=planet_radius, 
            texture_file=f"src/textures/{planet_name.lower()}.jpg", 
            position = (orbit_radius, 0, 0), 
            orbit_radius = orbit_radius, 
            rotation_speed = rotation_speed,  
            orbit_speed = (2 * math.pi) / period
        )
        planets.append(planet)
        
        if "satellites" in planet_data:
            for satellite_name, satellite_data in planet_data["satellites"].items():
                satellite_radius = float(satellite_data["size"]) / 100000
                satellite_orbit_radius = float(satellite_data["orbit"]) / 100000000
                satellite_period = float(satellite_data["period"])

                satellite = Planet(
                    name=satellite_name, 
                    radius=satellite_radius, 
                    texture_file=f"src/textures/{satellite_name.lower()}.jpg", 
                    position=(orbit_radius + satellite_orbit_radius, 0, 0), 
                    orbit_radius=satellite_orbit_radius, 
                    rotation_speed = 0.5, 
                    orbit_speed = (2 * math.pi) / satellite_period, 
                    sun_position=(orbit_radius, 0, 0)
                )
                planets.append(satellite)

    return planets

#Funcion de renderizado

def setup_renderer(planets):

    renderer = vtk.vtkRenderer()
    

    for planet in planets:
        actor = planet.create_actor()  # Crear el actor para cada planeta
        renderer.AddActor(actor)  # Añadir planeta al renderizador

    #setupt_light(renderer)
    renderer.SetBackground(0, 0, 0)

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

    if len(sys.argv) != 2:
        print("Uso: python main.py <descriptor.json>")
        return
    
    descriptor_file = sys.argv[1]
    descriptor = read_json(descriptor_file)
    planets = create_planets_from_json(descriptor)

    # factor_expancion = 4
    # factor_velocidad = 0

    # planets = [
    #     Planet(name="Sol", radius=4.65, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/sun.jpg", position=(0, 0, 0), orbit_radius=0, rotation_speed=0.5*factor_velocidad, orbit_speed=0*factor_velocidad),
    #     Planet(name="Mercurio", radius=0.017*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/mercury.jpg", position=(0.39, 0, 0), orbit_radius=7, rotation_speed=1.0*factor_velocidad, orbit_speed=4.74*factor_velocidad),
    #     Planet(name="Venus", radius=0.042*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/venus.jpg", position=(0.72, 0, 0), orbit_radius=10, rotation_speed=0.8*factor_velocidad, orbit_speed=3.5*factor_velocidad),
    #     Planet(name="Tierra", radius=0.045*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/earth.jpg", position=(1, 0, 0), orbit_radius=13, rotation_speed=0.9*factor_velocidad, orbit_speed=2.98*factor_velocidad),
    #     Planet(name="Marte", radius=0.024*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/mars.jpg", position=(1.52, 0, 0), orbit_radius=16, rotation_speed=0.95*factor_velocidad, orbit_speed=2.41*factor_velocidad),
    #     Planet(name="Júpiter", radius=0.5*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/jupiter.jpg", position=(5.2, 0, 0), orbit_radius=30, rotation_speed=2.4*factor_velocidad, orbit_speed=1.31*factor_velocidad),
    #     Planet(name="Saturno", radius=0.42*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/saturn.jpg", position=(9.58, 0, 0), orbit_radius=40, rotation_speed=2.0*factor_velocidad, orbit_speed=0.97*factor_velocidad),
    #     Planet(name="Urano", radius=0.18*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/uranus.jpg", position=(19.22, 0, 0), orbit_radius=55, rotation_speed=1.6*factor_velocidad, orbit_speed=0.68*factor_velocidad),
    #     Planet(name="Neptuno", radius=0.17*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/neptune.jpg", position=(30.05, 0, 0), orbit_radius=70, rotation_speed=1.5*factor_velocidad, orbit_speed=0.54*factor_velocidad),
        
    #     Planet(name="Luna", radius=0.008*factor_expancion, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/moon.jpg", position=(1.00257, 0, 0), orbit_radius=0.6, rotation_speed=0.27, orbit_speed=6.3, sun_position=(13, 0, 0))
    # ]

    
    renderer = setup_renderer(planets)

    
    render_window, render_interactor = setup_render_window(renderer)


    render_interactor.Initialize()
    render_interactor.AddObserver('TimerEvent', lambda iren, event: update_planets(planets, iren, event))
    render_interactor.CreateRepeatingTimer(20)  # Crear un temporizador que se repite cada 20 ms (50 FPS aproximadamente)

    
    render_window.Render()
    render_interactor.Start()

if __name__ == "__main__":
    main()