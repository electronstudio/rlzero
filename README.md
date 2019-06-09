# Richlib PRE-ALPHA DO NOT USE YET

A simplified API for Raylib for use in education and to enable beginners to create 3d games

## Use

Richlib is just a few classes that sit on top of Raylib Python CFFI.  Once you have imported Richlib you automatically get all of raylib.static
and raylib.pyray
and you could just copy any Raylib Python example code you find.  Then if you want to use Richlib's classes as well as Raylib you can.

The normal way of using Richlib is not to write your own main game loop.  Instead, you set some variables to tell Richlib how you'd like
your game to be:

Then you define some specially named methods:

Then you tell Richlib to run your methods in its game loop:



## Differences from Pygame Zero

1. We don't have a special mode in the Mu editor like Pygame Zero does, and therefore it is necessary to add an `import` line to the start of
every program, and a `run()` line to the end.

2. The underlying API, Raylib, is not object oriented like Pygame is.  The stuff added by Richlib is object oriented but you
might notice there is no equivalent of the `screen` object because Raylib doesn't have one.

3. 3D games are inherently more complex than 2D, e.g. there is no equivalent of the camera object for the 2d programmer
to worry about.

4. To mitigate (3) as much as possible we do automate some stuff that you might expect to do manually in Pygame Zero.