def create_sapper_field(n, m, mines):
    field = [[0 for _ in range(m)] for _ in range(n)]
    print(field)

    for mine in mines:
        row, col = mine
        field[row][col] = "*"

        # Увеличиваем значение соседних клеток на 1
        for i in range(max(0, row - 1), min(n, row + 2)):
            for j in range(max(0, col - 1), min(m, col + 2)):
                if field[i][j] != "*":
                    field[i][j] += 1

    return field

def print_sapper_field(field):
    for row in field:
        print(" ".join(map(str, row)))

# Пример использования
n = 5  # количество строк
m = 5  # количество столбцов
mines = [(1, 1), (2, 2), (3, 3)]  # координаты мин

field = create_sapper_field(n, m, mines)
print_sapper_field(field)