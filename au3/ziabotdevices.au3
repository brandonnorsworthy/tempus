#NoTrayIcon
#include <Constants.au3>
#include <GUIConstants.au3>
#include <SendMessage.au3>
#include <ScrollBarsConstants.au3>
#include <GUIConstants.au3>

Opt("GUIOnEventMode", 1)

Global $Form1 = GUICreate("Form1", 577, 329, 330, 318)
Global $Buildprop = GUICtrlCreateButton("Build.prop Info", 24, 56, 113, 185)
Global $Logs = GUICtrlCreateEdit("", 216, 56, 297, 193, BitOR($GUI_SS_DEFAULT_EDIT,$ES_READONLY))
GUICtrlSetOnEvent($Buildprop, '_Buildprop')
GUISetOnEvent($GUI_EVENT_CLOSE, '_AllExit', $Form1)
GUICtrlSetData($Logs, "Logs" & @CRLF)
GUISetState(@SW_SHOW, $Form1)

If not FileExists(@TempDir & "\adb.exe") Then FileInstall("adb.exe", @TempDir & "\adb.exe", $FC_OVERWRITE)
If not FileExists(@TempDir & "\AdbWinApi.dll") Then FileInstall("AdbWinApi.dll", @TempDir & "\AdbWinApi.dll", $FC_OVERWRITE)
If not FileExists(@TempDir & "\AdbWinUsbApi.dll") Then FileInstall("AdbWinUsbApi.dll", @TempDir & "\AdbWinUsbApi.dll", $FC_OVERWRITE)

While 1
   Sleep(3000)
   _SendMessage(GUICtrlGetHandle($Logs), $WM_VSCROLL, $SB_BOTTOM, 0)

WEnd

Func _AllExit()
   GUIDelete(@GUI_WinHandle)
   Exit
EndFunc

Func _Buildprop()
   $iPID = Run('adb shell "dd if="/sdcard/screencap.dump" bs=4 count=1 skip=360503 2>/dev/null | hexdump -C"', "", @SW_HIDE, $STDERR_CHILD + $STDOUT_CHILD)
   ProcessWaitClose($iPID)
   $sOutput = StringStripWS(StdoutRead($iPID), $STR_STRIPLEADING + $STR_STRIPTRAILING)
   $sOutput = StringTrimLeft ($sOutput, 9)
   $sOutput = StringTrimRight ($sOutput, StringLen($sOutput) - 10)
   $sOutput = StringStripWS($sOutput, $STR_STRIPALL)
   ConsoleWrite("Color" & $sOutput)
EndFunc