# Imports 
import random
from math import sqrt

# Variable Declarations
map_maze = {
    'A': {
        'adjacent': [('B', 5)], 
        'point': (1, 1)
    },
    'B': {
        'adjacent': [('A', 5), ('C', 7), ('F', 2)], 
        'point': (1, 6)
    },
    'C': {
        'adjacent': [('B', 7), ('L', 8)], 
        'point': (1, 13)
    },
    'D': {
        'adjacent': [('E', 3)], 
        'point': (3, 1)
    },
    'E': {
        'adjacent': [('D', 3), ('I', 6)],
        'point': (3, 4)
    },
    'F': {
        'adjacent': [('B', 2), ('G', 5), ('J', 6)], 
        'point': (3, 6)
    },
    'G': {
        'adjacent': [('F', 5), ('K', 6)],
        'point': (3, 11)
    },
    'H': {
        'adjacent': [('I', 3)],
        'point': (9, 1)
    },
    'I': {
        'adjacent': [('E', 6), ('J', 2)],
        'point': (9, 4)
    },
    'J': {
        'adjacent': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
        'point': (9, 6)
    },
    'K': {
        'adjacent': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
        'point': (9, 11)
    },
    'L': {
        'adjacent': [('C', 8), ('K', 2), ('U', 9)],
        'point': (9, 13)
    },
    'M': {
        'adjacent': [('N', 3)],
        'point': (11, 1)
    },
    'N': {
        'adjacent': [('M', 3), ('O', 2), ('R', 7)],
        'point': (11, 4)
    },
    'O': {
        'adjacent': [('J', 2), ('N', 2), ('P', 3)],
        'point': (11, 6)
    },
    'P': {
        'adjacent': [('O', 3), ('S', 7)],
        'point': (11, 9)
    },
    'Q': {
        'adjacent': [('R', 3)],
        'point': (18, 1)
    },
    'R': {
        'adjacent': [('N', 7), ('Q', 3), ('S', 5)],
        'point': (18, 4)
    },
    'S': {
        'adjacent': [('P', 7), ('R', 5), ('T', 2)],
        'point': (18, 9)
    },
    'T': {
        'adjacent': [('K', 9), ('S', 2), ('U', 2)],
        'point': (18, 11)
    },
    'U': {
        'adjacent': [('L', 9), ('T', 2)],
        'point': (18, 13)
    }
}

first_state = 'A'
objective_state = 'Q'

visited = [first_state]
result = [first_state]
state_ = first_state
heuristics = {}
value_ = 0

count_cost = 0

#pré calcula as heuristicas de cada ponto até o ponto do objetivo
def calc_heuristics():
    global map_maze

    xGoal, yGoal = map_maze[objective_state]['point']

    for k in map_maze.keys():
        xState, yState = map_maze[k]['point']
        heuristics.update({k : sqrt((xState - xGoal)**2) + ((yState - yGoal)**2)})


    print(heuristics)


# Function declaration
def get_adjacent_not_visited(state_):
    global visited
    global map_maze

    states = map_maze[state_]
    return_ = []

    for s in states['adjacent']:
        if s[0] not in visited:
            return_.append(s)

    return return_
    

def hn(state_):
  return state_[1]

#retorna o proximo estado com base na heuristica dos pontos adjacentes
def get_next_state(list_):
    h = []
    for state in list_:
        h.append((state[0], heuristics[state[0]]))
    
    #print('h', h)

    selected_state = sorted(h, key=hn)[0]

    return selected_state

calc_heuristics()

#Code Implementation
while state_ != objective_state:

    not_visited = get_adjacent_not_visited(state_)
    #print(not_visited)

    if len(not_visited) != 0:

        less_value = float('Inf')
        less_state = ''

        selected_state = get_next_state(not_visited)
        # print(selected_state)

        state_ = selected_state[0]
        value_ = selected_state[1]
        # print('state = ', state_)
        # print('value = ', value_)
        visited.append(state_)
        count_cost += value_
        result.append(state_)
        print(visited)
    else:
        del result[-1]
        state_ = result[-1]
        #count_cost -= value_

#remove os custos dos pontos visitados mas não selecionados
for state in visited:
    if (state not in result):
        count_cost -= heuristics[state]

print("Caminho resultante: %s" % result)
print("Custo do caminho: %s" % count_cost)