import pygame
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = pygame.Color('white')

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                    pygame.draw.rect(screen, self.color, (i * self.cell_size + self.left, j * self.cell_size + self.left,
                                                          self.cell_size, self.cell_size), 1)

    def get_cell(self, x, y):
        x1, y1 = (x - self.left) // self.cell_size, (y - self.left) // self.cell_size
        if x1 < 0 or y1 < 0 or x1 >= self.width or y1 >= self.height:
            return None
        return (x1, y1)

    # смена цветов клеток на поле
    def on_click(self, cell_coords):
        x, y = cell_coords
        cnt = 0
        print(self.board)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.board[y + j][x + i] == 10:
                    cnt += 1
        print(cnt)


    def get_click(self, mouse_pos):
        cell = self.get_cell(*mouse_pos)
        if cell:
            self.on_click(cell)

    # рисование поля
    def draw(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 10:
                    pygame.draw.rect(screen, 'red',
                                     (j * self.cell_size + self.left + 1, i * self.cell_size + self.left + 1,
                                      self.cell_size - 2, self.cell_size - 2))

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


class Minesweeper(Board):
    def __init__(self, width, height, mines):
        super().__init__(width, height)
        self.width, self.height, self.mines = width, height, mines
        self.change_board()

    def change_board(self):
        i = 0
        while i < self.mines:
            if self.board[random.randrange(self.height)][random.randrange(self.width)] == -1:
                self.board[random.randrange(self.height)][random.randrange(self.width)] = 10
            i += 1
        print(self.board)

    def open_cell(self):
        pass


# поле 5 на 7
board = Board(10, 15)
sweeper = Minesweeper(10, 15, 10)
board.set_view(20, 20, 40)
sweeper.set_view(20, 20, 40)
pygame.init()
screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption('Чёрное в белое и наоборот')
running = True
while running:
    sweeper.render(screen)
    sweeper.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            board.get_click(event.pos)

    pygame.display.flip()