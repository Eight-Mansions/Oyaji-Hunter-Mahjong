# Oyaji Hunter Mahjong English Translation
## Setup
1. Open `OperaFS [De]Compiler [EN].exe` in the tools folder.
2. Select decompile, find your copy of the game, then extract it to `cd/working`.

## Compiling changes
3DO is unfortunately not 1-click, but we get as close as we can.
1. Run `1-build.bat` to copy changes into the working folder.
2. Open `OperaFS [De]Compiler [EN].exe` in the tools folder.
    1. Select "Compile ISO"
    2. Select the `cd/working` folder. MAKE SURE to double click the folder to verify it's selected! You should see `AppStartup` and `BannerScreen` in the files list.
    3. Click "OK" then output it to the `cd` folder with the name "Oyaji Hunter Working.iso" You can also click an old version and overwrite it.
    4. There won't be any confirmation, but the window will be frozen until it's done. So you can shake the window and once it moves, you're good.
3. Run `3-sign-oyaji.bat` to sign the new iso with the right encryption key. This can be ignored if you use a hacked bios in your emulator, but it's so simple to do
