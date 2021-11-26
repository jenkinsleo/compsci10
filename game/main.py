#leos 2d game for computer science 10/20

#imports and sets window dimensions all very boring stuff as well as some basic constants here
import pygame
import time

run_main_override = True

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class game():
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    #player velocity
    VEL = 2
    
    #last pressed key, 1 = w, 2 = a, 3 = s, 4 = d
    move_opposite = 0

    #for pausing movement

    stop_movement = False


    

    def __init__(self):
        pygame.display.set_caption("First Game!")
        

        
        #player class
        self.char = player(self.WIDTH,self.HEIGHT)

        #level / map class
        self.level = level(self.WIN)

    #for keypresses and moving the player
    def movement(self):
        block_var = 0
        #1 = w, 2 = a, 3 = s, 4 = d
        #w = (0,0,1), a = (0,1,0), s = (1,0,0) = d = (1,1,0)
        #specific barriers will block the movement of specific arrows
        
        if self.char.player_rect.collidedict(self.level.collide_dict) != None:
            colour = self.char.player_rect.collidedict(self.level.collide_dict)
            print(colour)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and block_var != 'w':
            self.level.Y += self.VEL
            
        if keys[pygame.K_a] and block_var != 'a':
            self.level.X += self.VEL
            
        if keys[pygame.K_s] and block_var != 's':
            self.level.Y -= self.VEL
            
        if keys[pygame.K_d] and block_var != 'd':
            self.level.X -= self.VEL
            

    #this is the main game loop
    def main(self):
        global run_main_override
        #controls the clock speed
        clock = pygame.time.Clock()
        
        run = True

        self.char.draw_player(self.WIN)

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

            if run_main_override:       

                self.WIN.fill((25,20,43))
                #drawing and updating window comes after this but before the update
                #draws the invisible recangles for collision detection
                self.level.draw_collision(self.WIN)
                self.level.draw(self.WIN,self.char.player_rect, self.WIDTH, self.HEIGHT)
                
                

                self.movement()
                self.char.draw_player(self.WIN)


                pygame.display.update()
            else:
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_SPACE]:
                    run_main_override = True

                
        

    def pause_movement(self):
        print(self.stop_movementa)
        self.stop_movement = True

#for now this is a basic rectangle
class player():
    X = 0
    Y = 0

    # draws a 20x20 rectangle in the middle of the screen
    def default_coords(self,width,height):
        self.X = (width/2) - 20
        self.Y = (height/2) - 30

    def draw_player(self,WIN):
        self.player_rect = pygame.draw.rect(WIN, (255,255,255), (self.X,self.Y, 20,30))

    def __init__(self,width,height):
        self.default_coords(width,height)

#creates interactable objects
class game_object():
    obj_pos = (0,0)
    level_pos = (0,0)    
    within_range = False

    final_x = 0
    final_y = 0

    def __init__(self,XY, default_color, change_color, interact_method, complete_method):
        self.default_color = default_color
        self.change_color = change_color
        self.interact_method = interact_method
        self.complete_method = complete_method
        self.obj_pos = XY

    def draw_collide(self,WIN):
        self.collide_rect = pygame.draw.rect(WIN, (0,0,0), (self.final_x - 30, self.final_y - 30, 75,75))


    def draw(self, WIN,level_XY,player_rect, WIDTH, HEIGHT):
        self.final_x = self.obj_pos[0] + level_XY[0]
        self.final_y = self.obj_pos[1] + level_XY[1]

        if self.within_range:
            draw_color = self.change_color
        else:
            draw_color = self.default_color
        

        

        self.obj_rect = pygame.draw.rect(WIN,draw_color, (self.final_x,self.final_y,20,20))
        self.within_range = player_rect.colliderect(self.collide_rect)

        self.manage_interaction(WIDTH, HEIGHT, WIN)

    def manage_interaction(self, WIDTH, HEIGHT, WIN):
        keys = pygame.key.get_pressed()
        global run_main_override
        

        if self.within_range:
            
            if keys[pygame.K_SPACE]:
                
                if run_main_override != False:
                
                    args = {'win': WIN, 'width': WIDTH, 'text': self.complete_method}
                    self.interact_method(args)
                
    def dialogue_method(args):
        global run_main_override
        

        clock = pygame.time.Clock()

        pygame.image.save(args['win'],"game/screenshot.jpg")
        args['win'].blit(pygame.image.load('game/screenshot.jpg'), (0,0))
        pygame.draw.rect(args['win'], (255,255,255), (0,0,args['width'], 100))

        #creates the text
        textsurface = myfont.render(args['text'], True, (0, 0, 0))
        args['win'].blit(textsurface, (10,20))

        pygame.display.update()

        time.sleep(1)
            
        print("CALLED")

class level():
    X = 0
    Y = 0
    def __init__(self, WIN):
        self.image = pygame.image.load("game/cs20test.png")
        self.create_objects(WIN)

    def draw_collision(self,WIN):
        self.collide_dict = {}
        self.collide_dict[pygame.draw.rect(WIN,(255,255,255),(self.X, self.Y, 32, 512))] = "a"
        self.collide_dict[pygame.draw.rect(WIN,(255,255,255),(self.X + 32, self.Y + 62, 9*32, 32))] = "w"
        self.draw_object_collision(WIN)

        

    def draw(self,WIN,player_rect, WIDTH, HEIGHT):
        WIN.blit(self.image, (self.X,self.Y))
        
        self.draw_objects(WIN,player_rect, WIDTH, HEIGHT)

    def draw_objects(self,WIN,player_rect, WIDTH, HEIGHT):
        for game_object_instance in self.object_list:

                game_object_instance.draw(WIN, (self.X, self.Y),player_rect, WIDTH, HEIGHT)

    def draw_object_collision(self,WIN):
        for game_object_instance in self.object_list:

                game_object_instance.draw_collide(WIN)

    def create_objects(self, WIN):
        self.object_list = []

        self.object_list.append(game_object((300,300),(250, 37, 55),(81, 245, 66),game_object.dialogue_method,"Test"))
        self.object_list.append(game_object((500,300),(250, 37, 55),(81, 245, 66),"",""))



if __name__ == "__main__":
    new_game = game()
    new_game.main()