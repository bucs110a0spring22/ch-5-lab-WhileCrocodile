'''
Estimates pi using Monte Carlo simulation

Virtual Dartboard has area 2 X 2 to accommodate unit circle
Total area is 4
Therefore, since area of unit circle = pi * radius^2 (and radius of 1 squared
  is 1), ratio of area of unit circle to area of board should be pi/4
  Theoretically, if you fill the entire board with darts, counting
  the number of darts that fall within the circle divided by the
  total number of darts thrown should give us that ratio (i.e., 1/4 * pi)
  Therefore, multiplying that result by 4 should give us an approx. of pi

Output to monitor:
  approximation of pi (float)
Output to window:
  colored dots that simulate unit circle on 2x2 square
Functions you must implement:
  drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0) - to outline dartboard
  drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0) - to draw axes
  drawCircle(myturtle=None, radius=0) - to draw the circle
  setUpDartboard(myscreen=None, myturtle=None) - to set up the board using the above functions
  isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0) - determine if dot is in circle
  throwDart(myturtle=None)
  playDarts(myturtle=None) - a simulated game of darts between two players
  montePi(myturtle=None, num_darts=0) - simulation algorithm returns the approximation of pi
'''
import turtle
import random

#########################################################
#                   Your Code Goes Below                #
#########################################################
class Dartboard:
  def __init__(self, circle_radius=1):
    self.myturtle = turtle.Turtle()
    self.myturtle.speed(0)
    self.window = turtle.Screen()
    self.circle_radius = circle_radius
    
  def setCircle(self, circle_radius=1):  # Allows the user to set a new circle radius
    self.circle_radius = circle_radius
    
  def setUpDartboard(self):
    origin = 0
    urxy = self.circle_radius            # Because the dartboard is a square, the top right and bottom left
    llxy  = -self.circle_radius          # points will have x and y points of equal values (e.g. (1, 1))
    square_width = self.circle_radius*2
    
    self.window.setworldcoordinates(llxy, llxy, urxy, urxy)
    drawSquare(self.myturtle, square_width, top_left_x=llxy, top_left_y=urxy)
    drawLine(self.myturtle, x_start=llxy, y_start=origin, x_end=urxy, y_end=origin)
    drawLine(self.myturtle, x_start=origin, y_start=urxy, x_end=origin, y_end=llxy)
    self.myturtle.goto(x=origin,y=llxy)                           # Moves turtle to (0, -1) since the 
    drawCircle(self.myturtle, radius=self.circle_radius)          # circle is drawn from the bottom

  def isInCircle(self):
    return self.myturtle.distance(0, 0) <= self.circle_radius    # Assumes the circle is centered at (0, 0)

  def throwDart(self):
    dot_x = random.uniform(-1, 1)
    dot_y = random.uniform(-1, 1)
    self.myturtle.penup()
    self.myturtle.goto(dot_x, dot_y)
    if self.isInCircle():
      self.myturtle.color("blue")
      self.myturtle.stamp()
    else:
      self.myturtle.color("red")
      self.myturtle.stamp()
    self.myturtle.color("black")

  def playDarts(self, rounds = 10):
    player_one_points = 0
    player_two_points = 0
    for i in range(rounds):
      self.throwDart()
      if self.isInCircle():
        player_one_points += 1
      self.throwDart()
      if self.isInCircle():
        player_two_points +=1
    print("Player One:", player_one_points, "points.")
    print("Player Two:", player_two_points, "points.")
    if player_one_points > player_two_points:
      print("Player One won!")
    elif player_one_points < player_two_points:
      print("Player Two won!")
    else:
      print("It was a tie!")

  def montePi(self, num_darts=0): 
    inside_count = 0
    for i in range(num_darts):
      self.throwDart()
      if self.isInCircle():
        inside_count += 1
    approx_pi = (inside_count / num_darts) * 4
    return approx_pi
    
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  myturtle.penup()
  myturtle.goto(top_left_x, top_left_y)
  myturtle.pendown()
  myturtle.goto(top_left_x+width, top_left_y)
  myturtle.goto(top_left_x+width, top_left_y-width)
  myturtle.goto(top_left_x, top_left_y-width)
  myturtle.goto(top_left_x, top_left_y)
  myturtle.penup()
  
def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  myturtle.penup()
  myturtle.goto(x_start, y_start)
  myturtle.pendown()
  myturtle.goto(x_end, y_end)
  myturtle.penup()
  
def drawCircle(myturtle=None, radius=0, resolution = 100):
  myturtle.pendown()
  myturtle.circle(radius, steps=resolution)
  myturtle.penup()

#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################
def main():
    # Get number of darts for simulation from user
    # Note continuation character <\> so we don't go over 78 columns:
    print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
    print("=========== Part A ===========")

    # Creates a Dartboard object and sets it up
    dartboard = Dartboard()

    # Loop for 10 darts to test your code
    for i in range(10):
        dartboard.throwDart()
    print("\tPart A Complete...")
    print("=========== Part B ===========")
    dartboard.myturtle.clear()
    dartboard.setUpDartboard()
    dartboard.playDarts()
    print("\tPart B Complete...")
    # Keep the window up until dismissed
    print("=========== Part C ===========")
    dartboard.myturtle.clear()
    dartboard.setUpDartboard()
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
    BATCH_OF_DARTS = 5000
    dartboard.window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
    number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
    approx_pi = dartboard.montePi(number_darts)
    print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
    print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
    dartboard.window.exitonclick()

main()
