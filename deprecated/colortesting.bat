cd C:\Users\Brandon\Desktop\ZiaBot\tools
adb shell screencap /sdcard/screencap.dump
adb shell dd if=/sdcard/screencap.dump bs=4 count=1 skip=215837 2>/dev/null | hexdump -C
