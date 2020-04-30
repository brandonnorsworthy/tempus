#include <ButtonConstants.au3>
#include <ComboConstants.au3>
#include <GUIConstantsEx.au3>
#include <StaticConstants.au3>
#include <WindowsConstants.au3>
#Region ### START Koda GUI section ### Form=c:\users\brandon\desktop\ziabot\src\ziabot.kxf
$ZiaBot = GUICreate("ZiaBot", 618, 401, 657, 348)
GUISetIcon("C:\Users\Brandon\Desktop\ZiaBot\src\zbred_icon.ico", -1)
GUISetBkColor(0xB4B4B4)
$picLogo = GUICtrlCreatePic("C:\Users\Brandon\Desktop\ZiaBot\src\ziabotred.jpg", 200, 80, 212, 106)
$btnRefresh = GUICtrlCreateButton("Refresh", 368, 8, 75, 25)
GUICtrlSetColor(-1, 0xFFFFFF)
GUICtrlSetBkColor(-1, 0x171717)
$radTest = GUICtrlCreateRadio("Test", 24, 208, 113, 25)
GUICtrlSetFont(-1, 8, 800, 0, "MS Sans Serif")
$btnStart = GUICtrlCreateButton("Start", 16, 328, 587, 57)
GUICtrlSetFont(-1, 12, 800, 0, "MS Sans Serif")
GUICtrlSetColor(-1, 0xE3E3E3)
GUICtrlSetBkColor(-1, 0x171717)
$btnTestOption = GUICtrlCreateButton("Select Option", 16, 232, 123, 25)
GUICtrlSetFont(-1, 8, 800, 0, "MS Sans Serif")
GUICtrlSetColor(-1, 0xFFFFFF)
GUICtrlSetBkColor(-1, 0x171717)
$comboDevices = GUICtrlCreateCombo("", 456, 8, 153, 25, BitOR($CBS_DROPDOWN,$CBS_AUTOHSCROLL))
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###

While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		Case $btnStart
			tst()
	EndSwitch
	3

Func tst()
	Global $iResult
	$iResult = Run("colortesting.bat")
	MsgBox(0, "", "Result of Run: " & $iResult)
EndFunc

