import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
size = (600, 600)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Fractal Tree")

# Define the colors we will use
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the parameters of the fractal tree
angle = 0
length = 150

def branch(length, angle, x, y):
    # Draw the branch
    end_x = x + length * math.sin(angle)
    end_y = y - length * math.cos(angle)
    pygame.draw.line(screen, WHITE, [x, y], [end_x, end_y], 3)

    # Check if the branch is long enough to have sub-branches
    if length > 10:
        # Draw a sub-branch on the left
        branch(length * 0.67, angle + math.pi/6, end_x, end_y)
        # Draw a sub-branch on the right
        branch(length * 0.67, angle - math.pi/3, end_x, end_y)

# Set up the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Get the position of the mouse
    mouse_pos = pygame.mouse.get_pos()

    # Update the parameters of the fractal tree based on the mouse position
    angle = (mouse_pos[0] - size[0]/2) * math.pi / size[0]
    length = mouse_pos[1] / 2

    # Update the position of the tree so that it is centered on the screen
    tree_x = size[0] / 2
    tree_y = size[1]

    # Draw the fractal tree
    branch(length, -math.pi/2 + angle, tree_x, tree_y)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
