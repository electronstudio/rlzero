# README

A simplified API for Raylib for use in education and to enable beginners to create 3d games.

Current state:

## Use

```
pip3 install rlzero
```

RLZero is just a few classes that sit on top of Raylib.  Once you have imported RLZero you automatically get all of Raylib
and you could copy any Raylib Python example code you find.  Then if you want to use RLZero's classes as well as Raylib you can.

The normal way of using RLZero is not to write your own main game loop.  Instead, you set some 
variables to tell RLZero  how you'd like
your game to be define some specially named methods.

**test.py**:
```python
WIDTH=800
HEIGHT=640
CAMERA=rl.CAMERA_FIRST_PERSON
DATA_DIR="examples/models/resources/models/"

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')

def draw():
    clear()
    cube.draw()

def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100
```

Then you tell RLZero to run your methods in its game loop:
    
    python -m rlzero test.py


All the runner module does it add this line to the top of your code:

```python
from rlzero import *
```

and this line to the bottom of your code:

```python
run()
```

So if you can't use the runner, you can do that manually.

## Differences from Pygame Zero

1. We don't have a special mode in the Mu editor like Pygame Zero does, and therefore it is necessary to add an `import` line to the start of
every program, and a `run()` line to the end.
   