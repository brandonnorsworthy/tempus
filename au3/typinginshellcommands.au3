start()

Func start()
	Sleep(2000)
	Send("dd if=""/sdcard/screencap.dump"" bs=4 count=1 skip=250922 2>/dev/null | hexdump -C")
EndFunc