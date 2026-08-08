# Imported Pygame and Random
import pygame, random
pygame.init()

# Constants defined for Window size and the FPS (useful for the screen interface and for the Game Running with constant FPS)
LENGTH, WIDTH = 800, 600
FPS = 60

# Creating the Window with a Time Clock
window = pygame.display.set_mode((LENGTH, WIDTH))
caption = pygame.display.set_caption("I make this because I was bored but with OOP this time!!!")
clock = pygame.time.Clock()

# Random Colours that are generated
RANDOM_COLOURS = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "teal", "maroon", "navy", "olive", "brown", "white", "grey", "silver", "gold"
]

# List used for containing objects of the shape
shapeList = []

# Shape Class used for the Shape Objects
class Shape:
    #initialised with the attributes
    def __init__(self, x, y, length, width, x_velocity, y_velocity, colour):
        self.rectangle = pygame.Rect(x, y, length, width)
        self.x_velocity, self.y_velocity = x_velocity, y_velocity
        self.colour = colour
    
    # move method for moving the shapes based on their velocity
    def move(self):
        self.rectangle.x += self.x_velocity
        self.rectangle.y += self.y_velocity
    
    # Collision method for colliding with the different objects (needed help with this)
    def collision(self):
        for other in shapeList:
            if other is not self:
                if self.rectangle.colliderect(other.rectangle):
                    x_pos_overlap = min(self.rectangle.right, other.rectangle.right) - max(self.rectangle.left, other.rectangle.left)
                    y_pos_overlap = min(self.rectangle.bottom, other.rectangle.bottom) - max(self.rectangle.top, other.rectangle.top)
                    
                    if x_pos_overlap < y_pos_overlap:
                        self.x_velocity *= -1
                    
                    if x_pos_overlap > y_pos_overlap:
                        self.y_velocity *= -1
                        
        if (self.rectangle.left < 0 or self.rectangle.right > LENGTH):
            self.x_velocity *= -1
        
        if (self.rectangle.top < 0 or self.rectangle.bottom > WIDTH):
            self.y_velocity *= -1

# Creating Shape Objects to be stored on the list
for count in range(20):
    shapeObject = Shape(random.randint(50, 700), random.randint(50, 500), random.randint(25, 50), random.randint(25, 50), random.randint(1, 5), random.randint(1, 5), random.choice(RANDOM_COLOURS))
    
    shapeList.append(shapeObject)
 
# Drawing all shapes into the Python Interface   
def draw():
    window.fill((0, 0, 0))
    for shape in shapeList:
        pygame.draw.rect(window, shape.colour, shape.rectangle)
    pygame.display.update()

run = True

# Game Event Loop that is used for running the interface
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for shape in shapeList:
        shape.move() 
        shape.collision()
    draw()

pygame.quit()