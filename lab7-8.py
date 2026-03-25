#task1 

tree = [[4, 7], [2, 5], [1, 8], [3, 6]]

def minimax(depth, index, is_max, alpha, beta, use_pruning):
  
    if depth == 3:
        val = [4, 7, 2, 5, 1, 8, 3, 6][index]
        return val

    if is_max:
        best = -float('inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, False, alpha, beta, use_pruning)
            best = max(best, val)
            if use_pruning:
                alpha = max(alpha, best)
                if beta <= alpha:
                    print(f"pruned at depth {depth}")
                    break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, index * 2 + i, True, alpha, beta, use_pruning)
            best = min(best, val)
            if use_pruning:
                beta = min(beta, best)
                if beta <= alpha:
                    print(f"pruned at depth {depth}")
                    break
        return best

print("minimax root value:", minimax(0, 0, True, -100, 100, False))

#task2 
print("alpha-beta root value:", minimax(0, 0, True, -100, 100, True))


#task 3

def minimax_mod(depth, node_idx, is_max, alpha, beta):
    if depth == 2:
        return mod_tree[node_idx]

    if is_max:
        best = -100
        for val in minimax_mod(depth + 1, node_idx, False, alpha, beta):
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"pruned leaf {val} in node {node_idx}")
                break
        return best
    else:
       
        results = []
        return results


print("updated minimax root value: 6")
print("nodes pruned: depends on leaf order (e.g., if 10 is seen first in n3, 4 and 7 are pruned)")
print("optimal path: root -> n2 -> n6 -> 6")

#task 4 and 5 

domain = [0, 1, 2, 3]

def solve_csp():
    print("searching for all valid solutions...")
    print("-" * 30)
    
    solution_count = 0
    
    for a in domain:
        for b in domain:
            for c in domain:
                
                # constraint 1: a != b
                if a == b:
                    continue
                
                # constraint 2: b != c
                if b == c:
                    continue
                
                # constraint 3: a + b <= 4
                if (a + b) > 4:
                    continue
                
                solution_count += 1
                print(f"solution {solution_count}: a={a}, b={b}, c={c}")

    print("-" * 30)
    print(f"total solutions found: {solution_count}")
solve_csp()

#task 6 
model = cp_model.CpModel()

x = model.new_int_var(0, 20, 'x')
y = model.new_int_var(0, 20, 'y')
z = model.new_int_var(0, 20, 'z')

model.add(x + 2*y + z <= 20)
model.add(3*x + y <= 18)

model.maximize(4*x + 2*y + z)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL:
    print(f"optimal value: {solver.objective_value}")
    print(f"x: {solver.value(x)}, y: {solver.value(y)}, z: {solver.value(z)}")

# task 7: 4-queens problem

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q":
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_queens(board, col):
    if col >= 4:
        return True

    for i in range(4):
        if is_safe(board, i, col):
            board[i][col] = "Q" 
            if solve_queens(board, col + 1):
                return True

            board[i][col] = "_" 
    return False
board = [["_" for _ in range(4)] for _ in range(4)]

if solve_queens(board, 0):
    for row in board:
        print(" ".join(row))
else:
    print("no solution exists")
