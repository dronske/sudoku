import random

def empty():
    empty_row = []
    for i in range(9):
        empty_row.append(0)
    empty_puzzle = []
    for i in range(9):
        empty_puzzle.append(empty_row)
    return empty_puzzle

def gen_poss():
    poss = []
    for i in range(1,10):
        poss.append(i)
    return poss

def check_row(puzzle, ind):
    row = puzzle[ind[0]]
    new = row[ind[1]]
    valid = True
    for i in range(9):
        if(row[i] == new) and (i != ind[1]):
            valid = False
    return valid

def check_col(puzzle, ind):
    col = []
    for i in range(9):
        col.append(puzzle[i][ind[1]])
    new = col[ind[0]]
    valid = True
    for i in range(9):
        if(col[i] == new) and (i != ind[0]):
            valid = False
    return valid

def check_sq(puzzle, ind):
    return True

def check_all(puzzle, ind):
    return check_row(puzzle, ind) and check_col(puzzle, ind) and check_sq(puzzle, ind)

def generate():
    puzzle = empty()
    for x in range(9):
        for y in range(9):
            poss = gen_poss()
            while(not(check_all(puzzle, (x,y)))):
                print(poss)
                to_try = random.choice(poss)
                puzzle[x][y] = to_try
                if not(check_all(puzzle, (x,y))):
                    poss.remove(to_try)
    return puzzle

def display(puzzle):
    for x in range(9):
        row_str = "";
        for y in range(9):
            row_str += str(puzzle[x][y]) + " "
        print(row_str)

if __name__ == "__main__":
    display(generate())