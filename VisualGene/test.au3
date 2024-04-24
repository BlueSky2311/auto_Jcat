; Include the needed libraries
#include <MsgBoxConstants.au3>

Local $sFilePath = "C:\Users\Blue\Downloads\visual gene\VisualGeneDeveloper.exe"

; Start the application
Local $iPID = Run($sFilePath)

; Wait for the program to load
Sleep(10000) ; Adjust this value based on how long the program takes to load

; Activate the main window
WinActivate("[CLASS:VisualGeneDeveloper]")

; Now you can perform actions on the window
; For example, to click on a menu item, you can use the following code:
; ControlClick("[CLASS:VisualGeneDeveloper]", "", "[CLASS:MenuItem; TEXT:File]")
; ControlClick("[CLASS:VisualGeneDeveloper]", "", "[CLASS:MenuItem; TEXT:Import gene list]")
; ControlClick("[CLASS:VisualGeneDeveloper]", "", "[CLASS:MenuItem; TEXT:Fasta format]")
