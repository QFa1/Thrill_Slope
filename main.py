import pygame.freetype
import random
import os


pygame.init()
size = width, height = 700, 700
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
screen_rect = (0, 0, width, height)

scores = 0  # Очки
FONT = pygame.freetype.Font("data/font.ttf", 50)
FONT2 = pygame.freetype.Font("data/font.ttf", 20)
FONT3 = pygame.freetype.Font("data/font.ttf", 30)


def load_image(name, color_key=None):  # Скачивание файлов
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class ImageButton:  # Создание кнопок
    def __init__(self, x1, y, width1, height2, text, image_path, hover_image_path=None, btn_down=None, sound_path=None):
        self.text = text
        self.image = load_image(image_path)

        # Масшатибуем картинку под размеры кнопки
        self.image = load_image(image_path)
        self.image = pygame.transform.scale(self.image, (width1, height2))
        # Картинка если кнопка зажата
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width1, height2))

        self.btn_down = self.image
        if btn_down:
            self.btn_down = load_image(btn_down)
            self.btn_down = pygame.transform.scale(self.btn_down, (width1, height2))
        self.rect = self.image.get_rect(topleft=(x1, y))

        # Звук при нажатии кнопки
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        # Наведена ли мышка на кнопку
        self.is_hovered = False

        self.is_down = False

    def draw(self, screen1):
        if self.is_down:
            current_image = self.btn_down
        elif self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        screen1.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen1.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):  # Наведена ли мышка на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event1):  # обработка событий
        if self.is_hovered and event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            self.is_down = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
        else:
            self.is_down = False


class ButtonPause1(pygame.sprite.Sprite):  # Создание кнопки чтобы вызвать паузу
    def __init__(self, x1, y, width1, height2, image_path, hover_image_path=None, btn_down=None, sound_path=None):
        super().__init__(buttons_sprite, all_sprites)
        # Картинка если кнопка зажата
        self.hover_image = load_image(image_path)
        if hover_image_path:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width1, height2))
        self.btn_down = load_image(image_path)
        if btn_down:
            self.btn_down = load_image(btn_down)
            self.btn_down = pygame.transform.scale(self.btn_down, (width1, height2))
        # Звук при нажатии кнопки
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        # Наведена ли мышка на кнопку
        self.is_hovered = False
        # Нажата ли кнопка
        self.is_down = False
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y
        self.image_path = image_path
        self.width = width1
        self.height = height2
        self.settings1_button_time = 0

    def update(self):
        if self.is_down:
            self.image = self.btn_down
        elif self.is_hovered:
            self.image = self.hover_image
        else:
            self.image = load_image(self.image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if not pause:
            if self.settings1_button_time >= 0:
                self.settings1_button_time -= 0.1
                self.rect.y += 5
        else:
            if self.settings1_button_time <= 3:
                self.settings1_button_time += 0.1
                self.rect.y -= 5

    def check_hover(self, mouse_pos):  # Наведена ли мышка на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event1):  # обработка событий
        if self.is_hovered and event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            self.is_down = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
        else:
            self.is_down = False


class ButtonPause2(pygame.sprite.Sprite):  # Создание кнопок в паузе
    def __init__(self, x1, y, width1, height2, image_path, hover_image_path=None, btn_down=None, sound_path=None):
        super().__init__(background_pause_sprite, all_sprites)
        # Картинка если кнопка зажата
        self.hover_image = load_image(image_path)
        if hover_image_path:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width1, height2))
        self.btn_down = load_image(image_path)
        if btn_down:
            self.btn_down = load_image(btn_down)
            self.btn_down = pygame.transform.scale(self.btn_down, (width1, height2))
        # Звук при нажатии кнопки
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        # Наведена ли мышка на кнопку
        self.is_hovered = False
        # Нажата ли кнопка
        self.is_down = False
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y
        self.image_path = image_path
        self.width = width1
        self.height = height2
        self.settings1_button_time = 0

    def update(self):
        if self.is_down:
            if not music_play:
                self.image = self.btn_down
                sound_pause_btn.image = load_image('Buttons/notsoundbtn3.png')
            else:
                self.image = self.btn_down
        elif self.is_hovered:
            self.image = self.hover_image
            if not music_play:
                sound_pause_btn.image = load_image('Buttons/notsoundbtn2.png')
        else:
            self.image = load_image(self.image_path)
            if not music_play:
                sound_pause_btn.image = load_image('Buttons/notsoundbtn1.png')
        if not pause:
            if self.settings1_button_time >= 0:
                self.settings1_button_time -= 0.1
                self.rect.y += 7
        else:
            if not new_game and not defeat and not loading:
                if self.settings1_button_time <= 2.2:
                    self.settings1_button_time += 0.1
                    self.rect.y -= 7

    def check_hover(self, mouse_pos):  # Наведена ли мышка на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event1):  # обработка событий
        if self.is_hovered and event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            self.is_down = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
        else:
            self.is_down = False


