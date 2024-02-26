import pygame, sys, random
from buttons import *

pygame.init()

WIDTH, HEIGHT = 1280, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MENU TEST')
bg_image = pygame.image.load('image/FON.jpg')


def main():
    start_btn = Button(200, 200, 200, 100, "image/button0.jpg", "image/button1.jpg", "sound/nazh.wav", "sound/nazh.wav", "Game", "Samson.ttf", 55, (255, 255, 0))
    exit_btn = Button(200, 320, 200, 100, "image/button0.jpg", "image/button1.jpg", "sound/nazh.wav", "sound/nazh.wav", "Exit", "Samson.ttf", 55, (255, 255, 0))

    run = True
    while run:
        screen.blit(bg_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if start_btn.clicked:
                print('GAME')
                game()

            elif exit_btn.clicked:
                pygame.quit()
                sys.exit()

            for btn in [start_btn, exit_btn]:
                btn.handle_event(event)

        start_btn.draw(screen)
        exit_btn.draw(screen)

        pygame.display.flip()

def exit_menu():
    pass

def game():
    screen_width = 1280
    screen_height = 720

    # Цвета
    white = (255, 255, 255)
    red = (255, 0, 0)

    # Размер блока и начальные координаты змейки
    block_size = 40
    snake_speed = 15
    snake_block = 40

    # Создание экрана
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Змейка")

    # Создание змейки
    snake = [(screen_width // 2, screen_height // 2)]
    snake_direction = (1, 0)  # Направление движения змейки (по горизонтали)
    change_to = snake_direction  # Изменение направления
    sound = pygame.mixer.Sound('sound/nazh.wav')
    # Создание еды
    food = (random.randrange(1, (screen_width//block_size)) * block_size,
            random.randrange(1, (screen_height//block_size)) * block_size)
    # Отображение счёта
    score = 0
    font = pygame.font.Font("Samson.ttf", 36)
    # Основной цикл программы
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not snake_direction == (0, 1):
                    change_to = (0, -1)
                elif event.key == pygame.K_DOWN and not snake_direction == (0, -1):
                    change_to = (0, 1)
                elif event.key == pygame.K_LEFT and not snake_direction == (1, 0):
                    change_to = (-1, 0)
                elif event.key == pygame.K_RIGHT and not snake_direction == (-1, 0):
                    change_to = (1, 0)

        # Обновление направления змейки
        snake_direction = change_to

        # Обновление координат змейки
        x, y = snake[0]
        x += snake_direction[0] * snake_block
        y += snake_direction[1] * snake_block

        # Проверка на столкновение с границами экрана
        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            main()

        # Проверка на столкновение с самой собой
        if (x, y) in snake[1:]:
            main()

        # Проверка на поедание еды
        if (x, y) == food:
            food = (random.randrange(1, (screen_width//block_size)) * block_size,
                    random.randrange(1, (screen_height//block_size)) * block_size)
            pygame.mixer.Sound.play(sound)
            score += 1
        else:
            snake.pop()

        # Добавление новой головы змейки
        snake.insert(0, (x, y))

        # Очистка экрана
        screen.fill(white)

        # Отрисовка змейки
        for segment in snake:
            pygame.draw.rect(screen, red, (segment[0], segment[1], block_size, block_size))

        # Отрисовка еды
        pygame.draw.rect(screen, red, (food[0], food[1], block_size, block_size))
        #score
        score_text = font.render("Score: {}".format(score), True, red)
        screen.blit(score_text, (10, 10))
        # Обновление экрана
        pygame.display.flip()

        # Установка FPS
        clock.tick(snake_speed)



if __name__ == '__main__':
    main()