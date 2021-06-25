@echo off

cd tools

adb disconnect

adb connect localhost:5555
adb connect localhost:5565



::commenting out a bunch of ports as during testing more than 4 will never be run,
::will work on dynamically choosing the number of ports later
::adb connect localhost:5575
::adb connect localhost:5585
::adb connect localhost:5595
::adb connect localhost:5605
::adb connect localhost:5615
::adb connect localhost:5625
::adb connect localhost:5635
::adb connect localhost:5645