class ButtonDefeat(pygame.sprite.Sprite):  # Создание кнопок в поражении
    def __init__(self, x1, y, width1, height2, image_path, hover_image_path=None, btn_down=None, sound_path=None):
        super().__init__(buttons_sprite, all_sprites)
        # Картинка если кнопка зажата
        self.hover_image = load_image(image_path)
        if hover_image_path:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width1, height2))
        self.btn_down = load_image(image_path)
        if btn_down:
            self.btn_down = load_image(btn_down)
            self.btn_down = pygame.transform.scale(self.btn_down, (width1, height2))
        # Звук при нажатии кнопки
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        # Наведена ли мышка на кнопку
        self.is_hovered = False
        # Нажата ли кнопка
        self.is_down = False
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y
        self.image_path = image_path
        self.width = width1
        self.height = height2
        self.defeat_time = 0

    def update(self):
        if self.is_down:
            if not music_play:
                self.image = self.btn_down
                sound_defeat_btn.image = load_image('Buttons/notsoundbtn3.png')
            else:
                self.image = self.btn_down
        elif self.is_hovered:
            if not music_play:
                self.image = self.hover_image
                sound_defeat_btn.image = load_image('Buttons/notsoundbtn2.png')
            else:
                self.image = self.hover_image
        else:
            if not music_play:
                self.image = load_image(self.image_path)
                sound_defeat_btn.image = load_image('Buttons/notsoundbtn1.png')
            else:
                self.image = load_image(self.image_path)
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if defeat:
            if self.defeat_time <= 3:
                self.defeat_time += 0.1
                self.rect.y -= 5
        else:
            if self.defeat_time >= 0:
                self.defeat_time -= 0.1
                self.rect.y += 5

    def check_hover(self, mouse_pos):  # Наведена ли мышка на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event1):  # обработка событий
        if self.is_hovered and event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            self.is_down = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
        else:
            self.is_down = False


class ButtonsMainSettings(pygame.sprite.Sprite):  # Создание кнопок в настройках
    def __init__(self, x1, y, width1, height2, image_path, hover_image_path=None, btn_down=None, sound_path=None):
        super().__init__(background_pause_sprite, all_sprites)
        # Картинка если кнопка зажата
        self.hover_image = load_image(image_path)
        if hover_image_path:
            self.hover_image = load_image(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width1, height2))
        self.btn_down = load_image(image_path)
        if btn_down:
            self.btn_down = load_image(btn_down)
            self.btn_down = pygame.transform.scale(self.btn_down, (width1, height2))
        # Звук при нажатии кнопки
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        # Наведена ли мышка на кнопку
        self.is_hovered = False
        # Нажата ли кнопка
        self.is_down = False
        self.image = load_image(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y
        self.image_path = image_path
        self.width = width1
        self.height = height2
        self.settings1_button_time = 0
        self.time = 0

    def update(self):
        if self.is_down:
            if not music_play:
                self.image = self.btn_down
                sound_settings_btn.image = load_image('Buttons/settingsnotsoundbtn2.png')
            else:
                self.image = self.btn_down
        elif self.is_hovered:
            if not music_play:
                self.image = self.hover_image
                sound_settings_btn.image = load_image('Buttons/settingsnotsoundbtn2.png')
            else:
                self.image = self.hover_image
        else:
            if not music_play:
                self.image = load_image(self.image_path)
                sound_settings_btn.image = load_image('Buttons/settingsnotsoundbtn1.png')
            else:
                self.image = load_image(self.image_path)
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

        if main_settings_open:
            if self.time <= 4:
                self.time += 0.1
                self.rect.y -= 10
        else:
            if self.time >= 0:
                self.time -= 0.1
                self.rect.y += 10

    def check_hover(self, mouse_pos):  # Наведена ли мышка на кнопку
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event1):  # обработка событий
        if self.is_hovered and event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            self.is_down = True
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
        else:
            self.is_down = False


