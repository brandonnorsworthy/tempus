@echo off

set port=%1
set x1=%2
set y1=%3
set x2=%4
set y2=%5

cd tools
adb -s localhost:%port% shell "input swipe %x1% %y1% %x2% %y2%;"