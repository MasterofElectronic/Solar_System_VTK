import vtk
import math

class Planet:
    
    def __init__(self, name, radius, texture_file, position, orbit_radius, rotation_speed, orbit_speed, sun_position=(0, 0, 0)):

        self.name = name
        self.radius = radius
        self.texture_file = texture_file
        self.position = position 
        self.orbit_radius = orbit_radius
        self.rotation_speed = rotation_speed
        self.orbit_speed = orbit_speed
        self.actor = None 
        self.orbit_angle = 0  
        self.rotation_angle = 0
        self.sun_position = sun_position

    #Funcion para crear la esfera

    def create_sphere(self, resolution= 50):
    
        sphere = vtk.vtkSphereSource()
        sphere.SetRadius(self.radius)
        sphere.SetThetaResolution(resolution)
        sphere.SetPhiResolution(resolution)

        return sphere
    
    #funcion para aplicar texturas

    # def apply_texture(self, actor):
        
    #     #lee la imagen de textura
    #     reader = vtk.vtkJPEGReader()
    #     reader.SetFileName(self.texture_file)

    #     texture = vtk.vtkTexture()
    #     texture.SetInputConnection(reader.GetOutputPort())
    #     texture.InterpolateOn()

    #     actor.SetTexture(texture)



    def create_actor(self):
        # Crear la esfera
        sphere = self.create_sphere()

        # Mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        # Actor
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.SetPosition(*self.position)  # Posicionar el planeta

        # Aplicar la textura
        texture = vtk.vtkTexture()
        jpeg_reader = vtk.vtkJPEGReader()
        jpeg_reader.SetFileName(self.texture_file)
        texture.SetInputConnection(jpeg_reader.GetOutputPort())
        self.actor.SetTexture(texture)
        
        return self.actor
    
    def rotate(self):
        
        self.rotation_angle += self.rotation_speed
        self.actor.RotateY(self.rotation_speed)


    def orbit(self):
        
        self.orbit_angle += self.orbit_speed
        
        # Calcular las nuevas coordenadas basadas en la posición del Sol y el ángulo de la órbita
        x = self.sun_position[0] + self.orbit_radius * math.cos(math.radians(self.orbit_angle))
        y = self.sun_position[1] + self.orbit_radius * math.sin(math.radians(self.orbit_angle))

        # Actualizar la posición del planeta
        self.actor.SetPosition(x, y, self.sun_position[2])


