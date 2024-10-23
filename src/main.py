import vtk
from planet import Planet

#Funcion de renderizado

def setup_renderer(planets):

    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.1, 0.1, 0.1)

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
    
    print("Planetas actualizados")
    iren.GetRenderWindow().Render()  # Renderizar de nuevo

def main():


    planets = [
        Planet(name="Mercurio", radius=0.5, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/jupiter.jpg", position=(2, 0, 0), orbit_radius=5, rotation_speed=0.05, orbit_speed=0.01),
        Planet(name="Venus", radius=0.8, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/descarga.jpeg", position=(5, 0, 0), orbit_radius=2, rotation_speed=0.04, orbit_speed=0.02),
        Planet(name="Tierra", radius=1.0, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/jupiter.jpg", position=(8, 0, 0), orbit_radius=4, rotation_speed=0.03, orbit_speed=0.05),
        Planet(name="Marte", radius=0.6, texture_file="C:/Users/jhona/Documents/Javeriana/Primer Semestre/Computación Gráfica/vtk/sistema_solar/src/textures/jupiter.jpg", position=(11, 0, 0), orbit_radius=8, rotation_speed=0.07, orbit_speed=0.07),
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