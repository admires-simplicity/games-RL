import copy

class node:
    def __init__(self, initial_state):
        self.total = 0
        self.visits = 0
        self.state = copy.deepcopy(initial_state)
        self.children = []

    def __str__(self):
        return f'{self.state}'

def MCTS(initial_state, iterations):

    root = node(initial_state)
    current = root

    for i in range(iterations):
        # tree traversal
        while current.visits != 0:
            # ...
            pass
        # node expansion

        # rollout (random simulation)
        # backpropagation

board = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] 

#MCTS(board, 10)

lel = node(board)

print(lel)
