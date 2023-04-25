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

    hint_font = pygame.font.SysFont('Arial', 20, bold=True)
    hint_render = hint_font.render(
        'press t or r', True, pygame.Color('orange'))
    hint_rect = hint_render.get_rect(center=(global_.WINDOW_SIZE // 2, global_.WINDOW_SIZE // 3 + 40))
    global_.screen.blit(hint_render, hint_rect)


def draw_records(mas) -> None:
    global_.screen.blit(global_.hall, (0, 0))
    #global_.screen.fill(pygame.Color('black'))

    GOLD = (255, 215, 0)
    font_title = pygame.font.SysFont('Arial', 100, bold=True)
    title_render = font_title.render('Hall of Fame', True, GOLD)
    title_rect = title_render.get_rect(center=(global_.WINDOW_SIZE // 2, 100))
    global_.screen.blit(title_render, title_rect)

    now = 250
    font_records = pygame.font.SysFont('Arial', 75, bold=False)
    for name, score in mas:
        score_render = font_records.render(
            f'{name}   {score}', True, GOLD)
        score_rect = score_render.get_rect(
            center=(global_.WINDOW_SIZE // 2, now))
        now += 100
        global_.screen.blit(score_render, score_rect)
        if now + global_.SIZE * 2 >= global_.WINDOW_SIZE:
            break
