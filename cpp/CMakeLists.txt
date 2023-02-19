cmake_minimum_required(VERSION 3.23)

project(cpp)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# Where to find CMake modules and OpenCV
# set(OpenCV_DIR "C:\\opencv\\build\\include")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(image screen.cpp custom.h)

# add libs you need
set(OpenCV_LIBS opencv_core opencv_imgproc opencv_highgui opencv_imgcodecs)

# linking
target_link_libraries(image ${OpenCV_LIBS})