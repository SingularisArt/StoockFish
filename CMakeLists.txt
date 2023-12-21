cmake_minimum_required(VERSION 3.12)

project(ChessEngine)

set(CMAKE_CXX_STANDARD 11)

# Add your source files
file(GLOB SOURCE_FILES "src/*.cpp" "src/*.h")

# Add the executable
add_executable(ChessEngine ${SOURCE_FILES})

# SDL2
find_package(SDL2 REQUIRED)
include_directories(${SDL2_INCLUDE_DIRS})
target_link_libraries(ChessEngine ${SDL2_LIBRARIES})
