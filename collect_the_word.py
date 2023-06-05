from main import MazeGame
from queue_word import Queue
import pygame
import pygame.mixer
from maze_maps import Maze_maps
from spritesheet_test import animation_list_Tletters,animation_list_Mletters,animation_list_Sletters,animation_list_Aletters,animation_list_Cletters,animation_list_Eletters,animation_list_numbers
import os
import pygame.freetype

BLACK = (0, 0, 0)
WHITE = "white"

class Collect_the_word(MazeGame):
    def __init__(self, maze,mode, multi=False):
        super().__init__(maze,mode)
        pygame.freetype.init()
        self.goal_draw=False  
        self.score_FONT = pygame.font.SysFont('comicsans',30)

        self.maze = [[cell for cell in row] for row in maze]
        "Create queue for the blue player "
        self.multi=multi
        self.player_blue_score=Queue()
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("S")
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("C")
        self.player_blue_score.enqueue("T")
        self.player_blue_score.enqueue("E")
        self.player_blue_score.enqueue("A")
        self.player_blue_score.enqueue("M")
        self.player_blue_score.enqueue("4")
        "Create queue for the red player"
        self.player_red_score=Queue()
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("S")
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("C")
        self.player_red_score.enqueue("T")
        self.player_red_score.enqueue("E")
        self.player_red_score.enqueue("A")
        self.player_red_score.enqueue("M")
        self.player_red_score.enqueue("4")
        self.player_2_pos = self.find_character(maze,"L")
        self.player_pos = self.find_character(maze,"P")
        self.A = animation_list_Aletters
        self.S = animation_list_Sletters  
        self.C = animation_list_Cletters  
        self.T = animation_list_Tletters  
        self.E = animation_list_Eletters  
        self.M = animation_list_Mletters  
        self.N4 = animation_list_numbers
        # self.A_pos = self.find_character(maze,"A")
        self.S_pos = self.find_character(maze,"S")
        self.C_pos = self.find_character(maze,"C")
        self.T_pos = self.find_character(maze,"V")
        self.E_pos = self.find_character(maze,"E")
        self.M_pos = self.find_character(maze,"M")
        self.N4_pos = self.find_character(maze,"4")
        self.frame_A = 0
        self.frame_S = 0
        self.frame_C = 0
        self.frame_T = 0
        self.frame_E = 0
        self.frame_M = 0
        self.frame_N4 = 0
        self.delay_A = pygame.time.get_ticks()
        self.delay_S = pygame.time.get_ticks()
        self.delay_C = pygame.time.get_ticks()
        self.delay_T = pygame.time.get_ticks()
        self.delay_E = pygame.time.get_ticks()
        self.delay_M = pygame.time.get_ticks()
        self.delay_N4 = pygame.time.get_ticks()
        self.cooldown_A = 200
        self.cooldown_S = 200
        self.cooldown_C = 200
        self.cooldown_T = 200
        self.cooldown_E = 200
        self.cooldown_M = 200
        self.cooldown_N4 = 200
        self.letter_collect_sound = pygame.mixer.Sound(os.path.join("Assets","Video_game_treasure_sound_effect.wav"))
        self.paragraph_text = """
    Welcome to the captivating world of Collect the Word\n\n 
    mode in single player! Your mission is to collect\n\n
    the words that appear at the top of the screen\n\n
    in the exact order they are presented.\n\n
    Gather them all, and the coveted goal will appear,\n\n
    leading you to victory. Sharpen your focus\n\n
    and embark on this word-collecting adventure!
  """
        self.paragraph_text2 = """
    Welcome to multiplayer Collect the Word mode!\n\n
    Race against opponents to collect words faster\n\n
    in order and reach the goal.\n\n
    Stay alert, be quick, and let the excitement begin!\n\n
    You'll be rewarded for your efforts.\n\n
    Good luck!
     """
        # Video_game_treasure_sound_effect.wav
    def check_word(self, player):
        if player == 2: 
  
            front_of_queue = self.player_blue_score.peek()

            if self.maze[self.new_row][self.new_col] == front_of_queue: # Update the maze 
                self.player_blue_score.dequeue()
                self.letter_collect_sound.play()
                self.maze[self.new_row][self.new_col] = " " # Remove the letter 
                # print(self.maze[self.new_row][self.new_col])

            if self.maze[self.new_row][self.new_col] == "V" and front_of_queue == "T": # Update the maze 
                self.player_blue_score.dequeue()
                self.letter_collect_sound.play()
                self.maze[self.new_row][self.new_col] = " " # Remove the letter
        if player == 1:
            front_of_queue2 = self.player_red_score.peek()  
            if self.maze[self.new_row][self.new_col] == front_of_queue2: # Update the maze 
                self.player_red_score.dequeue()
                self.letter_collect_sound.play()
                self.maze[self.new_row][self.new_col] = " " # Remove the letter 
                print(self.maze[self.new_row][self.new_col])

            if self.maze[self.new_row][self.new_col] == "V" and front_of_queue2 == "T": # Update the maze 
                self.player_red_score.dequeue()
                self.letter_collect_sound.play()
                self.maze[self.new_row][self.new_col] = " " # Remove the letter

        if self.player_blue_score.isEmpty() or self.player_red_score.isEmpty() :  
            self.goal_draw=True  
            
    
    
    def draw_the_letter(self,letter,list):
            if letter == "A":
                for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "A":
                            current_time = pygame.time.get_ticks()
                            if current_time - self.delay_A >= self.cooldown_A:
                                self.frame_A += 1
                                self.delay_A = current_time
                                if self.frame_A >= len(list):
                                    self.frame_A = 0
                            self.window.blit(list[self.frame_A], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (row*35)+self.offsett))
            if letter == "S":
               for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "S": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_S >= self.cooldown_S:
                            self.frame_S += 1
                            self.delay_S = current_time
                            if self.frame_S >= len(list):
                                self.frame_S = 0
                        self.window.blit(list[self.frame_S], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), (row*35)+self.offsett))
            elif letter == "C":
                for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "C": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_C >= self.cooldown_C:
                            self.frame_C += 1
                            self.delay_C = current_time
                            if self.frame_C >= len(list):
                                self.frame_C = 0
                        self.window.blit(list[self.frame_C], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett))
            elif letter == "V":
                for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "V": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_T >= self.cooldown_T:
                            self.frame_T += 1
                            self.delay_T = current_time
                            if self.frame_T >= len(list):
                                self.frame_T= 0
                        self.window.blit(list[self.frame_T], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett))
            elif letter == "E":
                  for row in range(len(self.maze)):
                   for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "E": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_E >= self.cooldown_E:
                            self.frame_E += 1
                            self.delay_E = current_time
                            if self.frame_E >= len(list):
                                self.frame_E= 0
                        self.window.blit(list[self.frame_E], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett))
            elif letter == "M":
                for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "M": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_M >= self.cooldown_M:
                            self.frame_M += 1
                            self.delay_M = current_time
                            if self.frame_M >= len(list):
                                self.frame_M= 0
                        self.window.blit(list[self.frame_M], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett))
            elif letter == "4":
                for row in range(len(self.maze)):
                 for col in range(len(self.maze[0])):
                    if self.maze[row][col] == "4": 
                        current_time = pygame.time.get_ticks()
                        if current_time - self.delay_N4 >= self.cooldown_N4:
                            self.frame_N4 += 1
                            self.delay_N4 = current_time
                            if self.frame_N4 >= len(list):
                                self.frame_N4= 0
                        self.window.blit(list[self.frame_N4], (col*35+self.window_width//2-(self.cell_width*len(self.maze[0])//2), row*35+self.offsett)) 
    
    def move_player(self, direction, player): 
        super().move_player(direction, player)
        self.check_word(player)


    def showing_score(self,pos1,pos2,player):
        if player==1: 
            blue_score_text =f"Blue Player Word : { self.player_blue_score.__str__()}"
            draw_text = self.score_FONT.render(blue_score_text, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()
        if player==2 and self.multi: 
            red_score_text =f"Red Player Word : {  self.player_red_score.__str__()}"
            draw_text = self.score_FONT.render(red_score_text, 1, WHITE)
            self.window.blit(draw_text, (pos1,pos2))
            pygame.display.update()


    def check_find_goal(self):
        if self.player_pos[0] == self.goal[0] and self.player_pos[1]==self.goal[1] and self.player_blue_score.isEmpty():
            winner_text = "Congratulations! Blue Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)

            return True
        elif self.player_2_pos[0] == self.goal[0] and self.player_2_pos[1]==self.goal[1] and self.player_red_score.isEmpty():
            winner_text = "Congratulations! Red Win!"
            pygame.mixer.music.stop()
            self.game_win_sound.play()
            self.draw_winner(winner_text)
            pygame.mixer.music.load('Assets/menu-_sound.wav')
            pygame.mixer.music.play(-1)
            return True
        return False  


    def run(self,multi=False):
        self.running = True
        self.display_buttons = True
        self.display_game = False
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    self.running = False
                    pygame.mixer.music.load('Assets/menu-_sound.wav')
                    pygame.mixer.music.play(-1)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.move_player("up",1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player("down",1)
                    elif event.key == pygame.K_LEFT:
                        self.move_player("left",1)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player("right",1)
                    if event.key == pygame.K_w:
                        self.move_player("w",2)
                    elif event.key == pygame.K_s:
                        self.move_player("s",2)
                    elif event.key == pygame.K_a:
                        self.move_player("a",2)
                    elif event.key == pygame.K_d:
                        self.move_player("d",2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                #   self.Click_sound.play()
               
                    if self.ok_button_img_rect.collidepoint(mouse_pos) and self.display_buttons:
                        self.display_buttons=False
                        self.display_game = True
            self.window.fill(BLACK)


            if self.display_buttons:
                self.window.blit(self.info_button_img1 ,(self.info_button_x-450, self.info_button_y-350))
                self.window.blit(self.ok_button ,(self.ok_button_x-50, self.ok_button_y))
                self.ok_button_img_rect = pygame.Rect( self.ok_button_x-50, self.ok_button_y, self.ok_button_width, self.ok_button_height)
                names_button_label,Back_label_rect = self.font.render("OK", self.button_text_color, None)
                Back_label_rect = names_button_label.get_rect(center=self.ok_button_img_rect.center)
                self.window.blit(names_button_label, Back_label_rect)
                if self.multi:
                    self.draw_para(self.paragraph_text2)
                else:
                    self.draw_para(self.paragraph_text)
            if self.display_game:
                 self.draw_the_letter("A",self.A)
                 self.draw_the_letter("S",self.S)
                 self.draw_the_letter("C",self.C)
                 self.draw_the_letter("V",self.T)
                 self.draw_the_letter("E",self.E)
                 self.draw_the_letter("M",self.M)
                 self.draw_the_letter("4",self.N4)
                 self.draw_treasure_maze()
                 self.draw_player(self.player_pos[1],self.player_pos[0],1,self.list_player_blue)
                 self.showing_score(5,5,1)
                 if self.multi:
                     self.showing_score(self.window_width-360,5,2)
                     self.draw_player(self.player_2_pos[1],self.player_2_pos[0],2,self.list_player_2_red)

                     self.draw_goal()
                     if self.check_find_goal():
                         pygame.mixer.music.stop()
                         self.running = False
                         pygame.mixer.music.load('Assets/menu-_sound.wav')
                         pygame.mixer.music.play(-1)
            # self.draw_the_letter(10,10,1)
            # if self.multi:
            #     self.draw_the_letter(self.window_width-220,10,2)
            pygame.display.flip()
            self.clock.tick(60)
        # pygame.quit()

if __name__ == "__main__":
    game = Collect_the_word( Maze_maps.complete_the_word_maze,True)

    game.run()