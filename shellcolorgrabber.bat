@echo off

set port=%1
set offset=%2

cd tools
adb -s localhost:%port% shell "screencap /sdcard/screencap.dump; dd if=""/sdcard/screencap.dump"" bs=4 count=1 skip=%offset% 2>/dev/null | hexdump -C"