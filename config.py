SCREEN_COLOR = (15, 15, 15) #(0,0,0)
GRID_COLOR = (20,20,20)#(255,255,255)

WIDTH = 612   # Width of game surface
HEIGHT = 612  # Height of game surface
ROWS = 17
COLS = 17
SQUARE_SIZE_X = WIDTH // ROWS
SQUARE_SIZE_Y = HEIGHT // COLS
FPS = 3

Q_SPACE = {(x, y):(x*SQUARE_SIZE_X, y*SQUARE_SIZE_Y, SQUARE_SIZE_X, SQUARE_SIZE_Y)\
                            for x in range(COLS) for y in range(ROWS) }