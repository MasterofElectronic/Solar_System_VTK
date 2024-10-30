import vtk, math

class Moon:

    def __init__(self, name, radius, texture_file, orbit_radius, orbit_speed):

        self.name = name
        self.radius = radius
        self.texture_file = texture_file
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.orbit_angle = 0.0
        self.planet_position = (0, 0, 0)

        self.actor = self.create_moon_actor()


    def create_moon_actor (self):


        sphere = vtk.vtkTexturedSphereSource()
        sphere.SetRadius(self.radius)
        sphere.SetThetaResolution(30)
        sphere.SetPhiResolution(30)

        texture = vtk.vtkTexture()
        texture_reader = vtk.vtkJPEGReader()
        texture_reader.SetFileName(self.texture_file)
        texture.SetInputConnection(texture_reader.GetOutputPort())

        texture_mapper = vtk.vtkPolyDataMapper()
        texture_mapper.SetInputConnection(sphere.GetOutputPort())

        moon_actor = vtk.vtkActor()
        moon_actor.SetMapper(texture_mapper)
        moon_actor.SetTexture(texture)

        return moon_actor


    def orbit(self, planet_position):

        self.orbit_angle += self.orbit_speed
        x = planet_position[0] + self.orbit_radius * math.cos(math.radians(self.orbit_angle))
        y = planet_position[1] + self.orbit_radius * math.sin(math.radians(self.orbit_angle))

        self.actor.SetPosition(x, y, planet_position[2])

    def get_actor(self):

        return self.actor
