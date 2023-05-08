import pygame
import global_

def draw_score(score: int) -> None:
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    render_score = font_score.render(
        f'SCORE: {score}', True, pygame.Color('orange'))
    global_.screen.blit(render_score, (5, 5))


def draw_end() -> None:
    end_font = pygame.font.SysFont('Arial', 66, bold=True)
    end_render = end_font.render(
        'GAME OVER', True, pygame.Color('orange'))
    end_rect = end_render.get_rect(
        center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 3))
    global_.screen.blit(end_render, end_rect)

    SMALL_GAP = 40
    hint_font = pygame.font.SysFont('Arial', 20, bold=True)
    hint_render = hint_font.render(
        'press t (table) or r (restart) or m (menu)', True, pygame.Color('orange'))
    hint_rect = hint_render.get_rect(
        center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 3 + SMALL_GAP))
    global_.screen.blit(hint_render, hint_rect)


def draw_records(mas) -> None:
    global_.screen.blit(global_.hall, (0, 0))

    GOLD = (255, 215, 0)
    font_title = pygame.font.SysFont('Arial', 100, bold=True)
    title_render = font_title.render('Hall of Fame', True, GOLD)
    title_rect = title_render.get_rect(center=(global_.WINDOW_SIZE // 2, 100))
    global_.screen.blit(title_render, title_rect)

    now_y_to_records = global_.INITIAL_POSITION_FOR_RECORDS
    font_records = pygame.font.SysFont('Arial', 75, bold=False)
    for name, score in mas:
        score_render = font_records.render(
            f'{name}   {score}', True, GOLD)
        score_rect = score_render.get_rect(
            center=(global_.WINDOW_SIZE // 2, now_y_to_records))
        now_y_to_records += 100
        global_.screen.blit(score_render, score_rect)
        if now_y_to_records + global_.SIZE * 2 >= global_.WINDOW_SIZE:
            break

    support_font = pygame.font.SysFont('Arial', 20, bold=False)
    support_render = support_font.render('m (menu) or r (restart)', True, GOLD)
    global_.screen.blit(support_render, (5, global_.WINDOW_SIZE - 25))


def draw_help_menu():
    help_font = pygame.font.SysFont('Arial', 40, bold=True)
    help_render = help_font.render(
        'Input your nick.', True, pygame.Color('chartreuse4'))
    help_rect = help_render.get_rect(
        center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 10))
    global_.screen.blit(help_render, help_rect)

    help_render2 = help_font.render(
        'Click to rectangle and write your nick.', True, pygame.Color('chartreuse4'))
    help_rect2 = help_render2.get_rect(
        center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 10 + help_render.get_height()))
    global_.screen.blit(help_render2, help_rect2)

    help_render3 = help_font.render(
        'Click to Return to accept your nick.', True, pygame.Color('chartreuse4'))
    help_rect3 = help_render3.get_rect(
        center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 10 + help_render.get_height() + help_render2.get_height()))
    global_.screen.blit(help_render3, help_rect3)

    help_render4 = help_font.render(
        'After Return click 1...5 to choose level.', True, pygame.Color('chartreuse4'))
    help_rect4 = help_render4.get_rect(
        center=(global_.WINDOW_SIZE // 2, 8 * global_.WINDOW_SIZE // 10))
    global_.screen.blit(help_render4, help_rect4)
