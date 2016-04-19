import tkinter as tk
from tkinter import *
import spotipy
import webbrowser
from PIL import Image, ImageTk
import os
from twitter import *
from io import BytesIO
import urllib.request
import urllib.parse
import PIL.Image
from PIL import ImageTk
import simplejson

song1 = "spotify:artist:58lV9VcRSjABbAbfWS6skp"
song2 = 'spotify:artist:0PFtn5NtBbbUNbU9EAmIWF'
song3 = 'spotify:artist:5INjqkS1o8h1imAzPqGZBb'
song4 = 'spotify:artist:1HwM5zlC5qNWhJtM00yXzG'
song5 = 'spotify:artist:4tZwfgrHOc3mvqYlEYSvVi'
song6 = 'spotify:artist:3AA28KZvwAUcZuOKwyblJQ'
song7 = 'spotify:artist:5T0MSzX9RC5NA6gAI6irSn'
song8 = 'spotify:artist:0SwO7SWeDHJijQ3XNS7xEE'
song9 = 'spotify:artist:1dWEYMPtNmvSVaDNLgB6NV'


    # Put in token, token_key, con_secret, con_secret_key
t = Twitter(
            auth=OAuth('705153959368007680-F5OUf8pvmOlXku1b7gpJPSAToqzV4Fb', 'bEGLkUJBziLc17EuKLTAMio8ChmFxP9aHYADwRXnxDsoC',
           'gYDgR8lcTGcVZS9ucuEIYsMuj', '1dwHsLDN2go3aleQ8Q2vcKRfLETc51ipsP8310ayizL2p3Ycii'))

numberOfTweets = 5

