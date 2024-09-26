cmake_minimum_required(VERSION 3.20.0)

message(STATUS "List Dir: ${CMAKE_CURRENT_LIST_DIR}")

set(PONGRL_SRC_ROOT_DIR, ${CMAKE_CURRENT_LIST_DIR}/pongrl)
set(PONGRL_REPO_ROOT_DIR ${CMAKE_CURRENT_LIST_DIR})
set(PONGRL_BUILD_ROOT_DIR, ${CMAKE_CURRENT_BINARY_DIR})
set(PONGRL_DEVOPS_DIR ${PONGRL_REPO_ROOT_DIR}/devops)
set(PONGRL_BUILD_TEST_XML_OUTPUT_DIR, ${CMAKE_CURRENT_BINARY_DIR}/junit_xml_reports)
set(PONGRL_GENERATED_INCLUDES "${PONGRL_BUILD_ROOT_DIR}/generated_src")

# -- Load version information from a file
file(STRINGS  ${PONGRL_DEVOPS_DIR}/version.txt raw_version_vars)
list(LENGTH raw_version_vars raw_version_vars_len)
list(GET raw_version_vars 0 RAW_VER_MAJOR)
list(GET raw_version_vars 1 RAW_VER_MINOR)
list(GET raw_version_vars 2 RAW_VER_PATCH)

project(PongRL VERSION ${RAW_VER_MAJOR}.${RAW_VER_MINOR}.${RAW_VER_PATCH} 
DESCRIPTION "A basic game with the intention of using the api to train an RL model"
LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(BUILD_SHARED_LIBS TRUE)

list(APPEND CMAKE_MODULE_PATH "${PONGRL_REPO_ROOT_DIR}/installs/cmake")

set(CMAKE_DEBUG_POSTFIX "_d")

find_package(SFML REQUIRED)
target_link_libraries(PongRL
    PUBLIC 
        sfml-graphics)

add_library(PongRL PongRL.cpp)
add_executable(main PongRL.cpp)

include(CTest)
enable_testing()

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
