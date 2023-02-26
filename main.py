import pygame
from pygame.locals import *

class Gamer(object):
    def __init__(self,screen):
        self.x = 220
        self.y = 610
        self.screen = screen
        self.imageName = './src/ufo.png'
        self.image = pygame.image.load(self.imageName)
        self.bulletList = []

    def move_left(self):
        if self.x > 0:
            self.x -= 10

    def move_right(self):
        if self.x < 410:
            self.x += 10

    def move_up(self):
        if self.y > 300:
            self.y -= 10

    def move_down(self):
        if self.y < 610:
            self.y += 10

    def gamer_display(self):
        self.screen.blit(self.image, (self.x, self.y))
        needDeleteItem = []
        for item in self.bulletList:
            if item.judge():
                needDeleteItem.append(item)
        for i in needDeleteItem:
            self.bulletList.remove(i)
        for j in self.bulletList:
            j.display()
            j.move()

    def open_fire(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)

class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 23
        self.y = y - 20
        self.screen = screen
        self.image = pygame.image.load('./src/bullet02.png')

    def display(self):
        self.screen.blit(self.image,(self.x, self.y))

    def move(self):
        self.y -= 14

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

def key_control(GamerObj):
    # get keyboard event
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('quit this game')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                GamerObj.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                GamerObj.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up')
                GamerObj.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                GamerObj.move_down()
            elif event.key == K_SPACE:
                print('space')
                GamerObj.open_fire()

def main():
    screen = pygame.display.set_mode((470,660), depth=32)
    background = pygame.image.load('./src/background.png')
    icon = pygame.image.load('./src/star_wars_icon.png')
    # set a title
    pygame.display.set_caption('Star Wars')
    # set background music
    pygame.mixer.init()
    pygame.mixer.music.load('./src/the_night_king.mp3')
    pygame.mixer.music.set_volume(0.2)
    # loop music
    pygame.mixer.music.play(-1)

    # load gamer
    gamer = Gamer(screen)

    while True:
        screen.blit(background, (0, 0))
        pygame.display.set_icon(icon)
        # show gamer location
        gamer.gamer_display()
        # get keyboard event
        key_control(gamer)
        # update game
        pygame.display.update()

if __name__ == '__main__':
    main()