cmake_minimum_required(VERSION 2.8.3)
project(actions_quiz)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib
  actionlib_msgs # Add this line
)

## Generate actions in the 'action' folder
add_action_files(
  FILES
  ArdroneAction.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES std_msgs
)

## Declare a catkin package
catkin_package(
  CATKIN_DEPENDS message_runtime actionlib actionlib_msgs
)

## Build
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Install
catkin_install_python(
  PROGRAMS
  scripts/actions_quiz.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Testing
if(CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch)
endif()
