@echo off

set port=%1
set x=%2
set y=%3
set duration %4

cd tools
adb -s localhost:%port% shell "input swipe %x% %y% %duration;"