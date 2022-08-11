# conway's game of life

This repository contains a conways game of life developped in python, but currently the project is not actually optimized.

![](https://github.com/FACON-Nicolas/FACON-Nicolas/raw/main/resources/conways-py.gif)

#

# What the conway's game of life is ?

The conway's game of life is a cellular automate made by John Horton Conway in 1970. It's a complex game simulation dispite the easy rules.

The rules of the conway's game of life are very easy to understand, the game is composed by a grid of tiles called cells, each cells cans to have 2 differents states, dead or alive, and their state depend by the neighbors:

- **2 neighbors**: the cells' state doesn't change.
- **3 neighbors**: the cell's state become / stay alive
- **others**: the cell's state become / stay dead

![](https://www.researchgate.net/publication/339605473/figure/fig5/AS:869062565437443@1584212070801/Rules-of-Conways-Game-of-Life.png)

#

# Summary

* **[About](#What-the-conways-game-of-life-is)**
* **[Summary](#Summary)**
* **[Developers](#Developers)**
* **[Features](#Features)**
* **[pre-requisites](#Pre-requisites)**
* **[Install](#Install)**
* **[Inputs](#Inputs)**

#

# Developers

 * **[FACON Nicolas](www.github.com/FACON-Nicolas)** : creator of the project

#

# Features

+ Random Grid Generation
+ Clear Grid
+ Previous Step
+ Next Step
+ Pause / Resume

#

# Pre-requisites 

+ Windows
    - **[Python](https://www.python.org/downloads/)**
    - **[Git Bash](https://gitforwindows.org/)**
    - **pygame** (``py -3.8 -m pip install pygame`` in your terminal)
    - **pygame_gui** (``py -3.8 -m pip install pygame_gui`` in your terminal)

 + Linux:
 
    write this in terminal 
    ```sh
    #if python is not installed yet.
    sudo apt install python3.8
    #if pygame is not installed yet.
    pip install pygame
    #if pygame_gui is not installed yet.
    pip install pygame_gui
    ```

# 

# Install 

Write this in your terminal (or your Git Bash terminal).

```sh
git clone https://github.com/FACON-Nicolas/conways-life-game
cd Tetris/
#python3 or py on windows
python3 src/game.py
```

#

# Keys
<p>many buttons are presents in the window, but, some inputs can be used.</p>

| Key | Action |
|-----|--------|
| SPACE | launch the life |
| RIGHT | next step of the life |
| LEFT | last step of the life |

