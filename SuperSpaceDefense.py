__author__ = 'elpython3'


import pygame # The module to make games.
import sys # To close the game without error output.


from pygame.font import SysFont

# Initialize Pygame
pygame.init()

# This game is open-sourced. If you wish to mod this and make it public, you MUST open-source it as well.
# If you are using this file and want to mod it, get an IDLE, such as Visual Studio Code.
# To compile this game to an executable, please install Pyinstaller using pip. The command to install for Windows: pip install pyinstaller
# To compile this game to an executable, please install Pyinstaller using pip. The command to install for linux: pip3 install pyinstaller
# To turn the .py file into an executable, the command is: pyinstaller (type in the name of this file) --onefile

# Get the colors all set up and initialized. Each color is in RGB code (search up on the web for more info).
RED = (255, 0, 0)
ORANGE = (255, 150, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MIDNIGHT_BLUE = (25, 25, 125)
PURPLE = (50, 0, 50)
PINK = (255, 0, 255)
SILVER = (192, 192, 192)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def makeFromASCII(ascii, fgColor=(255,255,255), fgColor2=(0,0,0), fgColor3=(0,0,0), fgColor4=(0, 0, 0)):
    """Returns a new pygame.Surface object that has the image drawn on it as specified by the ascii parameter.
    The first and last line in ascii are ignored. Otherwise, any X in ascii marks a pixel with the foreground color
    and any other letter marks a pixel of the background color. The Surface object has a width of the widest line
    in the ascii string, and is always rectangular."""

    """ This function will be inherited into every sprite that will inherit this function, according to the laws of 
    Object-Orientated Programming. """
    ascii = ascii.split('\n')[1:-1]
    width = max([len(x) for x in ascii])
    height = len(ascii)
    surf = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    # surf.fill(bgColor)
    surf = surf.convert_alpha()

    pArr = pygame.PixelArray(surf)
    for y in range(height):
        for x in range(len(ascii[y])):
            if ascii[y][x] == 'X':
                pArr[x][y] = fgColor
            if ascii[y][x] == 'P':
                pArr[x][y] = fgColor2
            if ascii[y][x] == '#':
                pArr[x][y] = fgColor3
            if ascii[y][x] == 'E':
                pArr[x][y] = fgColor4
    return surf


spaceship = """ 

                                                X
                                              XXXXX
                                             XXXXXXX
                                           XXXXXXXXXXX
                                         XXXXXXXXXXXXXXX
                                       XXXXXXXXXXXXXXXXXXX
                                     XXXXXXXXXXXXXXXXXXXXXXX
                                   XXXXXXXXXXXXXXXXXXXXXXXXXXX
                                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                 PPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPP
               PPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPP
             PPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPP
           PPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPP
         PPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPP
       PPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPP
     PPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPP
   PPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPP
 PPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPPP XXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXX PPPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPPP   XXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXX  PPPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPPP     XXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXX    PPPPPPPPPPPPPPPP
PPPPPPPPPPPPPPP       XXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXX      PPPPPPPPPPPPPPP
PPPPPPPPPPPPPP         XXXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXXX        PPPPPPPPPPPPPP
PPPPPPPPPPPPP           XXXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXXXX          PPPPPPPPPPPPP
PPPPPPPPPPPP             XXXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXX             PPPPPPPPPPPP
PPPPPPPPPPP               XXXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXXX              PPPPPPPPPPP
PPPPPPPPPP                 XXXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXXX                PPPPPPPPPP
PPPPPPPPP                   XXXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXXX                  PPPPPPPPP
PPPPPPPP                     XXXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXXX                    PPPPPPPP
PPPPPPP                       XXXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXXX                      PPPPPPP
PPPPPP                         XXXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXXX                        PPPPPP
PPPPP                           XXXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXXX                          PPPPP
PPPP                             XXXXXXXXXXXXPPPPPPPPXXXXXXXXXXXX                            PPPP
PPP                               XXXXXXXXXXXPPPPPPPPXXXXXXXXXXX                              PPP
PP                                 XXXXXXXXXXPPPPPPPPXXXXXXXXXX                                PP
PP                                  XXXXXXXXXPPPPPPPPXXXXXXXXX                                 PP
PP                                           PPPPPPPP                                          PP
P                                            PPPPPPPP                                           P
"""

bullet = """ 

              X
             XXX
            XXXXX
           XXXXXXX
          XXXXXXXXX
         XXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX

 """



missle = """          
          XXXXXXXXX
         XXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXX
     XXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
         XXXXXXXXXXX
          XXXXXXXXX
           XXXXXXX
            XXXXX
             XXX
              X
"""


alien = """          
          XXXXXXXXX
         XXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXX
     XXXXXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
        XXXXXXXXXXXXX
         XXXXXXXXXXX
          XXXXXXXXX
           XXXXXXX
            XXXXX
             XXX
              X
"""


boss = """ 
        PP                                                          PP
        PPP                                                        PPP
        PPPP                                                      PPPP
        PPPPP         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX          PPPPP
        PPPPPP       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        PPPPPP
        PPPPPPP     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      PPPPPPP
        PPPPPPPP   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    PPPPPPPP
        PPPPPPPPP XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  PPPPPPPPP
        PPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPPP
        PPPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPPP
         PPPPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPPP
          PPPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPPP
           PPPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPPP
            PPPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPPP
             PPPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPPP
              PPPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPPP
               PPXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPP
                PXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXP
                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                         XXXXXXXXXXXXXXXXXXXXXXXXXXX
                          XXXXXXXXXXXXXXXXXXXXXXXXX
                           XXXXXXXXXXXXXXXXXXXXXXX
                            XXXXXXXXXXXXXXXXXXXXX
                             XXXXXXXXXXXXXXXXXXX
                              XXXXXXXXXXXXXXXXX
                               XXXXXXXXXXXXXXX
                                XXXXXXXXXXXXX
                                 XXXXXXXXXXX
                                  XXXXXXXXX
                                   XXXXXXX
                                    XXXXX
                                     XXX
                                      X
 """

class SpriteTemplate(pygame.sprite.Sprite):
    # Make some optional parameters, as some sprites do not use these parameters
    def __init__(self, image, speed, color1=(0, 0, 0), color2=(0, 0, 0), color3=(0, 0, 0), color4=(0, 0, 0), armor=0):
        # Put this line so some sprites are allowed to be put into Group, a list-like object from pygame
        super().__init__()

        # Make our image
        self.image = makeFromASCII(image, color1, color2, color3, color4)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.armor = armor
        self.vel = 0
        self.kill_this_sprite = False
    
    def update(self):
        # If the sprite needs to dissapear, kill the sprite
        if self.kill_this_sprite == True:
            self.kill()

    def blitme(self):
        TMRC.screen.blit(self.image, self.rect)

class Player(SpriteTemplate):
    """ Create our player, the spaceship """
    def __init__(self):
        SpriteTemplate.__init__(self, spaceship, 5, SILVER, RED, BLUE, ORANGE)

        self.rect.midbottom = TMRC.screen_rect.midbottom

        self.move_right = False
        self.move_left = False
        self.vel = float(self.rect.x)
        
    def update(self):
        SpriteTemplate.update(self)
        if self.move_left and self.rect.left > TMRC.screen_rect.left:
            self.vel -= self.speed
        if self.move_right and self.rect.right < TMRC.screen_rect.right:
            self.vel += self.speed
        self.rect.x = self.vel

    def blitme(self):
        SpriteTemplate.blitme(self)

class Bullet(SpriteTemplate):
    """ Create the bullet that the player will shoot.
    
    These bullets will dissapear when they reach the top of the screen. """
    def __init__(self):
        SpriteTemplate.__init__(self, bullet, 10, ORANGE)
        self.rect.center = TMRC.player.rect.midtop

        self.vel = float(self.rect.y)
    
    def update(self):
        SpriteTemplate.update(self)
        self.vel -= self.speed
        self.rect.y = self.vel
        if self.rect.bottom < TMRC.screen_rect.top: # Less than because the coordinates (0, 0) would mean the topleft of the screen.
            self.kill_this_sprite = True
    
    def blitme(self):
        SpriteTemplate.blitme(self)


class Alien(pygame.sprite.Sprite):
    """ Our enemy. We need to shoot each one of them, or else they will make it to their target and destroy the galaxy we live in. """
    def __init__(self):
        super().__init__()

        # Make our image
        self.image = makeFromASCII(alien, GREEN)
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

        self.speed = 3
        self.armor = 0
        self.vel = 0
        self.kill_this_sprite = False

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += (self.speed * TMRC.direction)
        
        # self.x += self.speed
        self.rect.x = self.x
    
    def check_edges(self):
        screen_rect = TMRC.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True
    
    def blitme(self):
        TMRC.screen.blit(self.image, self.rect)

class Missle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = makeFromASCII(missle, RED)
        self.rect = self.image.get_rect()
        self.rect.center = TMRC.bossSprite.rect.center

        self.speed = 3
        self.steer_speed = 5 

        self.xvel = float(self.rect.x)
        self.yvel = float(self.rect.y)
    
    def update(self):
        self.yvel += self.speed
        self.rect.y = self.yvel
        
        if TMRC.player.rect.right + 10 < self.rect.left:
            self.xvel -= self.steer_speed
        if TMRC.player.rect.left - 10 > self.rect.right: 
            self.xvel += self.steer_speed
        self.rect.x = self.xvel
    
    def blitme(self):
        TMRC.screen.blit(self.image, self.rect)

class Boss(SpriteTemplate):
    def __init__(self):
        SpriteTemplate.__init__(self, boss, 0, SILVER, GREEN, armor=3)

        self.rect.midtop = TMRC.screen_rect.midtop

        self.timer_ticks = pygame.time.get_ticks()

    def update(self):
        SpriteTemplate.update(self)

        if ((pygame.time.get_ticks()-self.timer_ticks)/1000) >= 3:
            newMissle = Missle()
            TMRC.missle_list.add(newMissle)
            self.timer_ticks = pygame.time.get_ticks()
        
        if self.armor == 0:
            TMRC.boss_destroyed = True
            TMRC.boss = False

class Button(pygame.sprite.Sprite):
    def __init__(self, word='', fontcolor=(0,0,0), backgroundcolor=(0,0,0)):
        super().__init__()
        self.color = fontcolor
        self.backgroundcolor = backgroundcolor
        self.word = word
        self.font = SysFont('Ubuntu', 50, False, False)
    
    def prep_button(self):
        self.image = self.font.render(self.word, True, self.color, self.backgroundcolor)

        self.rect = self.image.get_rect()
        self.rect.center = TMRC.screen_rect.center
    
    def blitme(self):
        TMRC.screen.blit(self.image, self.rect)

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self):
        self.color = WHITE
        self.font = SysFont('Ubuntu', 50, False, False)
    
    def prep_scoreboard(self):
        self.scoreimage = self.font.render("Score: " + str(TMRC.score), True, self.color)
        self.levelimage = self.font.render("Level: " + str(TMRC.level), True, self.color)

        self.score_rect = self.scoreimage.get_rect()
        self.level_rect = self.levelimage.get_rect()

        self.score_rect.topleft = TMRC.screen_rect.topleft
        self.level_rect.x = self.score_rect.x
        self.level_rect.y = self.score_rect.y + 50
    
    def blitme(self):
        TMRC.screen.blit(self.scoreimage, self.score_rect)
        TMRC.screen.blit(self.levelimage, self.level_rect)

