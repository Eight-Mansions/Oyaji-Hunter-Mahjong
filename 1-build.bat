@echo off
set working_name=working

echo Clearing out the old files and create a clean workspace
del /s /q cd\%working_name%\* 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Convert all images to cels and insert
python tools\BMPToCEL.py images\ cd\working\
echo:

echo Convert bmp sprite sheets to anims
tools\BMPTo3DOAnim.exe 24 24 anims\SUB_TITLE01.bmp cd\working\jyanpai\AnimationData\sub_title\SUB_TITLE01.ANIM
echo:

pause