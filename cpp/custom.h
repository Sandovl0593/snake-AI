//
// Created by adria on 19/2/2023.
//
#ifndef CPP_CUSTOM_H
#define CPP_CUSTOM_H

#include <list>
#include <string>

typedef std::list<std::pair<int, int>> tuples;

class Head {
    std::string to_direction = "right";
    std::string inv_direction = "right";
public:
    int x, y;
    Head(int x_, int y_): x(x_), y(y_) {}

    void move(char key) {
        if (key = 'a' && inv_direction != "right")
            to_direction = "left";
        else if (key == 'd' && inv_direction != "left")
            to_direction = "right";
        else if (key == 'w' && inv_direction != "down")
            to_direction = "up";
        else if (key == 's' && inv_direction != "up")
            to_direction = "down";

        inv_direction = to_direction;

        if (to_direction == "right")   x+=10;
        else if (to_direction == "left")    x-=10;
        else if (to_direction == "down")    y+=10;
        else if (to_direction == "up")    y-=10;
    }

    ~Head() {}
};

class Snake {
    Head* head;
    tuples body;
    unsigned int score;
public:
    bool closed = false;

    Snake(Head* head_, tuples body_, int scor): head(head_), body(body_), score(scor) {}

    bool colision_apple(std::pair<int, int> coords) {
        body.push_front(std::pair<int, int>(head->x, head->y));
        if (head->x == coords.first && head->y == coords.second) {
            score++;   return true;
        } else {
            body.pop_back();  return false;
        }
    }

    void colision_wall() {
        if (head->x>=500 || head->x<0 || head->y>=500 || head->y<0)  closed = true;
    }

    ~Snake() {  delete head; }
};

#endif //CPP_CUSTOM_H
