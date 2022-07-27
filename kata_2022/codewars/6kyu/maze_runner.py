MOVE = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}


def maze_runner(maze, directions):
    row, col = _get_start_point(maze, directions)
    max_maze_length = len(maze)

    for direction in directions:
        col, row = _move(direction, col, row)

        is_go_outside = not (0 <= row < max_maze_length) or not (0 <= col < max_maze_length)
        if is_go_outside or maze[row][col] == 1:
            return "Dead"

        is_arrive_finish = maze[row][col] == 3
        if is_arrive_finish:
            return "Finish"

    return "Lost"


def _move(direction, col, row):
    dy, dx = MOVE[direction]
    row += dy
    col += dx
    return col, row


def _get_start_point(maze, directions):
    return next((i, j) for i, positions in enumerate(maze) for j, position in enumerate(positions) if maze[i][j] == 2)


def test_maze_runner():
    maze = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1],
    ]
    assert maze_runner(maze, ["N", "N", "N", "W", "W"]) == "Dead"
    assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "S", "S", "S", "S"]) == "Dead"
    assert maze_runner(maze, ["W"]) == "Dead"

    assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"]) == "Finish"
    assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "S", "S", "E", "E", "N", "N", "E"]), "Finish"
    assert maze_runner(maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E", "W", "W"])

    assert maze_runner(maze, ["N", "E", "E", "E", "E"]) == "Lost"
