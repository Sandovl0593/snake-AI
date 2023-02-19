
class Snake:

    def __init__(self, head, body, score):
        self.head:Head = head
        self.body:list = body
        self.closed = False
        self.score = score

    def colision_apple(self, coords):
        self.body.insert(0,[self.head.x, self.head.y])
        if self.head.x == coords[0] and self.head.y == coords[1]:
            self.score += 1
            return True
        else:
            self.body.pop()
            return False
    
    def colision_wall(self):
       if self.head.x>=500 or self.head.x<0 or self.head.y>=500 or self.head.y<0:
           self.closed = True

class Head:
    def __init__(self, x, y):
        self.to_direction = "right"
        self.inv_direction = "right"
        self.x = x
        self.y = y
    
    def move(self, key):
        
        if key == ord('a') and self.inv_direction != 'right':
            self.to_direction = "left"
        elif key == ord('d') and self.inv_direction != 'left':
            self.to_direction = "right"
        elif key == ord('w') and self.inv_direction != 'down':
            self.to_direction = "up"
        elif key == ord('s') and self.inv_direction != 'up':
            self.to_direction = "down"
        
        self.inv_direction = self.to_direction

        if self.to_direction == "right":
            self.x += 10
        elif self.to_direction == "left":
            self.x -= 10
        elif self.to_direction == "down":
            self.y += 10
        elif self.to_direction == "up":
            self.y -= 10