class SetUp(tk.Tk):  #inheriting
   def __init__(self, *args, **kwargs):  #method, initialisng

       tk.Tk.__init__(self, *args, **kwargs)

       tk.Tk.wm_iconbitmap(self, default="favicon.ico")

       container = tk.Frame(self) #container for holding everything
       container.pack(side = "top", fill = None, expand = False)
       container.pack_propagate(0) # don't shrink
       container.grid_rowconfigure(0, weight = 1)
       container.grid_columnconfigure(0, weight = 1)

       self.frames = {}  #dictionary of frames

       for F in (StartPage, RadioPage, MapPage, DataPage, InvPage, StatsPage): #loop through the number of pages

           frame = F(container, self)

           self.frames[F] = frame

           frame.grid(row = 0, column = 0, sticky = "nsew") #alignment plus stretch

       self.show_frame(StartPage)

   def show_frame(self, cont):

       frame = self.frames[cont]
       frame.tkraise() #raised to the front

   def music(self, uri):

       spotify = spotipy.Spotify()
       results = spotify.artist_top_tracks(uri)

       #getting the track and audio link to top song
       for track in results['tracks'][:1]:
          text2 = track['preview_url']

       return text2

   def showTweets(self, x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(self, text=line1 + "\n" + line2 + "\n\n")
        w.pack()

   def getTweets(self):

        x = t.statuses.home_timeline(screen_name="AndrewKLeech")
        return x


   def tweet(self):


        text = entryWidget.get().strip()
        if text == "":
            print("Empty")
        else:
            t.statuses.update(status=text)
            entryWidget.delete(0,END)
            print("working")


   def get_map(self,lat,lng):
       latString = str(lat)
       lngString = str(lng)
       #Map url from google maps, has marker and colors included
       url = ("https://maps.googleapis.com/maps/api/staticmap?center="+latString+","+lngString+"&size=500x500&zoom=16&style=feature:road.local%7Celement:geometry%7Ccolor:0x00ff00%7Cweight:1%7Cvisibility:on&style=feature:landscape%7Celement:geometry.fill%7Ccolor:0x000000%7Cvisibility:on&style=feature:landscape%7Celement:geometry.fill%7Ccolor:0x000000%7Cvisibility:on&style=feature:administrative%7Celement:labels%7Cweight:3.9%7Cvisibility:on%7Cinverse_lightness:true&style=feature:poi%7Cvisibility:simplified&markers=color:blue%7Clabel:H%7C"+latString+","+lngString+"&markers=size:tiny%7Ccolor:green%7CDelta+Junction,AK\&sensor=false")
       buffer = BytesIO(urllib.request.urlopen(url).read())
       pil_image = PIL.Image.open(buffer)
       tk_image = ImageTk.PhotoImage(pil_image)
       # put the image in program
       label = Label(self, image=tk_image)
       label.pack(padx=5, pady=5)
       mainloop()

   def get_coordinates(self,from_sensor=False):


      if entryWidget2.get().strip() == "":
         print("Empty")
      else:
         query=entryWidget2.get().strip()
         print("working")
         query = query.encode('utf-8')
         params = {
            'address': query,
            'sensor': "true" if from_sensor else "false"
         }
         #url used for google geocodeing api
         googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/json?'
         url = googleGeocodeUrl + urllib.parse.urlencode(params)
         json_response = urllib.request.urlopen(url)
         response = simplejson.loads(json_response.read())
         if response['results']:
            location = response['results'][0]['geometry']['location']
            latitude, longitude = location['lat'], location['lng']
            print(query, latitude, longitude)
         else:
            latitude, longitude = None, None
            print(query, "<no results>")
         self.get_map(latitude, longitude)


   def game(self):
       w, h = 500, 500

       # Pack pygame in `embed`.
       root = tk.Tk()
       embed = tk.Frame(root, width=w, height=h)
       embed.pack()

       # Tell pygame's SDL window which window ID to use
       os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

       # Show the window so it's assigned an ID.
       root.update()

       # Game for Pip-Boy
       # Imports
       import pygame
       import random

       # Initialise PyGame
       pygame.init()

       # Set display width and height
       display_width = 500
       display_height = 500

       # Create a gameDisplay using display_width and display_height
       gameDisplay = pygame.display.set_mode((display_width, display_height))

       # Set the caption of the window to Turret Defense
       pygame.display.set_caption('Tank War!')

       # Create colours using RGB values
       black = (0, 0, 0)
       green = (0, 150, 0)
       lightGreen = (0, 255, 0)

       # Create fonts
       smallFont = pygame.font.SysFont(None, 25)
       mediumFont = pygame.font.SysFont(None, 50)
       largeFont = pygame.font.SysFont(None, 75)

       # Initialise the clock for FPS
       clock = pygame.time.Clock()

       # Tank part dimensions
       tankWidth = 40
       tankHeight = 20
       turretWidth = 5
       wheelWidth = 5

       # Ground height
       ground = .85 * display_height

       # Load sounds
       fireSound = pygame.mixer.Sound("fireSound.wav")
       cannon = pygame.mixer.Sound("cannon.wav")

       def text_objects(text, color, size="smallFont"):  # Function returns text for blitting

           if size == "smallFont":
               textSurface = smallFont.render(text, True, color)
           if size == "mediumFont":
               textSurface = mediumFont.render(text, True, color)
           if size == "largeFont":
               textSurface = largeFont.render(text, True, color)

           return textSurface, textSurface.get_rect()

       def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight,
                          size="smallFont"):  # Blits text to button

           textSurface, textRect = text_objects(msg, color, size)
           textRect.center = ((buttonx + buttonwidth / 2), buttony + (buttonheight / 2))
           gameDisplay.blit(textSurface, textRect)

       def message_to_screen(msg, color, y_displace=0, size="smallFont"):  # Blits the text returned from text_objects

           textSurface, textRect = text_objects(msg, color, size)
           textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
           gameDisplay.blit(textSurface, textRect)

       def tank(x, y, turretPosition):  # Draws the tank and turret

           # Casting x and y to be ints
           x = int(x)
           y = int(y)

           # Set possible turret positions
           turrets = [(x - 27, y - 2),
                      (x - 26, y - 5),
                      (x - 25, y - 8),
                      (x - 23, y - 12),
                      (x - 20, y - 14),
                      (x - 18, y - 15),
                      (x - 15, y - 17),
                      (x - 13, y - 19),
                      (x - 11, y - 21)]

           # Draw the tank
           pygame.draw.circle(gameDisplay, green, (int(x), int(y)), 10)
           pygame.draw.rect(gameDisplay, green, (x - tankHeight, y, tankWidth, tankHeight))
           pygame.draw.line(gameDisplay, green, (x, y), turrets[turretPosition], turretWidth)

           # Draw the wheels
           pygame.draw.circle(gameDisplay, green, (x - 15, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x - 10, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x - 5, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 0, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 5, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 10, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 15, y + 20), wheelWidth)

           # Return the turret position
           return turrets[turretPosition]

       def enemyTank(x, y, turretPosition):  # Draws the tank and turret

           # Casting x and y to be ints
           x = int(x)
           y = int(y)

           # Set possible turret positions
           turrets = [(x + 27, y - 2),
                      (x + 26, y - 5),
                      (x + 25, y - 8),
                      (x + 23, y - 12),
                      (x + 20, y - 14),
                      (x + 18, y - 15),
                      (x + 15, y - 17),
                      (x + 13, y - 19),
                      (x + 11, y - 21)]

           # Draw the tank
           pygame.draw.circle(gameDisplay, green, (int(x), int(y)), 10)
           pygame.draw.rect(gameDisplay, green, (x - tankHeight, y, tankWidth, tankHeight))
           pygame.draw.line(gameDisplay, green, (x, y), turrets[turretPosition], turretWidth)

           pygame.draw.circle(gameDisplay, green, (x - 15, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x - 10, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x - 5, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 0, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 5, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 10, y + 20), wheelWidth)
           pygame.draw.circle(gameDisplay, green, (x + 15, y + 20), wheelWidth)

           return turrets[turretPosition]

       def explosion(x, y):  # Draws an explosion on screen

           # Play a sound
           pygame.mixer.Sound.play(fireSound)

           explode = True

           while explode:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()

               choices = [green, lightGreen]

               magnitude = 1

               while magnitude < 50:
                   explodeBitX = x + random.randrange(-1 * magnitude, magnitude)
                   explodeBitY = y + random.randrange(-1 * magnitude, magnitude)

                   if explodeBitY > ground + 13:
                       pygame.draw.circle(gameDisplay, black, (explodeBitX, explodeBitY), random.randrange(1, 5))

                   else:
                       pygame.draw.circle(gameDisplay, choices[random.randrange(0, 2)], (explodeBitX, explodeBitY),
                                          random.randrange(1, 5))

                   magnitude += 1

                   pygame.display.update()
                   clock.tick(100)

               explode = False

       def fire(pos, turretPos, gunPower, enemyTankX,
                enemyTankY):  # Function for shooting and controlling bullet physics

           # Play a sound
           pygame.mixer.Sound.play(cannon)

           damage = 0

           fire = True

           startingPos = list(pos)

           while fire:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()

               pygame.draw.circle(gameDisplay, green, (startingPos[0], startingPos[1]), 5)

               startingPos[0] -= (10 - turretPos) * 2

               startingPos[1] += int((((startingPos[0] - pos[0]) * .015 / (gunPower / 50)) ** 2) - (
               turretPos + turretPos / (12 - turretPos)))

               # If the explosion is on the ground
               if startingPos[1] > ground:

                   hitX = int((startingPos[0]))
                   hitY = int(startingPos[1])

                   # If the explosion hits the tank
                   # Various damages for how close it was
                   if enemyTankX + 10 > hitX > enemyTankX - 10:
                       damage = 25

                   elif enemyTankX + 15 > hitX > enemyTankX - 15:
                       damage = 20

                   elif enemyTankX + 20 > hitX > enemyTankX - 20:
                       damage = 15

                   elif enemyTankX + 30 > hitX > enemyTankX - 30:
                       damage = 5

                   explosion(hitX, hitY)

                   fire = False

               pygame.display.update()
               clock.tick(60)

           return damage

       def enemyFire(pos, turretPos, gunPower, playerX,
                     playerY):  # Function for shooting and controlling bullet physics

           # Play a sound
           pygame.mixer.Sound.play(cannon)

           damage = 0
           currentPower = 1
           powerFound = False

           # How the AI decides what power to uses
           while not powerFound:

               currentPower += 1
               if currentPower > 100:
                   powerFound = True

               fire = True

               startingPos = list(pos)

               while fire:
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()

                   startingPos[0] += (10 - turretPos) * 2

                   # Make currentPower random between 80% and 120% of the chosen power
                   gunPower = random.randrange(int(currentPower * .8), int(currentPower * 1.2))

                   startingPos[1] += int((((startingPos[0] - pos[0]) * .015 / (gunPower / 50)) ** 2) - (
                   turretPos + turretPos / (12 - turretPos)))

                   # If the explosion is on the ground
                   if startingPos[1] > ground:

                       hitX = int((startingPos[0]))
                       hitY = int(startingPos[1])

                       if playerX + 15 > hitX > playerX - 15:
                           powerFound = True

                       fire = False

           fire = True
           startingPos = list(pos)

           # When the power is decided, it shoots
           while fire:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()

               pygame.draw.circle(gameDisplay, green, (startingPos[0], startingPos[1]), 5)

               startingPos[0] += (10 - turretPos) * 2

               startingPos[1] += int((((startingPos[0] - pos[0]) * .015 / (gunPower / 50)) ** 2) - (
               turretPos + turretPos / (12 - turretPos)))

               # If the explosion is on the ground
               if startingPos[1] > ground:

                   hitX = int((startingPos[0]))
                   hitY = int(startingPos[1])

                   # If the explosion hits the tank
                   # Various damages for how close it was
                   if playerX + 10 > hitX > playerX - 10:
                       damage = 25

                   elif playerX + 15 > hitX > playerX - 15:
                       damage = 20

                   elif playerX + 20 > hitX > playerX - 20:
                       damage = 15

                   elif playerX + 30 > hitX > playerX - 30:
                       damage = 5

                   explosion(hitX, hitY)

                   fire = False

               pygame.display.update()
               clock.tick(60)

           return damage

       def power(level):  # Blits the power level

           text = smallFont.render("Power: " + str(level) + "%", True, green)
           gameDisplay.blit(text, [display_width * .75, 10])

       def game_controls():  # Function for controls screen

           controls = True

           while controls:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()

               gameDisplay.fill(black)
               message_to_screen("Controls!", green, -100, size="largeFont")
               message_to_screen("Left and right arrow keys to move the tank!", green, 10, size="smallFont")
               message_to_screen("Up and down arrow keys to move the tank's turret!", green, 40, size="smallFont")
               message_to_screen("A  and D keys change the turret's power!", green, 70, size="smallFont")
               message_to_screen("P to pause the game!", green, 100, size="smallFont")

               # Buttons
               button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
               button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

               pygame.display.update()
               clock.tick(15)

       def button(text, x, y, width, height, colour, active_colour,
                  action):  # Creates the button, both active and inactive

           cursor = pygame.mouse.get_pos()
           click = pygame.mouse.get_pressed()

           if x + width > cursor[0] > x and y + height > cursor[1] > y:
               pygame.draw.rect(gameDisplay, active_colour, (x, y, width, height))
               if click[0] == 1 and action != None:
                   if action == "play":
                       gameLoop()

                   if action == "controls":
                       game_controls()

                   if action == "quit":
                       pygame.quit()
                       quit()
           else:
               pygame.draw.rect(gameDisplay, colour, (x, y, width, height))

           text_to_button(text, black, x, y, width, height)

       def pause():  # Pauses the game

           paused = True

           message_to_screen("Paused", green, -225, size="largeFont")
           message_to_screen("C to continue playing", green, -175, size="smallFont")
           message_to_screen("Q to quit", green, -150, size="smallFont")
           pygame.display.update()
           while paused:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()

                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_c:
                           paused = False

                       elif event.key == pygame.K_q:
                           pygame.quit()
                           quit()

               clock.tick(5)

       def game_intro():  # Function for game introduction screen

           intro = True

           while intro:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()

               gameDisplay.fill(black)
               message_to_screen("Tank War!", green, -200, size="largeFont")
               message_to_screen("Kill the enemy tank before it kills you!", green, -50, size="smallFont")
               message_to_screen("Press play to play!", green, 0, size="smallFont")
               message_to_screen("Press controls to view the game's controls!", green, 50, size="smallFont")
               message_to_screen("Press quit to exit the game!", green, 100, size="smallFont")

               # Text on the buttons
               button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
               button("Controls", 200, 400, 100, 50, green, lightGreen, action="controls")
               button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

               pygame.display.update()
               clock.tick(15)

       def gameWin():  # Function for game introduction screen

           win = True

           while win:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()

               gameDisplay.fill(black)
               message_to_screen("You won!", green, -100, size="largeFont")
               message_to_screen("Your enemy's tank was destroyed!", green, 0, size="smallFont")
               message_to_screen("Replay to replay or quit to quit!", green, 100, size="smallFont")

               # Text on the buttons
               button("Replay", 25, 400, 100, 50, green, lightGreen, action="play")
               button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

               pygame.display.update()
               clock.tick(15)

       def over():  # Function for game introduction screen

           over = True

           while over:
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       quit()

               gameDisplay.fill(black)
               message_to_screen("Game over!", green, -100, size="largeFont")
               message_to_screen("Your tank was destroyed!", green, 0, size="smallFont")
               message_to_screen("Replay to replay or quit to quit!", green, 100, size="smallFont")

               # Text on the buttons
               button("Replay", 25, 400, 100, 50, green, lightGreen, action="play")
               button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

               pygame.display.update()
               clock.tick(15)

       def health(playerHealth, enemyHealth, pX, eX):  # Health bars

           # Player health
           if playerHealth > 50:
               playerColour = lightGreen
           else:
               playerColour = green

           # Enemy health
           if enemyHealth > 50:
               enemyColour = lightGreen
           else:
               enemyColour = green

           # Draw the health bars
           pygame.draw.rect(gameDisplay, playerColour, (pX - 100, display_height * .7, playerHealth, 10))
           pygame.draw.rect(gameDisplay, enemyColour, (eX, display_height * .7, enemyHealth, 10))

       def gameLoop():  # Main game loop

           gameExit = False
           gameOver = False

           FPS = 15

           # Tank positioning
           mainTankX = display_width * .8
           mainTankY = display_height * .8
           tankMove = 0
           curTurretPosition = 0
           changeTurretPosition = 0

           # Fire power
           firePower = 50
           change = 0

           # enemyTank positioning
           enemyTankX = display_width * .2
           enemyTankY = display_height * .8
           tankMove = 0

           # Health
           playerHealth = 100
           enemyHealth = 100

           while not gameExit:
               if gameOver == True:
                   pygame.display.update()
                   while gameOver == True:
                       for event in pygame.event.get():
                           if event.type == pygame.QUIT:
                               gameExit = True
                               gameOver = False

               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       gameExit = True

                   # Movement for tank
                   if event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_LEFT:
                           tankMove = -5

                       elif event.key == pygame.K_RIGHT:
                           tankMove = 5

                       elif event.key == pygame.K_UP:
                           changeTurretPosition = 1

                       elif event.key == pygame.K_DOWN:
                           changeTurretPosition = -1

                       elif event.key == pygame.K_p:
                           pause()

                       elif event.key == pygame.K_SPACE:
                           # Player's shot
                           damage = fire(bullet, curTurretPosition, firePower, enemyTankX, enemyTankY)
                           enemyHealth -= damage

                           # Enemy moves
                           movements = ['f', 'b']
                           move = random.randrange(0, 2)

                           for x in range(random.randrange(0, 10)):
                               if display_width * .33 > enemyTankX > display_width * .05:
                                   if movements[move] == "f":
                                       enemyTankX += 5
                                   elif movements[move] == "r":
                                       enemyTankX -= 5

                                   # If the tank moves, re draw the screen
                                   gameDisplay.fill(black)
                                   health(playerHealth, enemyHealth, pX, eX)
                                   bullet = tank(mainTankX, mainTankY, curTurretPosition)
                                   enemyBullet = enemyTank(enemyTankX, enemyTankY, 8)
                                   pygame.draw.rect(gameDisplay, green, (0, ground, display_width, 10))
                                   pygame.display.update()
                                   clock.tick(FPS)

                           # Enemy's shot
                           damage = enemyFire(enemyBullet, 8, 33, mainTankX, mainTankY)
                           playerHealth -= damage

                       elif event.key == pygame.K_a:
                           change = -1

                       elif event.key == pygame.K_d:
                           change = 1

                   # If user stops pressing the button, stop moving the tank
                   elif event.type == pygame.KEYUP:
                       if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                           tankMove = 0

                       if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                           changeTurretPosition = 0

                       if event.key == pygame.K_a or event.key == pygame.K_d:
                           change = 0

               # Draw the game screen
               mainTankX += tankMove
               pX = mainTankX
               eX = enemyTankX
               gameDisplay.fill(black)
               health(playerHealth, enemyHealth, pX, eX)
               bullet = tank(mainTankX, mainTankY, curTurretPosition)
               enemyBullet = enemyTank(enemyTankX, enemyTankY, 8)
               pygame.draw.rect(gameDisplay, green, (0, ground, display_width, 10))

               # Change power of the bullet
               firePower += change

               if firePower <= 1:
                   firePower = 1

               if firePower >= 100:
                   firePower = 100

               power(firePower)

               # Check if gameOver or gameWin
               if playerHealth < 1:
                   over()

               elif enemyHealth < 1:
                   gameWin()

               # Turret positioning
               curTurretPosition += changeTurretPosition
               if curTurretPosition > 8:
                   curTurretPosition = 8
               elif curTurretPosition < 0:
                   curTurretPosition = 0

               # Avoid tank and walls collision
               if mainTankX > display_width:
                   mainTankX -= 5

               if mainTankX < display_width * .66:
                   mainTankX += 5

               pygame.display.update()
               clock.tick(FPS)

           pygame.quit()
           quit()

       game_intro()
       gameLoop()


