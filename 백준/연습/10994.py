def draw_star(n):
    size = 4 * n - 3
    canvas = [[' '] * size for _ in range(size)]

    def fill_pattern(x, y, n):
        if n == 1:
            canvas[x][y] = '*'
            return
        size = 4 * n - 3
        for i in range(size):
            canvas[x][y + i] = '*'
            canvas[x + size - 1][y + i] = '*' 
            canvas[x + i][y] = '*'
            canvas[x + i][y + size - 1] = '*'
        fill_pattern(x + 2, y + 2, n - 1)

    fill_pattern(0, 0, n)

    for row in canvas:
        print(''.join(row))

N = int(input())
draw_star(N)
