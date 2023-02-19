import cv2
import numpy as np
import pygame
import tensorflow as tf

# load the saved model
model = tf.keras.models.load_model('my_model.h5')

# set up the camera and preprocessing function
cap = cv2.VideoCapture(0)
preprocess = lambda img: cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (28, 28)).reshape((28, 28, 1)) / 255.0

# initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

def process_image(screen):
    # keep processing frames until the user exits
    while True:
        # get the next frame from the camera
        ret, frame = cap.read()

        # preprocess the image
        preprocessed = preprocess(frame)

        # make a prediction on the preprocessed image
        predicted_number = np.argmax(model.predict(np.array([preprocessed])))

        # display the frame and predicted number
        cv2.imshow('frame', frame)
        print('Predicted number:', predicted_number)

        # check for user input to exit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                cap.release()
                cv2.destroyAllWindows()
                return

        # wait for a small amount of time before getting the next frame
        pygame.time.wait(10)

# start the program
process_image(screen)