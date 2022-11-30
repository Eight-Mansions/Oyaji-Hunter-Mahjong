@echo off
set working_name=working

echo Clearing out the old files and creating a clean workspace...
del /s /q cd\%working_name%\* 1>nul
Xcopy /E /q cd\orig\ cd\%working_name%\ 1>nul
echo:

echo Converting all images to cels and inserting...
python tools\BMPToCEL.py images\ cd\working\
echo:

echo Converting bmp sprite sheets to anims...
python tools\BMPDirectoryToAnim.py anims anims_pre_process cd\working
::tools\BMPTo3DOAnim.exe 24 24 anims\SUB_TITLE01.bmp cd\working\jyanpai\AnimationData\sub_title\SUB_TITLE01.ANIM
echo:

echo Copying all subbed movies over...
copy movies\HunterMovie\* cd\%working_name%\HunterMovie 1>nul
echo:

pause