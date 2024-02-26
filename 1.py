import pygame
import sys

class Button:
    def __init__(self, x, y, width, height, idle_image_path, hover_image_path, click_sound_path, hover_sound_path, text, font_path, font_size, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.idle_image = pygame.image.load(idle_image_path)
        self.hover_image = pygame.image.load(hover_image_path)
        self.image = self.idle_image
        self.click_sound = pygame.mixer.Sound(click_sound_path)
        self.hover_sound = pygame.mixer.Sound(hover_sound_path)
        self.clicked = False
        self.hover_sound_played = False
        self.text = text
        self.font = pygame.font.Font(font_path, font_size)
        self.text_color = text_color

    def play_hover_sound(self):
        pygame.mixer.Sound.play(self.hover_sound)

    def play_click_sound(self):
        pygame.mixer.Sound.play(self.click_sound)

    def is_mouse_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def update(self):
        if self.is_mouse_over():
            self.image = self.hover_image
            if not self.clicked and not self.hover_sound_played:
                self.play_hover_sound()
                self.hover_sound_played = True
        else:
            self.image = self.idle_image
            self.hover_sound_played = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_mouse_over():
                self.play_click_sound()
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False

    def draw(self, screen):
        # Отрисовываем изображение кнопки
        screen.blit(self.image, self.rect.topleft)

        # Создаем текстовую метку
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Отрисовываем текстовую метку на кнопке
        screen.blit(text_surface, text_rect)

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Создание экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Кнопка с текстом")

# Создание объекта кнопки
button = Button(200, 200, 200, 100, "image/button0.jpg", "image/button1.jpg", "sound/nazh.wav", "sound/nazh.wav", "Game", "Samson.ttf", 55, (255, 255, 0))

# Основной цикл программы
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button.handle_event(event)

    # Обновление состояния кнопки
    button.update()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отрисовка кнопки
    button.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Установка FPS
    clock.tick(60)
