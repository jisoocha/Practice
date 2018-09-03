def solution(matrix):
    if not matrix:
        return 0

    visited = {(x, y): False for x in range(len(matrix)) for y in range(len(matrix[0]))}
    num_islands = 0

    def visit_island(x, y):
        stack = [(x, y)]
        while stack:
            (w, z) = stack.pop()
            for (a, b) in [(w + 1, z), (w - 1, z), (w, z + 1), (w, z - 1)]:
                if (a, b) not in visited:
                    continue
                elif not visited[(a, b)]:
                    visited[(a, b)] = True
                    if matrix[a][b] == 1:
                        stack.append((a, b))

    for (x, y) in visited:
        if visited[(x, y)]:
            continue
        elif matrix[x][y] == 0:
            visited[(x, y)] = True
        else:
            num_islands += 1
            visit_island(x, y)
    return num_islands


if __name__ == '__main__':
    problem_matrix = [[0, 1, 0, 1, 0],
              [0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1]]

    print(solution(problem_matrix))
