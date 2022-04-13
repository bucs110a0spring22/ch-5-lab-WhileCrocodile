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
import time

#########################################################
#                   Your Code Goes Below                #
#########################################################
def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
  '''
  Draws a square.
  
  args:
    myturtle: (turtle.Turtle) a turtle object
    width: (int) width of the square
    top_left_x: (int) x coordinate of top left corner
    top_right_y: (int) y coordinate of top left corner
  '''
  top_right_x = top_left_x+width
  bottom_right_y = top_left_y-width
  drawLine(myturtle, top_left_x, top_left_y, top_right_x, top_left_y)
  drawLine(myturtle, top_right_x, top_left_y, top_right_x, bottom_right_y)
  drawLine(myturtle, top_right_x, bottom_right_y, top_left_x, bottom_right_y)
  drawLine(myturtle, top_left_x, bottom_right_y, top_left_x, top_left_y)
  

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
  '''
  Draws a line from point A to point B.
  
  args:
    myturtle: (turtle.Turtle) a turtle object
    x_start: (int) x coordinate of starting point
    y_start: (int) y coordinate of starting point
    x_end: (int) x coordinate of ending point
    y_end: (int) y coordinate of ending point
  '''
  myturtle.penup()
  myturtle.goto(x_start, y_start)
  myturtle.pendown()
  myturtle.goto(x_end, y_end)
  

def drawCircle(myturtle=None, radius=0, resolution = 100):
  '''
  Draws a circle from the bottom up.
  
  args:
    myturtle: (turtle.Turtle) a turtle object
    radius: (int) radius of the drawn circle
    resolution: (int) how many lines the turtle uses to draw the circle
  '''
  myturtle.pendown()
  myturtle.circle(radius, steps=resolution)


def drawAxes(myturtle=None, axis_width=1, origin_x=0, origin_y=0):
  '''
  Draws x and y axes centered at a defined origin.
  
  args:
    myturtle: (turtle.Turtle) a turtle object
    axis_width: (int) length of one end of an axis to the other end
    origin_x: (int) x coordinate of the origin
    origin_y: (int) y coordinate of the origin
  '''
  upper_xy = axis_width/2
  lower_xy = -axis_width/2
  drawLine(myturtle, x_start=lower_xy, y_start=origin_y, x_end=upper_xy, y_end=origin_y)
  drawLine(myturtle, x_start=origin_x, y_start=lower_xy, x_end=origin_x, y_end=upper_xy)


def hitBounds(myturtle=None, wn_height=10, wn_width=10):
  '''
  Determines if a turtle hits the boundary of a set area, and 
  returns a hit in the format "hit_{bottom/top}{left/right}_bound",
  e.g. "hit_bottom_bound" or "hit_topright_bound"
  
  args:
    myturtle: (turtle.Turtle) a turtle object
    wn_height: (int) height of bound area
    wn_width: (int) width of bound area

  return:
    False: (bool) turtle did not hit a bound
    f"hit_{vertical}{horizontal}_bound": (str) turtle hit a bound
  '''
  right_bound = wn_width/2
  left_bound = -right_bound
  top_bound = wn_height/2
  bottom_bound = -top_bound
  vertical = ""
  horizontal = ""
  
  if myturtle.xcor() <= left_bound:
    horizontal = "left"
  elif myturtle.xcor() >= right_bound:
    horizontal = "right"
  
  if myturtle.ycor() <= bottom_bound:
    vertical = "bottom"
  elif myturtle.ycor() >= top_bound:
    vertical = "top"
  
  if vertical == "" and horizontal == "":
    return False
  else:
    return f"hit_{vertical}{horizontal}_bound"


def screenSaver(duration = 30, myturtle = None, wn_height = 20, wn_width = 20):
  '''
  Bounces a turtle around a set area for a specified duration, and traces
  a line across the trajectory.

  args:
    duration: (int) time the function will run
    myturtle: (turtle.Turtle) a turtle object to be bounced
    wn_height: (int) height of bound area
    wn_width: (int) width of bound area
  '''
  # Keeps track of time passed by comparing the current
  # time to the time the function is meant to end
  time_start = int(time.time())
  time_end = time_start + duration
  time_now = int(time.time())
  # Makes sure the length of one step does not exceed the
  # width of the window
  step_length = wn_width/100
  # Move to origin and spin to face random direction
  myturtle.penup()
  myturtle.goto(0,0)
  myturtle.pendown()
  myturtle.setheading(random.randrange(-180, 181))
  # Determines the angle of the turtle's trajectory 
  # through its last position, then reflects the trajectory based on
  # which boundary it hit. If the turtle hits a corner,
  # the trajectory isn't reflected, but flipped 180.
  while time_end > time_now:
    last_pos = myturtle.pos()
    myturtle.forward(step_length)
    angle = myturtle.towards(last_pos) + 180
    bound_hit = hitBounds(myturtle, wn_height, wn_width)
    if bound_hit == "hit_topleft_bound" or bound_hit == "hit_topright_bound" or bound_hit == "hit_bottomleft_bound" or bound_hit == "hit_bottomright_bound":
      myturtle.setheading(angle + 180)
    elif bound_hit == "hit_left_bound" or bound_hit == "hit_right_bound":
      myturtle.setheading(-angle + 180)
    elif bound_hit == "hit_top_bound" or bound_hit == "hit_bottom_bound":
      myturtle.setheading(-angle)
    time_now = int(time.time())
  

