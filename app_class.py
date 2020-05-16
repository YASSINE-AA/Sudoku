
import pygame
from settings import *
import sys
from backtracking import *
import time
from datetime import datetime, timedelta
from math import *
from boards_available import *
import runpy
from main import *
# User selected     
user_selected_x = 38
user_selected_y = 50

class Main:
    class App:
        def __init__(self):
            pygame.mixer.init(60000, -16, 2, 512)
            pygame.init()
            self.window = pygame.display.set_mode((width, height))
            pygame.display.set_caption(name)
            self.iconImg = pygame.image.load("icon.png")
            pygame.display.set_icon(self.iconImg)
            self.font = pygame.font.Font(used_font, 32) 
            self.font_user_input =pygame.font.Font(used_font, 32)
            self.font2 = pygame.font.Font(used_font, 14) 
            self.authors_font = pygame.font.Font(used_font, 12)
            self.beta = pygame.image.load("beta.png")
            self.running = True
            self.selected_x = 38
            self.selected_y = 150
            self.timeincrement = 0
            self.clicked = False
            self.num = 'NaN'
            self.vaild_to_place = True
            self.sound_enabled = False
            self.reset1 = False
            self.remove_last = False
            self.break1 = False
            self.reset_new = False
            self.clicked_r = False
        def run(self):
            while self.running:     
                self.events()
                self.draw()
                self.update()
           
                    
                    

    # ========================= EVENTS ===================================
        def events(self):
            
            def solver(new):
                if new == False:
                    self.board_being_showed = board_solved
                    solve(board_solved)
                    board_converted_solved = solve_converter()
                    k = 0
                    p = 0
                    for j in range(9):
                        for x in range(9): 
                            if board_converted_solved[x + k] == '0':
                                text = self.font.render('', True, material_blue)
                                self.window.blit(text, (57 + 56 * x, 165 + p))
                            else:
                                text = self.font.render(board_converted_solved[x + k], True, black)
                                self.window.blit(text, (57 + 56 * x, 165 + p))
                        k += 9
                        p += 56
                else:
                    clear(board_used)
            # Manages the sounds you want to play
            def sounds(sound):
                if self.sound_enabled:
                    return pygame.mixer.music.load(sound), pygame.mixer.music.play(1)
            user_selected_x_change = 0
            self.window.fill((255, 255, 255))
            # Fills up the Grid
            board_converted = converter()
            k = 0
            p = 0
            
            for j in range(9):
                for x in range(9): 
                    if board_converted[x + k] == '0':
                        text = self.font.render('', True, material_blue)
                        self.window.blit(text, (57 + 56 * x, 165 + p))
                    else:
                        text = self.font.render(board_converted[x + k], True, material_blue)
                        self.window.blit(text, (57 + 56 * x, 165 + p))
                k += 9
                p += 56
                
            if self.reset_new == True:
                for j in range(9):
                    for x in range(9): 
                        if isinstance(board_used[j][x], str):
                            board_used[j][x] = '0'
                            self.reset_new = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.selected_x += 56
                    if event.key == pygame.K_DOWN:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.selected_y += 56
                    if event.key == pygame.K_UP:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.selected_y += -56
                    if event.key == pygame.K_LEFT:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.selected_x += -56
                    if event.key == pygame.K_s:
                        self.sound_enabled = True
                        sounds(button_press)
                        solver(False)


                
                if event.type == pygame.KEYUP:
                    # ========================== Allows users to add items to the grid =============================
                    if event.key == pygame.K_1:
                        self.num = '1'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_2:
                        self.num = '2'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_3:
                        self.num = '3'
                        self.clicked = True       
                        self.sound_enabled = True
                        sounds(button_press)        
                    if event.key == pygame.K_4:
                        self.num = '4'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_5:
                        self.num = '5'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_6:
                        self.num = '6'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_7:
                        self.num = '7'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_8:
                        self.num = '8'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_9:
                        self.num = '9'
                        self.clicked = True
                        self.sound_enabled = True
                        sounds(button_press)
                    if event.key == pygame.K_n:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.reset_new = True
                    if event.key == pygame.K_q:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.clicked_r = True   

                    if event.key == pygame.K_r:
                        self.sound_enabled = True
                        sounds(button_press)
                        self.reset_new = True

    
    # ========================= DRAW ======================================
        def draw(self):
            pygame.draw.rect(self.window, material_blue,(0,0, 587, 100))
            self.window.blit(self.beta, (0,0))
            # ================================= Welcome Text ============================
            sudoku_text = self.font.render('Sudoku!', True, blue)
            welcome_text = self.font.render('Welcome to Sudoku!', True, white) 
            self.window.blit(welcome_text, (130, 35))

            # ================================= Solve Text ==============================
            solve_text = self.font2.render("Press 'S' to solve", True, blue) 
            self.window.blit(solve_text, (188, 117))
            # ================================== New game Text ==========================
            reset_text = self.font2.render("Press 'R' to reset", True, blue) 
            self.window.blit(reset_text, (50, 117))
            # ================================== New game Text ==========================
            remove_number_text = self.font2.render("Press 'Q' to remove a number", True, blue) 
            self.window.blit(remove_number_text, (333, 117))
            # ================================= Authors Text ============================
            authors_text = self.authors_font.render(f"Gui by: {authors.get('Gui')} | Algorithm by: {authors.get('Algorithm')}", True, black)
            self.window.blit(authors_text, (50, 662))

            # =================================== Timer (Fully working but slows down the application) =================================
            #m, s = divmod(self.timeincrement, 60)
            #h, m = divmod(m, 60)
            #timer = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
            #timer_1 = timer
            #timer_text = self.font.render(f'Time: {timer_1}', True, black)
            #time.sleep(1)
            #self.timeincrement += 1
            # self.window.blit(timer_text,  (180, 75))

            # ============================== User Related Stuff ========================
            # Selected Cell
            pygame.draw.rect(self.window, blue, (self.selected_x, self.selected_y, 56, 56), 4)
            # Set Boundaries
            if self.selected_x >= 486:
                self.selected_x = 486
            if self.selected_x <= 38:
                self.selected_x = 38
            if self.selected_y <= 150:
                self.selected_y = 150
            if self.selected_y >= 598:
                self.selected_y = 598
            # ================================== Grid =================================
            # Vertical Lignes
            for i in range(9):
                if i % 3 == 0:
                    pygame.draw.line(self.window, black, (38+ 56 * i, 150), (38+ 56 * i, 652), 3)
                else: 
                    pygame.draw.line(self.window, black, (38+ 56 * i, 150), (38+ 56 * i, 652), 1)
            # Horizontal Lignes
            for i in range(9):
                if i % 3 == 0:
                    pygame.draw.line(self.window, black, (38, 150 + 56 *i), (504 + 38, 150 + 56 * i), 3)
                else:
                    pygame.draw.line(self.window, black, (38, 150 + 56 *i), (504 + 38, 150 + 56 * i), 1)

            pygame.draw.rect(self.window, black, grid, 5)
            
        # ==================== Sounds ====================================
        
                    
        # ==================== Add Numbers ===============================

            # Position Finder
            col = trunc((self.selected_x - 38) / 56)
            row = trunc((self.selected_y - 150)/ 56)
            def replace(col, row, num):
                board_converted = converter()
                if board_used[row][col] == '0':
                    board_used[row][col] = num
            if self.clicked:
                replace(col, row, self.num)
                self.clicked = False
            
            # Remove selected
            col = trunc((self.selected_x - 38) / 56)
            row = trunc((self.selected_y - 150)/ 56)
            def remover(col, row):
                board_converted = converter()
                if isinstance(board_used[row][col],str):
                    board_used[row][col] = '0'
            if self.clicked_r:
                remover(col, row)
                self.clicked_r = False
            
            #===================== Solution Checker ==========================

        def update(self):
            pygame.display.update()

class restart():
    if Main().App().reset1:
        pygame.exit()
        Main()
        

restart()