class StartPage(tk.Frame):

   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       image = Image.open("Pip Boy Images\mrPip.gif")
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white", height = 40, width = 40)
       label.image = photo #keeping refrence
       label.pack(side = BOTTOM, padx = 10, pady = 10)

       #to make width for now
       label = tk.Label(self, width = 60, bg = "black")
       label.pack(side = BOTTOM, pady = 120)


class RadioPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

        #opening images for buttons

       bonjovi1 = Image.open("coverart\Bonjovi.gif")
       bonjovi = ImageTk.PhotoImage(bonjovi1)

       toto1 = Image.open("coverart\Toto.gif")
       toto = ImageTk.PhotoImage(toto1)

       tameimpala1 = Image.open("coverart\Tameimpala.gif")
       tameimpala = ImageTk.PhotoImage(tameimpala1)

       dmx1 = Image.open("coverart\Dmx.gif")
       dmx = ImageTk.PhotoImage(dmx1)

       daftpunk1 = Image.open("coverart\Daftpunk.gif")
       daftpunk = ImageTk.PhotoImage(daftpunk1)

       gorrillaz1 = Image.open("coverart\Gorrillaz.gif")
       gorrillaz = ImageTk.PhotoImage(gorrillaz1)

       estelle1 = Image.open("coverart\estelle.gif")
       estelle = ImageTk.PhotoImage(estelle1)

       mgmt1 = Image.open("coverart\Mgmt.gif")
       mgmt = ImageTk.PhotoImage(mgmt1)

       saintmotel1 = Image.open("coverart\Saintmotel.gif")
       saintmotel = ImageTk.PhotoImage(saintmotel1)

       music1 = tk.Button(self, image = bonjovi, fg = "white", bg = "black", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song1)))
       music1.image = bonjovi #keeping refrence
       music1.place(x = 70, y = 70)

       music2 = tk.Button(self, image = toto, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song2)))
       music2.image = toto
       music2.place(x = 70, y = 145)

       music3 = tk.Button(self, image = tameimpala, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song3)))
       music3.image = tameimpala
       music3.place(x = 70, y = 220)

       music4 = tk.Button(self, image = dmx, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song4)))
       music4.image = dmx
       music4.place(x = 175 , y = 70)

       music5 = tk.Button(self, image = daftpunk, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song5)))
       music5.image = daftpunk
       music5.place( x = 175 , y = 145)

       music6 = tk.Button(self, image = gorrillaz, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song6)))
       music6.image = gorrillaz
       music6.place(x = 175, y = 220)

       music7 = tk.Button(self, image = estelle, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song7)))
       music7.image = estelle
       music7.place(x = 280, y = 70)

       music8 = tk.Button(self, image = mgmt, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song8)))
       music8.image = mgmt
       music8.place(x = 280, y = 145)

       music9 = tk.Button(self, image = saintmotel, bg = "black", fg = "white", cursor = "hand2", width = 75, height = 75,
                          command = lambda: webbrowser.open_new(controller.music(song9)))
       music9.image = saintmotel
       music9.place(x = 280, y = 220)


class MapPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       label = tk.Label(self, text = "map functionality", bg = "black", fg = "white")
       label.pack(side = BOTTOM)
       global entryWidget2
       # Create a text frame to hold the text Label and the Entry widget
       textFrame = Frame(self)
       #Create a Label in textFrame
       entryLabel = Label(textFrame)
       entryLabel["text"] = "Where are you?"
       entryLabel.pack(side=LEFT)
       # Create an Entry Widget in textFrame
       entryWidget2 = Entry(textFrame)
       entryWidget2["width"] = 50
       entryWidget2.pack(side=LEFT)
       textFrame.pack()
       button = Button(self, text="Submit", command=controller.get_coordinates)
       button.pack()




class DataPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       global entryWidget
       #Create a Label in textFrame
       controller.showTweets(controller.getTweets(), numberOfTweets)
       entryLabel = Label(self)
       entryLabel["text"] = "Make a new Tweet:"
       entryLabel.pack(side = LEFT)
       # Create an Entry Widget in textFrame
       entryWidget = Entry(self)
       entryWidget["width"] = 50
       entryWidget.pack(side=LEFT)
       button = Button(self, text="Submit", command = controller.tweet)
       button.pack()



class InvPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)


class StatsPage(tk.Frame):
   def __init__(self, parent, controller):

       tk.Frame.__init__(self, parent)
       tk.Frame.configure(self, bg = "black")

       radio = tk.Button(self, text ="RADIO", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(RadioPage))
       radio.place(x = 15, y = 0)

       map = tk.Button(self, text ="MAP", bg="black", fg="green", width = 10,
                       command = lambda: controller.show_frame(MapPage))
       map.place(x = 95, y = 0)

       data = tk.Button(self, text="DATA", bg="black", fg="green", width = 10,
                        command = lambda: controller.show_frame(DataPage))
       data.place(x = 175, y = 0)

       inv = tk.Button(self, text ="INV", bg="black", fg="green", width = 10,
                       command = lambda: controller.game())
       inv.place(x = 255, y = 0)

       stats = tk.Button(self, text ="STATS", bg="black", fg="green", width = 10,
                         command = lambda: controller.show_frame(StatsPage))
       stats.place(x = 335, y = 0)

       #new buttons

       strength = tk.Button(self, text ="STRENGTH", bg="black", fg="green", width = 20,
                            command = lambda: self.ImageShow("Pip Boy Images\Strength.gif"))
       strength.place(x = 35, y = 50)

       perception = tk.Button(self, text ="PERCEPTION", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Perception.gif"))
       perception.place(x = 35, y = 75)

       endurance = tk.Button(self, text ="ENDURANCE", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Endurance.gif"))
       endurance.place(x = 35, y = 100)

       charisma = tk.Button(self, text ="CHARISMA", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Charisma.gif"))
       charisma.place(x = 35, y = 125)

       intelligence = tk.Button(self, text ="INTELLIGENCE", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Intelligence.gif"))
       intelligence.place(x = 35, y = 150)

       agility = tk.Button(self, text ="AGILITY", bg="black", fg="green", width = 20,
                              command = lambda: self.ImageShow("Pip Boy Images\Agility.gif"))
       agility.place(x = 35, y = 175)

       luck = tk.Button(self, text ="LUCK", bg="black", fg="green", width = 20,
                        command = lambda: self.ImageShow("Pip Boy Images\Luck.gif"))
       luck.place(x = 35, y = 200)


   def ImageShow(self, path):

       label = tk.Label(self, bg = "black",  width = 40, height = 40)
       label.place(x = 215, y = 75)

       image = Image.open(path)
       photo = ImageTk.PhotoImage(image)

       label = tk.Label(self, image = photo, bg = "black", fg = "white")
       label.image = photo #keeping refrence
       label.place(x = 200, y = 75)



app = SetUp()
app.mainloop()