class Background(pygame.sprite.Sprite):  # Начальный фон
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('Background/phon.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def update(self):
        self.kill()


class Character(pygame.sprite.Sprite):  # Персонаж
    def __init__(self, where, player_x1, player_y1):
        super().__init__(character_sprite, all_sprites)
        if where == 1:
            self.image = load_image('Character/MyCharacterLeft.png')
            self.rect = self.image.get_rect()
        if where == 2:
            self.image = load_image('Character/MyCharacterRight.png')
            self.rect = self.image.get_rect()
        if where == 3:
            self.image = load_image('Character/MyCharacter.png')
            self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = player_x1, player_y1

    def update(self):
        self.kill()


class ExtraPoints(pygame.sprite.Sprite):  # Дополнительные очки
    def __init__(self, x1, y, how_many):
        super().__init__(all_sprites)
        if how_many == 1:
            self.image = load_image('Background/extraScores.png')
            self.sound = pygame.mixer.Sound('data/Music/scoreSound.mp3')
        if how_many == 2:
            self.image = load_image('Background/extraScores2.png')
            self.sound = pygame.mixer.Sound('data/Music/upPresent.mp3')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y
        self.time = 0

    def update(self):
        if self.time == 0:
            self.sound.play()
        if self.time > 4:
            self.kill()
        self.time += 0.1


class Tree(pygame.sprite.Sprite):  # Деревья
    fir_picture = [load_image('Objects/fir3.png'), load_image('Objects/fir2.png'), load_image('Objects/fir3.png'),
                   load_image('Objects/fir.png'), load_image('Objects/fir.png'), load_image('Objects/fir.png'),
                   load_image('Objects/fir.png')]

    def __init__(self, pl_x, pl_y):
        super().__init__(tree_sprite, all_sprites)
        self.a = random.choice(self.fir_picture)
        self.image = self.a
        self.rect = self.image.get_rect()
        self.x, self.y = random.randint(-10, 690), -200
        self.rect.x, self.rect.y = self.x, self.y

        self.pl_pos = pl_x - 20, pl_y
        self.is_defeat = True
        self.a = True

    def update(self):
        global pause, defeat, scores, defeat_background_time
        if not defeat:
            if self.rect.collidepoint(self.pl_pos):
                if self.a:
                    scores += 2
                    self.a = False
                    ExtraPoints(self.rect.x + 10, self.rect.y, 1)
        if defeat:
            if scores <= 100:
                self.rect.y += 10
            elif scores >= 100:
                self.rect.y += 12

            if defeat_background_time <= 0.5:
                self.rect.x -= 6
            elif 0.5 <= defeat_background_time <= 1.5:
                self.rect.x += 6
            elif 1.5 <= defeat_background_time <= 2:
                self.rect.x -= 6
            else:
                self.rect.x = self.x
        if not pygame.sprite.collide_mask(self, character):
            if pause:
                self.rect.y += 0
            elif scores <= 100:
                if not raise_clock:
                    self.rect.y += 10
                else:
                    self.rect.y += 7
            elif scores >= 100:
                if not raise_clock:
                    self.rect.y += 12
                else:
                    self.rect.y += 7
            if self.rect.y > 700:
                self.kill()
        else:
            if defeat:
                if scores <= 100:
                    self.rect.y += 10
                elif scores >= 100:
                    self.rect.y += 12
            else:
                self.kill()
            pause = True
            if self.is_defeat:
                defeat = True
                self.is_defeat = False
        if new_game:
            self.kill()


class PauseBackground(pygame.sprite.Sprite):  # Фон для паузы
    def __init__(self, y):
        super().__init__(buttons_sprite, all_sprites)
        self.image = load_image('Background/pause.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, y

    def update(self):
        self.kill()


class Trace(pygame.sprite.Sprite):  # След после персонажа
    def __init__(self, x1, y1):
        super().__init__(all_sprites)
        self.image = load_image('Character/Trace.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y1

    def update(self):
        if not pause:
            if scores >= 100:
                if not raise_clock:
                    self.rect.y += 12
                else:
                    self.rect.y += 7
            else:
                if not raise_clock:
                    self.rect.y += 10
                else:
                    self.rect.y += 7
        else:
            if defeat:
                self.rect.y += 10
            else:
                self.rect.y += 0
        if new_game:
            self.kill()


class Defeat(pygame.sprite.Sprite):  # Фон для результатов поражения
    def __init__(self, x1, y):
        super().__init__(all_sprites)
        self.image = load_image('Background/defeat.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x1, y

    def update(self):
        if defeat:
            if self.rect.x < 0:
                self.rect.x += 10
            else:
                self.rect.x += 0
        self.kill()


class DefeatBackground(pygame.sprite.Sprite):  # Фон поражения
    def __init__(self, y):
        super().__init__(all_sprites)
        self.image = load_image('Background/defeat2.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, y

    def update(self):
        self.kill()


class LoadingText(pygame.sprite.Sprite):  # Загрузка
    def __init__(self, time1):
        super().__init__(loading_sprite, all_sprites)
        if time1 <= 0.2:
            self.image = load_image('Background/loadingText1.png')
        elif 0.2 <= time1 <= 0.5:
            self.image = load_image('Background/loadingText2.png')
        elif 0.5 <= time1 <= 3:
            self.image = load_image('Background/loadingText3.png')
        elif 3 <= time1 <= 3.5:
            self.image = load_image('Background/loadingText4.png')
        elif 3.5 <= time1 <= 4:
            self.image = load_image('Background/loadingText5.png')
        else:
            self.image = load_image('Background/nothing.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 234.5, 301

    def update(self):
        self.kill()


class Loading(pygame.sprite.Sprite):  # Фон загрузки
    def __init__(self, time1):
        super().__init__(loading_sprite, all_sprites)
        if time1 <= 0.2:
            self.image = load_image('Background/loading.png')
        elif 0.2 <= time1 <= 0.5:
            self.image = load_image('Background/loading2.png')
        elif 0.5 <= time1 <= 3:
            self.image = load_image('Background/loading3.png')
        elif 3 <= time1 <= 3.5:
            self.image = load_image('Background/loading2.png')
        elif 3.5 <= time1 <= 4:
            self.image = load_image('Background/loading.png')
        else:
            self.image = load_image('Background/nothing.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def update(self):
        self.kill()


class Particle(pygame.sprite.Sprite):  # Генерация частиц
    # сгенерируем частицы разного размера
    fire = [load_image("Objects/particle.png"), load_image("Objects/particle2.png")]
    for scale in (3, 8, 10):
        fire.append(pygame.transform.scale(fire[random.choice((0, 1))], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos
        # гравитация будет одинаковой (значение константы)
        self.gravity = -0.4
        self.a = 0

    def update(self):
        self.a += 1
        if self.a > 70 or loading:
            self.kill()
        else:
            # применяем гравитационный эффект:
            # движение с ускорением под действием гравитации
            if self.a > 5:
                self.velocity[1] -= self.gravity + -0.1
            else:
                self.velocity[1] += self.gravity + -1
            # перемещаем частицу
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            # убиваем, если частица ушла за экран
            if not self.rect.colliderect(screen_rect):
                self.kill()


class Stones(pygame.sprite.Sprite):  # Класс спавна камней
    stone_picture = [load_image('Objects/stone3.png'), load_image('Objects/stone.png'),
                     load_image('Objects/stone2.png')]

    def __init__(self, x1, y):
        super().__init__(stone_sprite, all_sprites)
        self.a = random.choice(self.stone_picture)
        self.image = self.a
        self.rect = self.image.get_rect()
        self.x, self.y = random.randint(-10, 690), -200
        self.rect.x, self.rect.y = self.x, self.y

        self.pl_pos = x1, y
        self.is_defeat = True

    def update(self):
        global pause, defeat, defeat_background_time, scores
        if pygame.sprite.collide_mask(self, tree):
            self.kill()
        if not defeat:
            if self.rect.collidepoint(self.pl_pos):
                if self.a:
                    scores += 2
                    self.a = False
                    ExtraPoints(self.rect.x + 10, self.rect.y, 1)
        if defeat:
            if scores >= 100:
                self.rect.y += 12
            elif scores <= 100:
                self.rect.y += 10

            if defeat_background_time <= 0.5:
                self.rect.x -= 6
            elif 0.5 <= defeat_background_time <= 1.5:
                self.rect.x += 6
            elif 1.5 <= defeat_background_time <= 2:
                self.rect.x -= 6
            else:
                self.rect.x = self.x
        if not pygame.sprite.collide_mask(self, character):
            if pause:
                self.rect.y += 0
            elif scores >= 100:
                if not raise_clock:
                    self.rect.y += 12
                else:
                    self.rect.y += 7
            elif scores <= 100:
                if not raise_clock:
                    self.rect.y += 10
                else:
                    self.rect.y += 7
            if self.rect.y > 700:
                self.kill()
        else:
            self.kill()
            if defeat:
                if scores >= 100:
                    self.rect.y += 12
                elif scores <= 100:
                    self.rect.y += 10
            pause = True
            if self.is_defeat:
                defeat = True
                self.is_defeat = False
        if new_game:
            self.kill()


class Present(pygame.sprite.Sprite):  # Подарок за который дают 10 очков
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('Objects/present.png')
        self.rect = self.image.get_rect()
        self.x, self.y = random.randint(0, 660), -200
        self.rect.x, self.rect.y = self.x, self.y
        self.time = 0

    def update(self):
        global scores, pause, defeat, new_gifts

        if not pause or defeat:  # Анимация
            self.time += 0.1
            if self.time <= 2:
                self.rect.y += 1
            elif 2 <= self.time <= 4:
                self.rect.y -= 1
            else:
                self.time = 0

        if pygame.sprite.collide_mask(self, tree) or pygame.sprite.collide_mask(self, stone):
            self.rect.x, self.rect.y = random.randint(0, 660), -200
        if defeat:
            if scores >= 100:
                self.rect.y += 12
            elif scores <= 100:
                self.rect.y += 10
            if defeat_background_time <= 0.5:
                self.rect.x -= 6
            elif 0.5 <= defeat_background_time <= 1.5:
                self.rect.x += 6
            elif 1.5 <= defeat_background_time <= 2:
                self.rect.x -= 6
            else:
                self.rect.x = self.x
        if not pygame.sprite.collide_mask(self, character):
            if pause:
                self.rect.y += 0
            elif scores >= 100:
                if not raise_clock:
                    self.rect.y += 12
                else:
                    self.rect.y += 7
            elif scores <= 100:
                if not raise_clock:
                    self.rect.y += 10
                else:
                    self.rect.y += 7
            if self.rect.y > 700:
                self.kill()
        else:
            ExtraPoints(self.rect.x + 10, self.rect.y, 2)
            scores += 10
            new_gifts += 1
            self.kill()
        if new_game:
            self.kill()


class Clocks(pygame.sprite.Sprite):  # Объект часы которые замедляют время
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('Objects/clock.png')
        self.rect = self.image.get_rect()
        self.x, self.y = random.randint(0, 650), -200
        self.rect.x, self.rect.y = self.x, self.y
        self.time = 0
        self.raise_clock2 = True

    def update(self):
        global scores, pause, defeat, raise_clock, new_clocks

        if not pause or defeat:  # Анимация
            self.time += 0.1
            if self.time <= 2:
                self.rect.y += 1
            elif 2 <= self.time <= 4:
                self.rect.y -= 1
            else:
                self.time = 0

        if pygame.sprite.collide_mask(self, tree) or pygame.sprite.collide_mask(self, stone):
            self.rect.x, self.rect.y = random.randint(0, 650), -200
        if defeat:
            if scores >= 100:
                self.rect.y += 12
            elif scores <= 100:
                self.rect.y += 10
            if defeat_background_time <= 0.5:
                self.rect.x -= 6
            elif 0.5 <= defeat_background_time <= 1.5:
                self.rect.x += 6
            elif 1.5 <= defeat_background_time <= 2:
                self.rect.x -= 6
            else:
                self.rect.x = self.x
        if not pygame.sprite.collide_mask(self, character):
            if pause:
                self.rect.y += 0
            elif scores >= 100:
                if not raise_clock:
                    self.rect.y += 12
                else:
                    self.rect.y += 7
            elif scores <= 100:
                if not raise_clock:
                    self.rect.y += 10
                else:
                    self.rect.y += 7
            if self.rect.y > 700:
                self.kill()
        else:
            self.kill()
            if self.raise_clock2:
                raise_clock = True
                new_clocks += 1
                self.raise_clock2 = False
            if defeat:
                if scores >= 100:
                    self.rect.y += 12
                elif scores <= 100:
                    self.rect.y += 10
        if new_game:
            self.kill()


class Text(pygame.sprite.Sprite):  # Вывод текста с результатами при поражении
    def __init__(self, text, pos, antialias, color, size1, font='data/font.ttf'):
        super().__init__(loading_sprite, all_sprites)
        self.font = pygame.font.Font(font, size1)
        self.image = self.font.render(text, antialias, color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def update(self):
        self.kill()


class Text2(pygame.sprite.Sprite):  # Написание текста в настройках
    def __init__(self, text, pos, antialias, color, size1, font='data/font.ttf'):
        super().__init__(loading_sprite, all_sprites)
        self.font = pygame.font.Font(font, size1)
        self.image = self.font.render(text, antialias, color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.time = 0

    def update(self):
        if main_settings_open:
            if self.time <= 4:
                self.time += 0.1
                self.rect.y -= 10
        else:
            if self.time >= 0:
                self.time -= 0.1
                self.rect.y += 10


class Wind(pygame.sprite.Sprite):  # Частицы ветра
    # сгенерируем частицы разного размера
    fire = [load_image("Objects/windParticle.png")]
    for scale in (3, 8, 10):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def update(self):
        if not pause:
            self.rect.x += 15
            self.rect.y += 10
        # убиваем, если частица ушла за экран
        if self.rect.x > 700 or self.rect.y > 700 or loading or defeat:
            self.kill()


def create_particles(position):  # Создаем частицы
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


# Кнопки
start_button = ImageButton(191, 310, 318, 89, '', 'Buttons/startbtn1.png', 'Buttons/startbtn2.png',
                           'Buttons/startbtn3.png', 'data/Music/buttonsound.mp3')

exit_button = ImageButton(191, 420, 318, 89, '', 'Buttons/exitbtn1.png', 'Buttons/exitbtn2.png',
                          'Buttons/exitbtn3.png', 'data/Music/buttonsound.mp3')

settings2_button = ImageButton(173, 530, 354, 89, '', 'Buttons/mainsettingbtn1.png', 'Buttons/mainsettingbtn2.png',
                               'Buttons/mainsettingbtn3.png', 'data/Music/buttonsound.mp3')

pygame.display.set_icon(load_image('profile.png'))
pygame.display.set_caption('Thrill Slope ⛷️')

# Скачивание данных из файла
with open('data/data.txt', mode='r', encoding='utf-8') as file:
    data1 = file.readlines()
    kol = 0
    try:
        for b in range(len(data1)):
            if data1[kol][0] == '#':
                data1.pop(kol)
            kol += 1
    except IndexError:
        pass
for x in range(len(data1)):
    data1[x] = data1[x].strip()
all_scores, all_gifts, all_clocks, all_defeats = data1[0], data1[1], data1[2], data1[3]
new_gifts, new_clocks, new_defeats = 0, 0, int(all_defeats)

if __name__ == '__main__':
    # Спрайты
    all_sprites = pygame.sprite.Group()
    character_sprite = pygame.sprite.Group()
    tree_sprite = pygame.sprite.Group()
    stone_sprite = pygame.sprite.Group()
    buttons_sprite = pygame.sprite.Group()
    background_pause_sprite = pygame.sprite.Group()
    loading_sprite = pygame.sprite.Group()

    # Скачивание нужных файлов
    background = load_image('Background/background.png')

    # Нужные переменные
    main_settings_open = False  # Открыты ли настройки
    background_x, background_y, background_time, background_speed = -100, 0, 0, 0  # Фон
    trace_y = 740  # След за персонажем
    player_x, player_y, player_speed, start = 325, 700, 10, 0  # Игрок
    pause, background_pause_y, background_pause_time, defeat_background_time = True, 0, 0, 0  # Пауза
    new_game, new_game2 = True, True  # Начальный фон
    loading, loading_time = False, 0  # Анимация загрузки
    settings1_window_open = False  # Открываем меню паузы в игре
    defeat, defeat_x1, defeat_x2, defeat_x3, defeat_time, defeat_bg_y, k = False, -720, -720, -720, 0, 0, 0  # Поражение
    wind_particles = 0  # Частицы ветра
    time_score = 0  # Количество очков даваемых за время пока игрок жив
    spawn_presents = 0  # Количество подарков на карте
    quantity_tree, quantity_stone = 0, 0  # Количество объектов на карте
    raise_clock, spawn_clock, time_passed = False, 0, 0  # Объект часы
    defeat_music_play, clock_sound, clock_time = 0, False, 0  # Музыка
    # Музыка
    music_play, music_play2, music_play3, music_play4, defeat_notmusic_play, notmusicdefeat = True, 0, 0, 0, False, 0
    bg_music = pygame.mixer.Sound('data/Music/bgMusic.mp3')
    defeat_music = pygame.mixer.Sound('data/Music/defeatMusic.mp3')
    clockSound = pygame.mixer.Sound('data/Music/clockSound.mp3')

    # Кнопки спрайты
    settings1_button = ButtonPause1(635, 10, 63, 63, 'Buttons/settingbtn1.png',
                                    'Buttons/settingbtn2.png', None, 'data/Music/buttonsound.mp3')
    play_button = ButtonPause2(316, 766, 68, 68, 'Buttons/playbtn.png', 'Buttons/playbtn2.png',
                               None, 'data/Music/buttonsound.mp3')
    sound_pause_btn = ButtonPause2(231, 773, 55, 59, 'Buttons/soundbtn.png', 'Buttons/soundbtn2.png',
                                   'Buttons/soundbtn3.png', 'data/Music/buttonsound.mp3')
    small_exit_btn = ButtonPause2(411, 773, 55, 59, 'Buttons/smallexitbtn1.png', 'Buttons/smallexitbtn2.png',
                                  'Buttons/smallexitbtn3.png', 'data/Music/buttonsound.mp3')
    start_again_button = ButtonDefeat(316, 770, 68, 68, 'Buttons/playbtn.png', 'Buttons/playbtn2.png',
                                      None, 'data/Music/buttonsound.mp3')
    sound_defeat_btn = ButtonDefeat(231, 780, 55, 59, 'Buttons/soundbtn.png', 'Buttons/soundbtn2.png',
                                    'Buttons/soundbtn3.png', 'data/Music/buttonsound.mp3')
    small_defeat_btn = ButtonDefeat(411, 780, 55, 59, 'Buttons/smallexitbtn1.png', 'Buttons/smallexitbtn2.png',
                                    'Buttons/smallexitbtn3.png', 'data/Music/buttonsound.mp3')

    settings_screen = ButtonsMainSettings(131, 710, 438, 315, 'Background/settingsScreen.png')
    exit_settings_btn = ButtonsMainSettings(160, 930, 380, 70, 'Buttons/exitsettingsbtn1.png', 'Buttons'
                                                                                               '/exitsettingsbtn2.png',
                                            'Buttons/exitsettingsbtn3.png', 'data/Music/buttonsound.mp3')
    setting_text1 = Text2(f'Max. scores: {all_scores}', (155, 755), False, (0, 0, 0), 35)
    setting_text2 = Text2(f'Number of rounds: {all_defeats}', (155, 800), False, (0, 0, 0), 35)
    setting_text3 = Text2('«Restart the game to update the data»', (195, 735), False, (0, 0, 0), 15)
    musicText = ButtonsMainSettings(180, 860, 218, 51, 'Background/musicText.png')
    sound_settings_btn = ButtonsMainSettings(440, 850, 73, 70, 'Buttons/settingssoundbtn1.png',
                                             'Buttons/settingssoundbtn2.png', None, 'data/Music/buttonsound.mp3')

    running = True
    while running:
        all_sprites.update()
        buttons_sprite.update()
        background_pause_sprite.update()
        loading_sprite.update()
        screen.fill((0, 0, 0))
        screen.blit(background, (background_x, background_y - 17200))  # Задний фон

        # Обрабатывание нажатие кнопок
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.USEREVENT and event.button == exit_button
                    or event.type == pygame.USEREVENT and event.button == small_exit_btn or event.type ==
                    pygame.USEREVENT and event.button == small_defeat_btn):
                running = False
            if event.type == pygame.USEREVENT and event.button == start_button:
                new_game, new_game2 = False, False
                pause = False
            if event.type == pygame.USEREVENT and event.button == settings1_button:
                pause = True
                settings1_window_open = True
            if event.type == pygame.USEREVENT and event.button == play_button:
                pause = False
                settings1_window_open = False
            if event.type == pygame.USEREVENT and event.button == start_again_button:
                defeat, defeat_x1, defeat_x2, defeat_x3, defeat_time, defeat_bg_y = False, -720, -720, -720, 0, 0
                start = 0
                player_y, player_x, trace_y = 700, 325, 750
                loading, new_game = True, True
            if event.type == pygame.USEREVENT and event.button == sound_defeat_btn:
                if music_play3 == 0:
                    music_play = False
                    music_play3 += 1
                else:
                    music_play = True
                    music_play3 = 0
            if event.type == pygame.USEREVENT and event.button == sound_pause_btn:
                if music_play3 == 0:
                    music_play = False
                    music_play3 += 1
                else:
                    music_play = True
                    music_play3 = 0
            if event.type == pygame.USEREVENT and event.button == sound_settings_btn:
                if music_play3 == 0:
                    music_play = False
                    music_play3 += 1
                else:
                    music_play = True
                    music_play3 = 0
            if event.type == pygame.USEREVENT and event.button == settings2_button:
                main_settings_open = True
            if event.type == pygame.USEREVENT and event.button == exit_settings_btn:
                main_settings_open = False

            # Передаем ивенты кнопкам
            if new_game:
                if not main_settings_open:
                    start_button.handle_event(event)
                    exit_button.handle_event(event)
                    settings2_button.handle_event(event)
                else:
                    exit_settings_btn.handle_event(event)
                    sound_settings_btn.handle_event(event)
            if defeat:
                start_again_button.handle_event(event)
                sound_defeat_btn.handle_event(event)
                small_defeat_btn.handle_event(event)
            else:
                if not pause:
                    settings1_button.handle_event(event)
                play_button.handle_event(event)
                sound_pause_btn.handle_event(event)
                small_exit_btn.handle_event(event)

        if music_play:  # Проигрывание фоновой музыки
            if not defeat_notmusic_play:
                if music_play2 == 0:
                    music_play2 += 1
                    bg_music.play(-1)
        else:
            bg_music.stop()
            music_play2 = 0

        # Создание частиц ветра
        if not new_game:
            wind_particles += 0.1
            if wind_particles == 0.4:
                if not pause:
                    Wind((0, random.choice(range(-350, 600))))
            elif wind_particles > 0.4:
                wind_particles = 0

        if loading:  # Анимация загрузки
            if loading_time <= 4:
                Loading(loading_time)
                LoadingText(loading_time)
                loading_time += 0.1
            else:
                loading_time = 0
                loading = False
                new_game2 = True

        if clock_sound:  # Звук при поднятии часов
            clockSound.play()
            clock_sound = False

        if raise_clock:  # "Замедляем время" при поднятии часов
            if not defeat:
                FONT2.render_to(screen, (270, 4), 'Оставшееся время', (0, 0, 0))
                FONT3.render_to(screen, (320, 20), str(int(time_passed)) + '/50', (0, 0, 0))
            background_speed = 7
            if not pause:
                if clock_time == 0:
                    clock_sound = True
                    clock_time += 1
                time_passed += 0.1
                if time_passed > 50:
                    time_passed = 0
                    raise_clock = False
        else:
            clock_time = 0

        if defeat:  # Поражение
            notmusicdefeat = 0
            clockSound.stop()
            if defeat_music_play == 0:
                bg_music.stop()
                defeat_music.play()
                defeat_music_play, defeat_notmusic_play = 1, True

            start_again_button.check_hover(pygame.mouse.get_pos())
            sound_defeat_btn.check_hover(pygame.mouse.get_pos())
            small_defeat_btn.check_hover(pygame.mouse.get_pos())
            if k == 0:  # Создание частиц
                create_particles((player_x, player_y))
                new_defeats += 1
                all_gifts = new_gifts + int(all_gifts)
                all_clocks = new_clocks + int(all_clocks)
                k += 1
            # Записываем данные в файл
            if scores > int(all_scores):
                all_scores = scores
            with open('data/data.txt', mode='w', encoding='utf-8') as new_reports:
                new_reports.write(f'# Максимальное количество очков:\n{all_scores}\n# Количество собранных подарков:\n')
                new_reports.write(f'{all_gifts}\n# Количество собранных часов:\n{all_clocks}\n')
                new_reports.write(f'# Общее количество поражений:\n{new_defeats}')

            if defeat_background_time <= 0.5:
                background_x -= 6
                defeat_background_time += 0.1
            elif 0.5 <= defeat_background_time <= 1.5:
                background_x += 6
                defeat_background_time += 0.1
            elif 1.5 <= defeat_background_time <= 2:
                background_x -= 6
                defeat_background_time += 0.1
            else:
                background_x = -100

            # Выводим окошечко с результатами
            second, third = False, False
            if defeat_time <= 1.2:
                defeat_bg_y -= 7.5
            DefeatBackground(defeat_bg_y)
            if defeat_x1 < 0:
                defeat_x1 += 30
            if 0.8 <= defeat_time:
                second = True
            if 1.3 <= defeat_time:
                third = True
            if second:
                if defeat_x2 < 0:
                    defeat_x2 += 30
            if third:
                if defeat_x3 < 0:
                    defeat_x3 += 30

            # Таблички с результатами
            Defeat(defeat_x1, 90)
            Text(f'Очки: {scores}', (defeat_x1 + 225, 96), False, (255, 255, 255), 58)
            Defeat(defeat_x2, 210)
            Text(f'Собрано подарков: {new_gifts}', (defeat_x2 + 130, 220), False, (255, 255, 255), 45)
            Defeat(defeat_x3, 330)
            Text(f'Собрано часов: {new_clocks}', (defeat_x2 + 140, 340), False, (255, 255, 255), 50)
            defeat_time += 0.1

            background_y += background_speed
            if 1.5 <= background_time <= 3:
                background_time += 0.1
                background_speed = 3
            if 3 <= background_time:
                if scores >= 100:
                    quantity_stone += 0.1
                    quantity_tree += 0.1
                    background_speed = 12
                    if quantity_tree > 1:
                        tree = Tree(player_x, player_y)
                        quantity_tree = 0
                    if quantity_stone > 3:
                        stone = Stones(player_x, player_y)
                        quantity_stone = 0
                else:
                    # Количество объектов на карте(елки, камни ...)
                    quantity_stone += 0.1
                    quantity_tree += 0.1
                    background_speed = 10
                    if quantity_tree > 1:
                        tree = Tree(player_x, player_y)
                        quantity_tree = 0
                    if quantity_stone > 3:
                        stone = Stones(player_x, player_y)
                        quantity_stone = 0

        # Начальный экран с кнопками
        if new_game:
            defeat, defeat_background_time, k, raise_clock, time_passed = False, 0, 0, False, 0
            scores, new_gifts, new_clocks = 0, 0, 0
            defeat_music_play, defeat_notmusic_play = 0, False
            if notmusicdefeat == 0:
                music_play2 = 0
                notmusicdefeat += 1
            if new_game2:
                Background()
                start_button.check_hover(pygame.mouse.get_pos())
                start_button.draw(screen)
                exit_button.check_hover(pygame.mouse.get_pos())
                exit_button.draw(screen)
                settings2_button.check_hover(pygame.mouse.get_pos())
                settings2_button.draw(screen)
                exit_settings_btn.check_hover(pygame.mouse.get_pos())
                sound_settings_btn.check_hover(pygame.mouse.get_pos())

        if not pause:  # Пауза в игре
            settings1_button.check_hover(pygame.mouse.get_pos())

            # Счет и отображение очков
            if time_score <= 1:
                time_score += 0.01
            elif time_score >= 1:
                time_score = 0
                scores += 1
            FONT.render_to(screen, (15, 15), str(scores), (0, 0, 0))

            # Ускорение заднего фона
            background_y += background_speed
            if background_time <= 0.5:
                background_speed = 0.5
                background_time += 0.1
            if 0.5 <= background_time <= 1:
                background_time += 0.1
                background_speed = 1
            if 1 <= background_time <= 1.5:
                background_time += 0.1
                background_speed = 2
            if 1.5 <= background_time <= 3:
                background_time += 0.1
                background_speed = 3
            if 3 <= background_time:
                if scores >= 100:
                    # Количество объектов на карте(елки, камни ...)
                    quantity_stone += 0.1
                    quantity_tree += 0.1
                    background_speed = 12
                    if quantity_tree > 1:
                        tree = Tree(player_x, player_y)
                        quantity_tree = 0
                        spawn_presents += 0.1
                        if spawn_presents > 6:
                            present = Present()
                            spawn_presents = 0
                    if quantity_stone > 3:
                        stone = Stones(player_x, player_y)
                        quantity_stone = 0
                        spawn_clock += 0.1
                        if spawn_clock > 3:
                            spawn_clock = 0
                            clocks = Clocks()
                else:
                    # Количество объектов на карте(елки, камни ...)
                    quantity_stone += 0.1
                    quantity_tree += 0.1
                    background_speed = 10
                    if quantity_tree > 1:
                        tree = Tree(player_x, player_y)
                        quantity_tree = 0
                        spawn_presents += 0.1
                        if spawn_presents > 6:
                            present = Present()
                            spawn_presents = 0
                    if quantity_stone > 3:
                        stone = Stones(player_x, player_y)
                        quantity_stone = 0
                        spawn_clock += 0.1
                        if spawn_clock > 3:
                            spawn_clock = 0
                            clocks = Clocks()
            keys = pygame.key.get_pressed()
            # Меняем картинку если персонаж едет влево и вправо
            if keys[pygame.K_LEFT] or keys[pygame.K_a] and player_x > 1:
                if start <= 2:  # Игрок в начале выезжает
                    player_y -= 13
                    start += 0.1
                    trace_y -= 13
                player_x -= player_speed
                trace = Trace(player_x + 20, trace_y)
                character = Character(1, player_x, player_y)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_x < 660:
                if start <= 2:  # Игрок в начале выезжает
                    player_y -= 13
                    start += 0.1
                    trace_y -= 13
                player_x += player_speed
                trace = Trace(player_x, trace_y)
                character = Character(2, player_x, player_y)
            else:
                if start <= 2:  # Игрок в начале выезжает
                    player_y -= 13
                    start += 0.1
                    trace_y -= 13
                trace = Trace(player_x, trace_y)
                character = Character(3, player_x, player_y)

        else:
            trace = Trace(player_x, trace_y)
            if pause:  # Останавливаем персонажа при паузе
                character = Character(3, player_x, player_y)
            if defeat:  # Когда персонаж сталкивается с объектом
                if player_y < 790:
                    player_y += 13
                    trace_y += 13
                character = Character(3, player_x, player_y)

        if settings1_window_open:  # Анимация выхода паузы
            if background_pause_time <= 1.2:
                background_pause_time += 0.1
                background_pause_y -= 7.5
            play_button.check_hover(pygame.mouse.get_pos())
            sound_pause_btn.check_hover(pygame.mouse.get_pos())
            small_exit_btn.check_hover(pygame.mouse.get_pos())
            PauseBackground(background_pause_y)
        else:
            if background_pause_time >= 0:
                background_pause_time -= 0.1
                background_pause_y += 7.5
                play_button.check_hover(pygame.mouse.get_pos())
                sound_pause_btn.check_hover(pygame.mouse.get_pos())
                small_exit_btn.check_hover(pygame.mouse.get_pos())
                PauseBackground(background_pause_y)
        if background_y >= 17150:  # Обновление заднего фона если он закончился
            background_y = 0

        all_sprites.draw(screen)
        buttons_sprite.draw(screen)
        background_pause_sprite.draw(screen)
        loading_sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
