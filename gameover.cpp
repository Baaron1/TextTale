#include <cv.h>
#include <highgui.h>

using namespace cv;

int main()
{

Mat im = imread("image.jpg", CV_LOAD_IMAGE_COLOR);
namedWindow("image");
imshow("image", im);
waitKey(0);
}