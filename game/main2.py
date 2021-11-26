#this is a rewrite of the first python game idea 

import pygame

#isntance vars not the WIN is extremely important and gets used alot
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#custom font make sure to install it from the ttf file if not already
pygame.font.init()
font = pygame.font.SysFont('Press Start 2P', 30)


class map():
    #velocity for moving the map around
    #all game objects will be linked to the map x and y plus/minus their respective value 
    VEL = 5
    x, y = 0, 0

    #loads the base image from the map
    def __init__(self, current_map, ):
        self.image = pygame.image.load(f"game/{current_map}.png")

    def draw(self):
        #fills with background color then adds the level / image on top
        WIN.fill((25,20,43))
        WIN.blit(self.image, (self.x,self.y))

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y += self.VEL
        if keys[pygame.K_a]:
            self.x += self.VEL
        if keys[pygame.K_s]:
            self.y -= self.VEL
        if keys[pygame.K_d]:
            self.x -= self.VEL

        return self.x, self.y

    def create_collision_rects_32x32(self,collisions):
        #this creates collision rects that will block specific movements for the 32x32 tilebased games
        for x in 

    def draw_collision_rects(self):
        rect_values = self.create_collision_rects_32x32()


class player():
    x,y = 0,0
    def __init__(self):
        self.center_player()

    def center_player(self):
        self.x = WIDTH / 2 - 20
        self.y = HEIGHT / 2 - 30

    def update_player(self):
        self.player_rect.x = self.x
        self.player_rect.y = self.y

    def draw(self):
        #creates a rect and make sure that the x and y are in centre of the screen the whole time
        self.player_rect = pygame.draw.rect(WIN,(255,255,255), (self.x,self.y,20,30))

    

#setup
def setup():
    global level1
    level1 = map('cs20test')
    
    collision_rects = [((2,3),(10,3)),((1,4),(1,7)),((2,8),(17,8))]

    global character
    character = player()

#this is the mainloop for the game
def main():
    #controls wether the loop runs or not
    run = True
    clock = pygame.time.Clock()
    while run:
        #ensures a smooth 60 fps and that the velocity can be moved at the same speed the whole time
        clock.tick(60)
        #allows the program to be quit cleanly
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

        #handles movement
        x,y = level1.movement()

        level1.draw()
        character.draw()

        #updates the window make sure this is at the end
        pygame.display.update()

if __name__ == "__main__":
    setup()
    main()