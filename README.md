![image](image.png)#### CS 110
# Midterm - Python Programming

***

_Replace anything surrounded by the `< >` symbols._

## SUMMARY:
What did you clean up?:
* Collected some functions under a Dartboard class.
* Functions (methods) under the Dartboard class now uses the arguments passed to and initialized by the Dartboard class (e.g. circle radius), rather than individually hardcoded numbers.
* The Dartboard class creates its own window and turtle, which is reused for its functions (meaning the window and turtle do not have to be passed every time these functions/methods are called)
* In drawSquare(), replaced myturtle.goto() with drawLine(), and repetitive calculations in the arguments with two local variables.
* Replaced two calls to drawLine() in setUpDartboard() with one call to drawAxes()

Summary of function(s) added:
* The setCircle(circle_radius) method of the Dartboard class allows the user to set another radius for the circle.
* The clearBoard() method clears the drawings of the Turtle object created by the Dartboard object.
* The guessDart(guess) takes a guess of "hit" (landing in the circle) or "miss" (landing outside the circle) as an argument. If the guess is correct, it returns True. If it is incorrect, it returns False. Note that this is not very fun, as you are always more likely to land in the circle than outside it.
* The dartRandom() function allows you to throw a number of darts, then tells you how many hit. Not actually random, since darts are more likely to hit the dartboard than miss it. It's random in dart physics.
* The drawAxes() function draws symmetric x and y axes based on location and size.
* The hitBounds() function determines if a turtle object hits a boundary, and outputs which boundary it hit (directional wall, or a corner).
* The screenSaver() functions takes a turtle and bounces symmetrically around a defined area, and traces a line where it goes.

Summary of Feature Added:
* Added a screensaver through the screenSaver() function.
* The screenSaver() function uses the turtle belonging to the Dartboard object (at least the way it's called in main() ) and bounces it around a defined area.
* The screenSaver() function can also take other turtles and bounce it around custom-defined areas.
* If you leave the screenSaver() running for long enough, it makes a pretty satisfying pattern.


## KNOWN BUGS AND INCOMPLETE PARTS:
N/A

## REFERENCES:
* turtle documentation
* time documentation
* random documentation

## MISCELLANEOUS COMMENTS:
* The hitBounds() and screenSaver() function became more complicated because I had to account for not just hitting the walls, but hitting the corners. Hopefully the code is still readable.
