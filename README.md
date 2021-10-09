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

RLZero was inspired by the amazing Pygame Zero but with the addition of 3d graphics. Since I've
been using it in the classroom the design has diverged a little.  It turns out
that 'zero boilerplate', in the sense of making the program as short as it can possibly be, is not actually most
conducive to learning.  Sometimes being explicit rather than implicit is good.

## Callbacks

PGZero is heavily based on asynchronous callbacks. The main advantage of this is you can get started without
writing a main loop. It also makes event processing and timers easier. (Well, easier in the sense of requiring less code.)
Conceptually a callback is quite an advanced concept, so the downside is that the student may learn how to use it but
won’t really understand how it works.  When asked to add code to an existing program, 
students frequently attempt to add multiple `update` functions, because
they don't understand what a function is, or why there can't be two functions with the same name, or why this
particular function is special.

I think it’s worth keeping the callbacks for use by beginners  especially as that lets us have a hidden (fairly complex)
main loop. But it should be possible for students to write their own main loops, and at some point we should encourage
this.

## Imports/runner

PGZero avoids the use of imports (and run method) by using its own runner to load and run the programs. This saves
two lines of boilerplate on each program. However the trade-off is pretty large:

* PGZero programs are not valid Python programs
* PGZero is only easy to set-up in the Mu Editor - elsewhere it’s a pain.
* Importing is a fundamental concept in almost every programming language so any student who goes beyond the basics will
  have to learn about it eventually.  Hiding it doesn’t do them any favours except save some typing on the first day.

For these reasons PGZero can optionally work using imports and without the runner. I think RLZero should default to th
other choice: require imports, but have a runner available for teachers that want to use it.

RlZero is intended to be the first step in a programming education. On the other hand, for a one off lesson with students who are never
going to actually learn to program, a runner would be better.

## File loading

Pygame zero loads data files without specifying the file extension or the directory containing the file. There’s little
harm in implementing this as a fallback to help those who need it to but I’ve seen students get quite confused by it.
With no file extension they don't see any difference between the file name and a variable name. So I’m
going to specify the full file path in the examples.

## Light weight, minimal wrapper

As much possible we should encourage the use of Raylib functions. There are some additions but I don’t want to maintain
a whole parallel hierarchy of enhanced versions of data types that already exist in Raylib. Eventually students should
be able to use pure Raylib and Implement their own versions of sprite classes, etc. And our implementations should try
to be simple enough they could be pasted into a pure Raylib program if needed.

## Strings

PGZero automatically converts strings to colours.  This confuses students about why some colour names are
accepted and some are not.  And of course we can't do IDE autocompletion or checking on strings.
So we are using Color type constants instead.

PGZero weirdly *doesn't* use strings where it would make sense: when loading sound files.  Instead the file name
is read from a pseudo package name.  It reduces typing slightly, but conceptually makes it seem like the name is
part of the language, not a file on disk.  This is really getting into the territory of creating dynamic DSLs
like Ruby does, which is not Python-like.