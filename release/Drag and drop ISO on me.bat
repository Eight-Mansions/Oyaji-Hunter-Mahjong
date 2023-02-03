@echo off
set filename=Oyaji Hunter Mahjong - English v1.0
set file_type=ISO
set patch_file=Oyaji-Hunter-patch.xdelta

set found_disc=

pushd %~dp0
if "%~1"=="" goto :NOISO

:: Iterate over all files that get dragged onto here
for %%A in (%*) do (
    echo Patching %%A...
    echo:

    patch_data\xdelta.exe -d -f -s %%A "patch_data\%patch_file%" "%filename%.iso" 2>nul
    if not errorlevel 1 (
        set found_disc=true

        echo Original disc for "Oyaji Hunter Mahjong" found!
    )

)

if not defined found_disc goto :NOPATCHFOUND

echo Success!
echo:
echo ---
echo The following %file_type% file should have been created next to the bat file:
echo * %filename%.iso
echo ---
echo:
echo Load up the .iso file for the disc you wish to play and enjoy!
echo:
goto :EXIT

:NOISO
echo To patch %file_type% don't run this bat file.
echo Simply drag and drop %file_type% on it and the patch process will start.
goto :EXIT

:NOPATCHFOUND
echo No patch found suitable for those files.
echo Please make sure to drag in a clean ISO file of the original "Oyaji Hunter Mahjong".
echo:
echo If the problem persists, go throw a sad puppy at SnowyAria ; _;

:EXIT
popd
echo:
echo Press any key to close this window
pause >nul
exit
