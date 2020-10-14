# data = input("Imput grid size(1-9): ")

EMPTY = " "

def print_output(problem_grid):
    for row in range(len(problem_grid)):
        for x in range(len(problem_grid)):
            print("---", end=" ")
        print("")
        for column in range(len(problem_grid)):
            print("|" + str(problem_grid[row][column]) + "|", end=" ")
        print("")
    for x in range(len(problem_grid)):
        print("---", end=" ")
    print("")


# print_output([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# print_output([[0, 0], [0, 0]])
# print_output([[EMPTY, EMPTY], [EMPTY, EMPTY]])
# print_output([[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]])
# print_output([[1, 2], [2, 1]])
# print_output([[1, 2], [EMPTY, 1]])


def is_solved(problem_grid):
    if check_for_blank_cells(problem_grid):
        return False
    for row in range(len(problem_grid)):
        if check_duplicate_in_row(problem_grid[row]):
            return False
    if check_duplicate_in_column(problem_grid):
        return False

    return True


def check_for_blank_cells(problem_grid):
    for row in range(len(problem_grid)):
        for column in range(len(problem_grid)):
            if problem_grid[row][column] == EMPTY:
                return True
    return False


def check_duplicate_in_row(row):
    return len(set(row)) < len(row)


def check_duplicate_in_column(problem_grid):
    rows = len(problem_grid)
    if rows == 0:
        return False
    for row in range(len(problem_grid)):
        columns = len(problem_grid[row])
        if rows != columns:
            return True

    for row in range(len(problem_grid)):
        columnSet = set()
        for column in range(len(problem_grid[0])):
            columnSet.add(problem_grid[column][row])

        if len(columnSet) != len(problem_grid[0]):
            return True
    return False


assert check_for_blank_cells([[1]]) == False
assert is_solved([[1]]) == True
assert is_solved([[EMPTY]]) == False

assert check_duplicate_in_row([]) == False
assert check_duplicate_in_row([1]) == False
assert check_duplicate_in_row([1, 2]) == False
assert check_duplicate_in_row([2, 1]) == False
assert check_duplicate_in_row([1, 1]) == True
assert check_duplicate_in_row([2, 1, 3]) == False
assert check_duplicate_in_row([2, 3, 3]) == True
assert check_duplicate_in_row([1, EMPTY]) == False
assert check_duplicate_in_row([EMPTY, EMPTY]) == True

assert check_duplicate_in_column([]) == False
assert check_duplicate_in_column([[1, 1], [1]]) == True

assert check_duplicate_in_column([[1]]) == False
assert check_duplicate_in_column([[1, 2], [2, 1]]) == False
assert check_duplicate_in_column([[1, 2], [1, 3]]) == True
assert check_duplicate_in_column([[1, 2], [1, 2]]) == True
assert check_duplicate_in_column([[EMPTY, EMPTY], [EMPTY, EMPTY]]) == True


assert is_solved([[1, 2], [EMPTY, 1]]) == False
assert is_solved([[1, 1], [1, 1]]) == False
assert is_solved([[1, 2], [1, 1]]) == False
assert is_solved([[1, 3], [1, 3]]) == False
assert is_solved([[1, 3], [2, 3]]) == False

assert is_solved([[1, 2], [2, 1]]) == True

assert is_solved([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == False
assert is_solved([[1,2,3], [2,3,1], [3,1,EMPTY]]) == False
assert is_solved([[1,2,3], [2,3,1], [3,1,2]]) == True

assert is_solved([[1,1,3], [2,3,1], [3,1,2]]) == False
assert is_solved([[1,2,3], [1,3,1], [3,1,2]]) == False


assert is_solved([[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]]) == True
assert is_solved([[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,EMPTY]]) == False

assert is_solved([[1,2,3,1], [2,3,4,1], [3,4,1,2], [4,1,2,3]]) == False

