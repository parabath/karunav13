from direct.showbase.ShowBase import ShowBase
from panda3d.core import CardMaker, Texture, TransparencyAttrib
from panda3d.core import Vec3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)


        self.accept("a",self.bgaa) 
        self.accept("b",self.bgab)   
        self.accept("c",self.bgac)  
        self.accept("d",self.bgad)  
        self.accept("e",self.bgae)  
        self.accept("f",self.bgaf)                      
        # Create a card to serve as the background
 
        
        # Load a model
        self.cube = self.loader.loadModel("whiteboard_short_circuit_line_graph.glb")
        self.cube.reparentTo(self.render)
        
        # Set initial scale
        self.cube.setScale(2)
        self.cube.setPos(0, 0, 0)

        # Center the model and set it at a distance from the camera
        distance_from_camera = 10  # Adjust this value as needed
        self.cube.setPos(0, distance_from_camera, 0)
        
        # Ensure the camera is looking at the model
        self.camera.setPos(0, -20, 10)  # Adjust the camera position
        self.camera.lookAt(self.cube)

        # Add the rotation task
        self.taskMgr.add(self.rotate_cube, "RotateCubeTask")

        # Accept the 'w' key to scale the cube to zero
        self.accept("w", self.scale_cube)

    def bgaa(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('window.jpg')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back 

    def bgab(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('law1.png')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back     

    def bgac(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('photo_6145195957252375150_y.jpg')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back 

    def bgad(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('photo_6145195957252375151_y.jpg')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back   

    def bgae(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('photo_6145195957252375152_y.jpg')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back 

    def bgaf(self):
        cm = CardMaker('background')
        cm.setFrame(-1, 1, -1, 1)  # Set the size of the card
        
        # Attach the card to render2d
        self.background = render2d.attachNewNode(cm.generate())
        
        # Load the texture
        texture = self.loader.loadTexture('photo_6145195957252375153_y.jpg')
        self.background.setTexture(texture)
        
        # Enable transparency
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        
        # Position the background behind the 3D models
        self.background.setPos(0, 0, 0)  # Adjust the Z value to move it back       
    def scale_cube(self):
        self.cube.setScale(0, 0, 0)

    def rotate_cube(self, task):
        angle_degrees = task.time * 50.0  # Rotate 50 degrees per second
        self.cube.setHpr(angle_degrees, 0, 0)
        return task.cont    

app = MyApp()
app.run()