class TheMainRunningClass():
    def __init__(self):
        # Our function to initialize
        # Make our screen dimensions
        self.WIDTH = 1200
        self.HEIGHT = 800
        self.WINDOW_SIZE = [self.WIDTH, self.HEIGHT]
        self.WINDOW_FLAGS = pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, self.WINDOW_FLAGS)
        self.screen_rect = self.screen.get_rect()

        # Set our caption for the window.
        pygame.display.set_caption("Super Space Defense")

        self.level = 1
        self.score = 0

        self.boss = False
        self.boss_destroyed = False

        self.set_game_active = False

        self.clock = pygame.time.Clock()
        

    def mainFunc(self):
        # Our main game loop

        # Set up number variables
        self.direction = 1
        # Define our sprites; These sprites will reset their stats everytime a new level happens. Also define our groups.
        self.startButton = Button('PLAY', BLACK, RED)
        self.startButton.prep_button()
        self.scoreboard = ScoreBoard()
        self.scoreboard.prep_scoreboard()
        self.player = Player()
        self.bullet_list = pygame.sprite.Group()
        self.enemy_alien_list = pygame.sprite.Group()
        self.missle_list = pygame.sprite.Group()
        self.make_alien_fleet()

        
        while True:
            # Bug checker (will be deleted when put on github)
            # print(str(self.screen_rect.left) + ", " + str(self.player.rect.left))
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If we clicked on the red X
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Our check if we are pressing on the keyboard.
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = True
                    if event.key == pygame.K_SPACE:
                        if self.set_game_active == True:
                            self.fire_bullet()
                if event.type == pygame.KEYUP:
                    # Our check if we are letting go of the keyboard.
                    if event.key == pygame.K_LEFT:
                        self.player.move_left = False
                    if event.key == pygame.K_RIGHT:
                        self.player.move_right = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If we clicked on the mouse...
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        # To be precise, if we left-clicked on the mouse...
                        clicked = self.startButton.rect.collidepoint(mouse_pos)
                        if clicked:
                            self.set_game_active = True
                            self.boss_destroyed = False
            # Update our sprites
            self.update()
            # Blit our sprites to our screen
            self.blit_everything_onto_screen()

            # Call the function to destroy the aliens
            self.check_bullet_alien_collision()

            # Call the function to make the aliens change dir
            self._check_fleet_edges()

            # Set our fps to 60
            self.clock.tick(60)

            # Let us see what we have drawn.
            pygame.display.flip()
        
        # Just to be safe, kill the program if the game is closed.
        sys.exit()

    def update(self):
        if self.set_game_active == True:
            for bullet in self.bullet_list:
                bullet.update()
            self.player.update()
            for alien in self.enemy_alien_list:
                alien.update()
            if self.boss == True:
                self.bossSprite.update()
                self.bossisdestroyed()
            for missle in self.missle_list:
                missle.update()
            self._check_collision_on_bottom()
        self.scoreboard.prep_scoreboard()
    
    def blit_everything_onto_screen(self):
        # Draw everything onto the screen. Order matters.

        # Fill the background a specific color, say midnight blue
        self.screen.fill(MIDNIGHT_BLUE)
        # Draw the bullets. These will go below the player (makes more sense)
        for bullet in self.bullet_list:
            bullet.blitme()
        # Draw our infamous player, the spaceship
        self.player.blitme()
        # Draw our enemy aliens
        for alien in self.enemy_alien_list:
            alien.blitme()
        
        for missle in self.missle_list:
            missle.blitme()
        if self.boss == True:
            self.bossSprite.blitme()
        self.scoreboard.blitme()
        if self.set_game_active == False:
            self.startButton.blitme()            
    
    # Make special functions
    def fire_bullet(self):
        # If our amount of ammo shot is less than five, then fire a bullet. Else, lets reload.
        if len(self.bullet_list) <= 5:
            newBullet = Bullet()
            self.bullet_list.add(newBullet)
    
    def make_alien_fleet(self):
        alien = Alien()
        alien_width, alien_height = alien.rect.size

        avaliable_space_x = self.WIDTH - (2 * alien_width)
                
        number_aliens_x = avaliable_space_x // (2 * alien_width)
                
        ship_height = self.player.rect.height
        avaliable_space_y = (self.HEIGHT - (3 * alien_height) - ship_height)
        
        # number_rows = avaliable_space_y // (2 * alien_height)
        number_rows = 4
        for row_number in range(number_rows):    
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        alien = Alien()
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.enemy_alien_list.add(alien)

    def check_bullet_alien_collision(self):
        # Detects if we destroyed something
        self.collide = pygame.sprite.groupcollide(self.bullet_list, self.enemy_alien_list, True, True)
        self.collide2 = pygame.sprite.groupcollide(self.bullet_list, self.missle_list, True, True)
        if self.level == 5:
            self.collide3 = pygame.sprite.spritecollide(self.bossSprite, self.bullet_list, True)
        # Add to our score
        if self.collide:
            self.score += 10
        if self.collide2:
            self.score += 20
        if self.level == 5:
            if self.collide3:
                self.bossSprite.armor -= 1
                self.score += 20
        # Now detect if there are no aliens
        if not self.enemy_alien_list and not self.boss:
            self.bullet_list.empty()
            self.enemy_alien_list.empty()
            self.level += 1
            if self.level < 5:
                self.make_alien_fleet()
            elif self.level >= 5:
                if self.boss_destroyed == False:
                    self.boss = True
                    self.bossSprite = Boss()
            
        
    
    def _check_fleet_edges(self):
        for alien in self.enemy_alien_list.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.enemy_alien_list.sprites():
            alien.rect.y += 10
        self.direction *= -1
    
    def _check_collision_on_bottom(self):
        for alien in self.enemy_alien_list.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self.player_hit()
        if pygame.sprite.spritecollide(self.player, self.enemy_alien_list, True):
            self.player_hit()
        for missle in self.missle_list.sprites():
            if missle.rect.bottom >= self.screen_rect.bottom:
                self.player_hit()
        if pygame.sprite.spritecollide(self.player, self.missle_list, True):
            self.player_hit()
    
    def bossisdestroyed(self):
        if self.bossSprite.armor == 0:
            self.missle_list.empty()
            self.enemy_alien_list.empty()
            self.level = 1
            self.score = 0
            self.make_alien_fleet()
            self.set_game_active = False
    
    def player_hit(self):
        self.bullet_list.empty()
        self.enemy_alien_list.empty()
        self.missle_list.empty()
        self.make_alien_fleet()
        self.level = 1
        self.score = 0
        self.player.rect.midbottom = self.screen_rect.midbottom
        self.set_game_active = False





TMRC = TheMainRunningClass()
TMRC.mainFunc()