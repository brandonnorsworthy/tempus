@echo off

set port=%1
set x=%2
set y=%3

cd tools
adb -s localhost:%port% shell "input tap %x% %y%;"