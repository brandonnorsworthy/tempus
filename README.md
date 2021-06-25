# tempus

`repository must be cloned down to function`

## About

This is a python "bot" that plays the MMORPG game *Old-School Runescape* this bot dynamically can connect to a BlueStacks Emulator Enviorment using a andriod development tool called ADB *Andriod Development Bridge* giving my bot the ability to simulate clicks without disturbing the mouse or anythin on the host machine so you can add as many instances of simultaneously running bots at the same time

![Demo Image](/assets/images/readme/demo_4_clients_connected.png)

## Installation

ADB Technically isn't a requirement because it is automatically in the repository but if you want a direct download you can [click here](https://dl.google.com/android/repository/platform-tools-latest-windows.zip).

To set up the script you also need to download **Python3** and **BlueStacks**

**BlueStacks Settings**
* First log into BlueStacks using the play store.
* Second go into the options and change the settings to **Resolution 960x540** and **DPI 240**
* The real resolution on your monitor is irrelevant so don't try just resizing the window that doesn't help with anything

## Running the Program

A user GUI has been implemented so you can just launch the **tempus.py** via command line `python tempus.py` in the file directory and everything should startup as normal.

## Currently Support

**Mining**
* South-West Varrock Iron Mine
* Web Walking to Varrock East Bank
* Multiple Clients can Connect

## Planned

### Finished

- Multiple clients can connect
- Nice GUI instead of calling scripts directly

### Current Focused Item

```
#TODO add basic UI so i dont have to type shit out
#TODO add more clarification to comments
#TODO call python script specifically for that emulator(port)
```

### Short-term

```
#TODO toggle the run off automatically on start
#TODO pick an action (in gui mining, walking something idk)
#TODO random circle ontop of randomness [multiple layers of randomness]
#TODO add area support to pixelSearch instead of a single pixel
#TODO add new capability walking to the bank from W varrock
#TODO add support for lumbridge tin and copper
#TODO add function for entering text from script
```

### Long-term

```
#TODO when sending RANDOM variables to a batch file format them to 1 decimal place #maximum [reduce memory sent == fast communication]
#TODO webwalker interface
#TODO shows where all the connected bots are on a map
#TODO front end web face for bot control
#TODO add support for connecting automatically
#TODO ADD BREAKS WATCH YOUTUBE VIDEO FOR TIMES [makes look like a human]
#TODO go one by one through functions and see if they can be more efficent or smaller
#TODO add support for SW varrock tin and copper
#TODO add option for either droping materials or banking them
#TODO add power woodcutting
#TODO add random ge purchases
#TODO add a distraction chance while performing a repetative action
#TODO "accidentally" click a random hotbar
#TODO move the camera around and then return it back
#TODO stop interacting for a random period of time up to ~5 minutes
```

## Copyright
All code has been written by Brandon Norsworthy Copyright @ 2020
