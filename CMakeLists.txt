# CMake version
cmake_minimum_required(VERSION 3.12)

# Project name
project(ChessEngine)

# Set C++ standard
set(CMAKE_CXX_STANDARD 11)

# Add source files
file(GLOB SOURCE_FILES "src/*.cpp" "src/*.h")

# Add the executable
add_executable(ChessEngine ${SOURCE_FILES})

# SDL2
find_package(SDL2 REQUIRED)
include_directories(headers ${SDL2_INCLUDE_DIRS})

# Add SDL2_image at link time
target_link_libraries(ChessEngine ${SDL2_LIBRARIES} SDL2_image)
