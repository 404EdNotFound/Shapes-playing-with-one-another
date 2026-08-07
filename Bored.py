import pygame, random #Imported Modules
pygame.init()

#Creating a Window 
LENGTH, WIDTH = 800, 600
window = pygame.display.set_mode((LENGTH, WIDTH))
caption = pygame.display.set_caption("I got bored so I made this!")
clock = pygame.time.Clock()

x_velocity = y_velocity = 0

objectList = []
velocityList = []
colourList = []

# Generated to list a random colours
RANDOM_COLOURS = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "cyan", "magenta", "lime", "teal", "maroon", "navy", "olive", "brown", "white", "grey", "silver", "gold"
]

#creates the objects to be added in an array
for count in range(20):
    object = pygame.Rect(random.randrange(50, 400), random.randrange(50, 400), random.randrange(25, 50), random.randrange(25, 50))
    
    objectList.append(object)
    colourList.append(random.choice(RANDOM_COLOURS))

# each object is assigned a velocity and appended into an array
for item in objectList:
    x_velocity = random.randint(1, 5)
    y_velocity = random.randint(1, 5)
    
    velocityList.append([x_velocity, y_velocity])

# displays the rectangle in the screen
def draw():
    window.fill("black")
    for i, object in enumerate(objectList): #Enumerate is used for assigning values with indexes and these indexes can be used in other data structures
        pygame.draw.rect(window, colourList[i], object)
    
    pygame.display.update()

# used for collision between the rectangles (needed help with this)
def collisionDetection():
    for i, item in enumerate(objectList):
        for otherObject in objectList:
            if otherObject is not item:
                
                # Needed help with this
                if item.colliderect(otherObject): #used for calculating the overlap used for collision
                    overlap_X_pos = min(item.right, otherObject.right) - max(item.left, otherObject.left)
                    
                    overlap_Y_pos = min(item.bottom, otherObject.bottom) - max(item.top, otherObject.top)
                    
                    if overlap_X_pos < overlap_Y_pos:
                        velocityList[i][0] *= -1
                    
                    if overlap_X_pos > overlap_Y_pos:
                        velocityList[i][1] *= -1
                        
        if (item.left < 0 or item.right > LENGTH):
            velocityList[i][0] *= -1
        
        if (item.top < 0 or item.bottom > WIDTH):
            velocityList[i][1] *= -1

# moves the shapes based on the provided velocity
def move():
    for i, item in enumerate(objectList):
        item.x += velocityList[i][0]
        item.y += velocityList[i][1]

run = True

# Game loop that runs and checks for events and updates the whole program
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()
    move()
    collisionDetection()
    
pygame.quit()