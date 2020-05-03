@echo off

set port=%1
set input=%2

cd tools
adb -s localhost:%port% shell "input text %input%;"