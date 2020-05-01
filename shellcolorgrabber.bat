@echo off

set port=%1
set x=%2
set y=%3
set offset=%4

cd tools
adb -s localhost:%port% shell "screencap /sdcard/screencap.dump; dd if="/sdcard/screencap.dump" bs=4 count=1 skip=%offset% 2>/dev/null | hexdump -C"