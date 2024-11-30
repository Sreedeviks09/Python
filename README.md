First Python Program
------------------------
1-Import the Turtle Library
-----------------------------
    --from turtle import *
       -- The turtle module is used to create graphics by controlling a virtual turtle.
          --  It provides functions to draw shapes, lines, and patterns.
2-Set the Speed
---------------------
   -- speed(0) 
        --The speed of the turtle is set to the fastest level (0), ensuring the pattern is drawn as quickly as possible.
3-Set the Background Color
-------------------------------
   -- bgcolor('black') 
    --  The background color of the canvas is set to black for high contrast with the drawing. 
4-Set the Pen Color 
---------------------------
    --color('yellow') 
     -- The turtle’s drawing color is set to yellow, which creates a bright and striking pattern against the black background. 
5-Start a Loop 
-----------------
  --  for i in range(160):
        --A loop is executed 160 times. 
            --The loop variable i is used to vary the angles and lengths, giving the pattern its dynamic, spiral-like shape.
6-Rotate the Turtle 
-----------------------
    --  rt(i) 
          --The turtle rotates to the right by i degrees. 
            --As i increases with each loop iteration, the turtle turns at progressively larger angles. 
8-Draw a Circular Arc
----------------------
    --circle(160, i) 
        --The turtle draws a partial circle (arc) with a radius of 160 units. 
            --The extent of the arc is determined by i, increasing as the loop progresses.
9-Move Forward 
-------------------
    ---fd(i) 
        ---The turtle moves forward by i units. 
          ------This creates the expanding spiral effect as the forward distance grows with each loop.
10-Rotate Again
------------------
    ---rt(90) 
      --The turtle rotates to the right by 90 degrees after each step, contributing to the angular, repetitive pattern.
11-Hide the Turtle
------------------------
        ---hideturtle() '
                --The turtle (cursor) is hidden once the drawing is complete, leaving just the design on the screen.
12-Keep the Window Open 
-----------------------
      --done() 
          ---Ensures the turtle graphics window remains open after the program finishes executing.

--Result The combination of these steps produces a mesmerizing spiral-like pattern with arcs and rotations. The increasing values of i make the design dynamic and intricate. The black background and yellow pen color enhance the visual appeal of the artwork.
