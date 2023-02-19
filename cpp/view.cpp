#include <opencv2/highgui.hpp>
using namespace cv;

int main(void) {

	// Read image in GrayScale mode
	Mat image = imread("photo.jpg", IMREAD_COLOR);

	// Save grayscale image
	// imwrite("boyGray.jpg", image);

	// To display the image
	imshow("First image", image);
	waitKey(0);

	return 0;
}