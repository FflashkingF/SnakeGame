import global_
import pygame
import fonts_
import constants_

def menu(start_name=''):
    size_of_font = 100
    base_font = pygame.font.Font(None, size_of_font)
    user_text = start_name
    input_rect = pygame.Rect(global_.WINDOW_SIZE // 4,
                             global_.WINDOW_SIZE // 3, size_of_font, size_of_font)
    color_active = pygame.Color('chartreuse4')
    color_passive = pygame.Color('lightskyblue3')
    color = color_active

    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        active = False
                    else:
                        user_text += event.unicode

                else:
                    level = 0
                    if event.key == pygame.K_1 or event.unicode == '1':
                        level = 1
                    elif event.key == pygame.K_2 or event.unicode == '2':
                        level = 2
                    elif event.key == pygame.K_3 or event.unicode == '3':
                        level = 3
                    elif event.key == pygame.K_4 or event.unicode == '4':
                        level = 4
                    elif event.key == pygame.K_5 or event.unicode == '5':
                        level = 5

                    if level:
                        return [level, user_text]

        global_.screen.fill('white')

        if active:
            color = color_active
        else:
            color = color_passive

        fonts_.draw_help_menu()
        pygame.draw.rect(global_.screen, color, input_rect)
        text_surface = base_font.render(user_text, True, 'white')
        global_.screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(size_of_font, text_surface.get_width()+10)

        pygame.display.flip()
        global_.clock.tick(60)