class Dartboard:
  def __init__(self, circle_radius=1):
    '''
    Initialize the Dartboard object.
    
    args:
    circle_radius: (int) radius of dartboard
    '''
    self.myturtle = turtle.Turtle()
    self.myturtle.speed(0)
    self.window = turtle.Screen()
    self.circle_radius = circle_radius
    
  
  def setCircle(self, circle_radius=1):
    '''
    Set a new circle radius.
    '''
    self.circle_radius = circle_radius
    
  
  def setUpDartboard(self):
    '''
    Sets up a window for use by the Dartboard.
    '''
    originxy = 0                          # Because the dartboard is a square,
    urxy = self.circle_radius             # the upper right and lower left
    llxy  = -self.circle_radius           # points will have x and y points 
    square_width = self.circle_radius*2   # of equal values (e.g. (1, 1))
  
    self.window.setworldcoordinates(llxy, llxy, urxy, urxy)
    drawSquare(self.myturtle, square_width, top_left_x=llxy, top_left_y=urxy)
    drawAxes(self.myturtle, axis_width=square_width, origin_x=originxy, origin_y=originxy)
    self.myturtle.goto(x=originxy,y=llxy)                           
    drawCircle(self.myturtle, radius=self.circle_radius)

  
  def clearDartboard(self):
    '''
    Clear the Dartboard window.
    '''
    self.myturtle.clear()
    
 
  def isInCircle(self):
    '''
    Checks if the turtle used by the Dartboard is within the
    dartboard circle.

    return:
      return: (bool) True if in circle, False if not
    '''
    return self.myturtle.distance(0, 0) <= self.circle_radius

  
  def throwDart(self):
    '''
    Throws a dart that is blue if it hits the dartboard, and red if it misses
    '''
    dot_x = random.uniform(-self.circle_radius, self.circle_radius)
    dot_y = random.uniform(-self.circle_radius, self.circle_radius)
    self.myturtle.penup()
    self.myturtle.goto(dot_x, dot_y)
    if self.isInCircle():
      self.myturtle.color("blue")
      self.myturtle.stamp()
    else:
      self.myturtle.color("red")
      self.myturtle.stamp()
    self.myturtle.color("black")

  
  def dartGuess(self, guess = "hit"):      # Throws dart and lets user guess
    '''
    Throws a dart, and checks if its hit/miss is the same as the guess.

    args:
      guess: (string) "hit" or "miss"

    return: 
      return: (bool) True if guess is same as dart, False if not
    '''
    self.throwDart()                       # if the dart hit
    if guess == "hit":
      return self.isInCircle() == True
    if guess == "miss":
      return self.isInCircle() == False

  
  def dartRandom(self, throws = 10):
    '''
    Throws a number of darts, and says how many hit.
    
    args:
      throws: (int) number of thrown darts  

    return:
      hit: (int) number of darts hitting the board
    '''
    hit = 0
    for throws in range(throws):
      self.throwDart()
      if self.isInCircle() == True:
        hit += 1
    return hit
    
  
  def playDarts(self, rounds=10):
    '''
    Simulates a dart game between two players, and announces the winner.

    args:
      rounds: (int) number of rounds played
    '''
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
    '''
    Performs a monte pi simulation to approximate pi.

    args:
    num_darts: (int) number of darts thrown in the simulation

    return:
      approx_pi: (float) calculated approximation of pi
    '''
    inside_count = 0
    for i in range(num_darts):
      self.throwDart()
      if self.isInCircle():
        inside_count += 1
    approx_pi = (inside_count / num_darts) * 4
    return approx_pi
  
############################################################################
### The first half of main() is just the original code rewritten         ###
### to work with the Dartboard class. The second half is original code,  ###
### written to demonstrate new features (e.g. the Dartboard class)       ###
############################################################################

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
  dartboard.setUpDartboard()
  
  # Loop for 10 darts to test your code
  for i in range(10):
      dartboard.throwDart()
  print("\tPart A Complete...")
  print("=========== Part B ===========")
  dartboard.clearDartboard()
  dartboard.setUpDartboard()
  dartboard.playDarts()
  print("\tPart B Complete...")
  # Keep the window up until dismissed
  print("=========== Part C ===========")
  dartboard.clearDartboard()
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

  #############################################
  ### Everything past this point is new code ##
  #############################################
  print("\n========== Midterm  ==========")      
  dartboard.window.tracer(1)
  dartboard.clearDartboard()               # This shows that the dartboard
  dartboard.setCircle(10)                  # functions the same even with
  print("Redrawing dartboard with new radius 10...") # a new radius
  dartboard.setUpDartboard()
  print("Replaying dart game...")
  dartboard.playDarts()
  print("\nThrowing random darts...")
  randomThrows = int(input("How many darts would you like to throw? "))
  randomHit = dartboard.dartRandom(randomThrows)
  print(f"{randomHit} darts hit!")

  print("\nPlaying guessing game...")
  myguess = str(input("Hit or miss?\n"))
  myguess = myguess.lower()
  if dartboard.dartGuess(myguess) == True:
    if myguess == "hit":
      print("\nCorrect! The dart hit.")
    else:
      print("\nCorrect! The dart missed.")
  else:
    if myguess == "hit":
      print("\nIncorrect! The dart missed.")
    else:
      print("\nIncorrect! The dart hit.")
  
  screensaver_time = int(input("How many seconds would you like to play the screensaver for? "))
  print(f"\nBeginning Screensaver for {screensaver_time} seconds...")
  dartboard.clearDartboard()
  drawSquare(dartboard.myturtle, width=dartboard.circle_radius*2, top_left_x=-dartboard.circle_radius, top_left_y=dartboard.circle_radius)
  screenSaver(duration=screensaver_time, myturtle=dartboard.myturtle, wn_height=dartboard.circle_radius*2, wn_width = dartboard.circle_radius*2)
  print("Screensaver has completed...")
  print("\nThe program demo has concluded. \nThank you for your time!")
  dartboard.window.exitonclick()
main()
