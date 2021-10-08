# README

A simplified API for Raylib for use in education and to enable beginners to create 3d games.

Current state: 2d API is working and usable for education although may change a little before v1.0. 3d API is still in
flux.

## Use

```
pip3 install rlzero
```

RLZero is just a few classes that sit on top of Raylib. Once you have imported RLZero you automatically get all of
Raylib and you could copy any Raylib Python example code you find. Then if you want to use RLZero's classes as well as
Raylib you can.

The normal way of using RLZero is not to write your own main game loop. Instead, you set some variables to tell RLZero
how you'd like your game to be define some specially named methods.

**test.py**:

```python
from rlzero import *

WIDTH = 800
HEIGHT = 640
CAMERA = CAMERA_FIRST_PERSON
DATA_DIR = "examples/models/resources/models/"

cube = Cube((0, 10, 0), (10, 20, 10), BLUE)


def draw3d():
    clear()
    cube.draw()


def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100


run()
```

# Design notes

RLZero started out as "Pygame Zero + 3d" but the design has diverged since then.

## Callbacks

Pygame Zero is heavily based on asynchronous callbacks. The main advantage of this is you can get started without
writing a main loop. It also makes event processing and timers easier. Well, easier in the sense of requiring less code.
Conceptually a callback is quite an advanced concept, so the downside is that the student may learn how to use it but
won’t really understand how it works.

I think it’s worth keeping the callbacks for use by beginners , especially as that lets us have a hidden fairly complex
main loop. But it should be possible for students to write their own main loops, and at some point we should encourage
this.

## Imports/runner

Pygame Zero avoids the use of imports (and run method) by using its own runner to load and run the programs. This saves
two lines of boilerplate on each program. However the trade-off is pretty large:

* Pygame Zero programs are not valid Python programs
* Pygame Zero is only easy to setup in the Mu Editor - elsewhere it’s pain
* Importing is a fundamental concept in almost every programming language so any student who goes beyond helloworld will
  have to learn about it, so hiding it doesn’t do them any favours except save some typing.

For these reasons pygame zero can optionally work without the runner. I think RLZero should default to the other choice
of requiring imports, but have a runner available for teachers that want to use it.

RlZero is intended to be the first step in a programming education. For a one off lesson for students who are never
going to actually learn to program a runner would be better.

## File loading

Pygame zero loads data files without specifying the file extension or the directory containing the file. There’s little
harm in implementing this as a fallback to help those who need it to but I’ve seen students get quite confused by it so I’m
going to specify the full file path in the examples.

## Light weight, minimal wrapper

As much possible we should encourage the use of Raylib functions. There are some additions but I don’t want to maintain
a whole parallel hierarchy of enhanced versions of data types that already exist in Raylib. Eventually students should
be able to use pure Raylib and Implement their own versions of sprite classes, etc. And our implementations should try
to be simple enough they could be pasted into a pure Raylib program if needed.