#include <opencv2/highgui.hpp>
#include <time.h>
#include "custom.h"

using namespace cv;
using namespace std;

typedef list<pair<int, int>> tuples;

const tuples INIT_POSITION = {{250, 250}, {240, 250}, {230, 250}};
const int INIT_HEAD_X = 250, INIT_HEAD_Y = 250;

class Screen {
    Snake* snake = new Snake(new Head(INIT_HEAD_X, INIT_HEAD_Y), INIT_POSITION, 0);
    int apple[2] = {(1+ rand()%49)*10, (1+ rand()%49)*10};

public:
    Screen() {}

    void update() {

    }

    Snake* current_snake() {  return snake; }

    void insert_key() {

    }

    ~Screen()  { deleet snake; }
};

int main(void) {

    Screen* game = new Screen();

    while (true) {
        game->update();

        // bucle de esperar tecla por cada paso del snake

        game->insert_key();

        if (game->current_snake()->closed) {
            // mostrar el score
            break;
        }

    }
    destroyAllWindows();
    delete game;
	return 0;
}