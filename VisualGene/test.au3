; Include the needed libraries
#include <MsgBoxConstants.au3>
#include <FileConstants.au3>
#include <Array.au3>

; Define the path to the CSV file
Local $sCSVFilePath = "C:\Users\Blue\Downloads\JCat_test.csv"

; Read the CSV file into an array
Local $aSequences
_FileReadToArray($sCSVFilePath, $aSequences)

; Loop through each sequence in the array
For $i = 1 To UBound($aSequences) - 1
    ; Split the line into an array
    Local $aLine = StringSplit($aSequences[$i], ",")

    ; Get the sequence from the line
    Local $sSequence = $aLine[6]

    ; Define the path to the application
    Local $sFilePath = "C:\Users\Blue\Downloads\visual gene\VisualGeneDeveloper.exe"

    ; Start the application
    Local $iPID = Run($sFilePath)

    ; Wait for the program to load
    Sleep(3000) ; Adjust this value based on how long the program takes to load

    ; Activate the main window
    WinActivate("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]")

    ; Change the text in the Text_Seq control
    ControlSetText("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]", "", "[NAME:Text_Seq]", $sSequence)

    ; Click on the "MainMenu" control
    ControlClick("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]", "", "[CLASS:WindowsForms10.Window.8.app.0.1ca0192_r8_ad1; INSTANCE:3]")

    ; Move the mouse to the specific position and click
    MouseClick("left", 107, 34, 1)

    ; Move the mouse to the new position and click
    MouseClick("left", 143, 300, 1)

    ; Click on the "ComboBox_TargetCodonUsage" control
    MouseClick("left", 916, 248, 1)

    ; Scroll the mouse wheel up 3 times
    MouseWheel("up", 3)

    ; Click on the "Ecoli K12" 
    MouseClick("left", 918, 296, 1)

    ; Click on the "Perform" 
    MouseClick("left", 614, 192, 1)

    ; Get the text from the Text_GCcontent control
    Local $sGCContent = ControlGetText("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]", "", "[NAME:Text_GCcontent]")

    ; Get the text from the Text_CAI1 control
    Local $sCAIValue = ControlGetText("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]", "", "[NAME:Text_CAI1]")

    ; Get the text from the Text_Nc control
    Local $sNcValue = ControlGetText("Visual Gene Developer 2.1  Build 797   [Untitled.vgd]", "", "[NAME:Text_Nc]")

    ; Define the path to the results file
    Local $sResultsFilePath = "C:\Users\Blue\Desktop\results.csv"

    ; Open the file for writing
    Local $hFile = FileOpen($sResultsFilePath, $FO_OVERWRITE)

    ; Check if the file opened successfully
    If $hFile = -1 Then
        MsgBox($MB_SYSTEMMODAL, "", "An error occurred while opening the file.")
        Exit
    EndIf

    ; Write the input sequence, optimized sequence, %GC content, CAI value, and Nc value to the file in CSV format
    FileWrite($hFile, "Input Sequence,Optimized Sequence,%GC Content,CAI Value,Nc Value" & @CRLF)
    FileWrite($hFile, $sSequence & "," & $sGCContent & "," & $sCAIValue & "," & $sNcValue & @CRLF)

    ; Close the file
    FileClose($hFile)

    ; Close the application
    ProcessClose($iPID)
Next