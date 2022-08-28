import pygame
import sys
sys.path.append('/Menu/')
from DataHandler import EnterQueue

def MainScreen(screen):
    #colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    color_active = pygame.Color('lightskyblue3')
    color = RED

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    font_arial = pygame.font.SysFont("arial", 50)
    font_arial_18 = pygame.font.SysFont("arial", 18)
    user_text = ''

    # Create objects
    input_rect = pygame.Rect(270, 115, 140, 32)
    Join_rect = pygame.Rect(10, 300, 100, 30)
    Username_label = font_arial.render("Username:", 1, BLACK)
    Username_err_label = font_arial_18.render("Username needs to be between 3 and 12 characters", 1, RED)
  
    active = False
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

                if Join_rect.collidepoint(event.pos):
                    EnterQueue()
  
            if event.type == pygame.KEYDOWN:
  
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
  
                else:
                    user_text += event.unicode

#rendering
        screen.fill((255, 255, 255))
        screen.blit(Username_label, (10, 100))
        if active:
            color = color_active
        elif len(user_text) < 3 or len(user_text) > 12:
            color = RED
            screen.blit(Username_err_label, (10, 150))
        else: 
            pygame.draw.rect(screen, GREEN, Join_rect)
            text_surface = font_arial_18.render("Join", True, (255, 255, 255))
            screen.blit(text_surface, (10, 300))
          
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)

#update call
        pygame.display.flip()