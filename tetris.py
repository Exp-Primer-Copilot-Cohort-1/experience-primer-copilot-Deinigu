import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Tamaño de la cuadrícula
block_size = 30
grid_width = width // block_size
grid_height = height // block_size

# Definir las piezas del Tetris
pieces = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Clase para representar una pieza
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j]:
                    pygame.draw.rect(screen, WHITE, (self.x * block_size + j * block_size, self.y * block_size + i * block_size, block_size, block_size))

# Función para crear una nueva pieza aleatoria
def create_piece():
    shape = random.choice(pieces)
    x = grid_width // 2 - len(shape[0]) // 2
    y = 0
    return Piece(x, y, shape)

# Función para verificar si una pieza colisiona con los bordes o con otras piezas
def check_collision(piece, grid):
    for i in range(len(piece.shape)):
        for j in range(len(piece.shape[i])):
            if piece.shape[i][j]:
                if piece.x + j < 0 or piece.x + j >= grid_width or piece.y + i >= grid_height or grid[piece.y + i][piece.x + j]:
                    return True
    return False

# Función para actualizar la cuadrícula con las piezas colocadas
def update_grid(piece, grid):
    for i in range(len(piece.shape)):
        for j in range(len(piece.shape[i])):
            if piece.shape[i][j]:
                grid[piece.y + i][piece.x + j] = 1

# Función para eliminar las filas completas de la cuadrícula
def clear_rows(grid):
    full_rows = []
    for i in range(grid_height):
        if all(grid[i]):
            full_rows.append(i)
    for row in full_rows:
        del grid[row]
        grid.insert(0, [0] * grid_width)

# Función principal del juego
def play_game():
    clock = pygame.time.Clock()
    grid = [[0] * grid_width for _ in range(grid_height)]
    piece = create_piece()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    piece.move(-1, 0)
                    if check_collision(piece, grid):
                        piece.move(1, 0)
                elif event.key == pygame.K_RIGHT:
                    piece.move(1, 0)
                    if check_collision(piece, grid):
                        piece.move(-1, 0)
                elif event.key == pygame.K_DOWN:
                    piece.move(0, 1)
                    if check_collision(piece, grid):
                        piece.move(0, -1)
                elif event.key == pygame.K_UP:
                    piece.rotate()
                    if check_collision(piece, grid):
                        piece.rotate()

        piece.move(0, 1)
        if check_collision(piece, grid):
            piece.move(0, -1)
            update_grid(piece, grid)
            clear_rows(grid)
            piece = create_piece()
            if check_collision(piece, grid):
                game_over = True

        screen.fill(BLACK)
        for i in range(grid_height):
            for j in range(grid_width):
                if grid[i][j]:
                    pygame.draw.rect(screen, WHITE, (j * block_size, i * block_size, block_size, block_size))
        piece.draw()
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()

# Iniciar el juego
play_game()