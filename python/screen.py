import cv2
import random as rd
import numpy as np
from custom import *
import time

INIT_POSITION = [[250,250],[240,250],[230,250]]
INIT_HEAD_X, INIT_HEAD_Y = 250, 250
APPLE_COLOR = (0,0,255)
SNAKE_COLOR = (0,255,0)

class Screen:

    def __init__(self):
        self.img = np.zeros((500,500,3),dtype='uint8')
        self.snake = Snake(Head(INIT_HEAD_X, INIT_HEAD_Y), INIT_POSITION, 0)
        self.apple = [rd.randrange(1,50)*10, rd.randrange(1,50)*10 ]

    def update(self):

        cv2.imshow('Snake game', self.img)
        cv2.waitKey(1)
        self.img = np.zeros((500,500,3),dtype='uint8')

        # displya the apple
        cv2.rectangle(self.img,(self.apple[0], self.apple[1]),(self.apple[0]+10,self.apple[1]+10),APPLE_COLOR, 3)

        # display the body
        for position in self.snake.body:
            cv2.rectangle(self.img,(position[0],position[1]),(position[0]+10,position[1]+10),SNAKE_COLOR,3)

    def insertKey(self, key):

        if key == ord('q'):
            self.snake.closed = True

        self.snake.head.move(key)

        if self.snake.colision_apple(self.apple):
            self.apple[0] = rd.randrange(1,50)*10
            self.apple[1] = rd.randrange(1,50)*10
            
        self.snake.colision_wall()


if __name__ == "__main__":
    game = Screen()

    while True:
        game.update()

        t_end = time.time() + 0.2
        k = -1
        while time.time() < t_end:
            if k == -1:
                k = cv2.waitKey(125)
            else:
                continue

        game.insertKey(k)

        if game.snake.closed:

            font = cv2.FONT_HERSHEY_SIMPLEX
            game.img = np.zeros((500,500,3),dtype='uint8')
            cv2.putText(game.img,'Your Score is {}'.format(game.snake.score),(140,250), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.imshow('Snake game',game.img)
            cv2.waitKey(0)
            break

    cv2.destroyAllWindows()