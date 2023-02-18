import pygame
from keras.models import load_model
import tensorflow as tf
import numpy as np



model = load_model('my_model.h5')

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
size = (280, 280)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Handwritten Digit Recognizer")

# Define the colors we will use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the font for drawing text on the screen
font = pygame.font.Font(None, 36)

# Define the size of the drawing surface
draw_size = (280, 280)

# Create a drawing surface to draw on
drawing_surface = pygame.Surface(draw_size)
drawing_surface.fill(BLACK)

# Set the drawing color to white
drawing_color = WHITE

# Load the trained model
model = tf.keras.models.load_model("mnist_model.h5")

# Set up the main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # If the left mouse button is held down, draw a line
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.line(drawing_surface, drawing_color, event.pos, event.pos, 10)
        elif event.type == pygame.KEYDOWN:
            # Clear the drawing surface if the user presses the spacebar
            if event.key == pygame.K_SPACE:
                drawing_surface.fill(BLACK)

            # Recognize the handwritten digit if the user presses the enter key
            elif event.key == pygame.K_RETURN:
                # Resize the drawing surface to 28x28 pixels
                digit_surface = pygame.transform.smoothscale(drawing_surface, (28, 28))
                digit_image = pygame.surfarray.array2d(digit_surface)
                digit_image = np.expand_dims(digit_image, axis=0)
                digit_image = np.expand_dims(digit_image, axis=-1)

                # Normalize the pixel values to be between 0 and 1
                digit_image = digit_image / 255.0

                # Use the model to predict the digit
                prediction = model.predict(digit_image)
                digit = np.argmax(prediction)

                # Display the predicted digit on the screen
                text = font.render(str(digit), True, WHITE)
                screen.blit(text, (10, 10))

    # Draw the drawing surface on the screen
    screen.blit(drawing_surface, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()