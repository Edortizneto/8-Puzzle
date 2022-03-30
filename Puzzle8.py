
from SearchAlgorithms import AEstrela
from Graph import State
import numpy as np
import time
import copy

class Puzzle8(State):

    def __init__(self, board, op, goal):
        self.board = board
        self.operator = op
        self.goal = goal
        
    def env(self):
        return str(self.board)#self.operator+"#"+str(self.cost())

    def sucessors(self):
        sucessors = []
        #self.cost_value += 1
        rows, cols = self.board.shape
        for i in range(rows):
            for j in range(cols):
                if(self.board[i][j] == 0):
                    #move up
                    if (i - 1) >= 0:
                        temp = copy.deepcopy(self.board)
                        #temp = self.board.copy()
                        temp[i][j] = temp[i-1][j]
                        temp[i-1][j] = 0
                        sucessors.append(Puzzle8(temp, 'up', self.goal))
                    #move down
                    if (i + 1) < rows:
                        temp = copy.deepcopy(self.board)
                        #temp = self.board.copy()
                        temp[i][j] = temp[i+1][j]
                        temp[i+1][j] = 0
                        sucessors.append(Puzzle8(temp,'down', self.goal))
                    #move left
                    if (j - 1) >= 0:
                        temp = copy.deepcopy(self.board)
                        #temp = self.board.copy()
                        temp[i][j] = temp[i][j-1]
                        temp[i][j-1] = 0
                        sucessors.append(Puzzle8(temp,'left', self.goal))
                    #move right
                    if (j + 1) < cols:
                        temp = copy.deepcopy(self.board)
                        #temp = self.board.copy()
                        temp[i][j] = temp[i][j+1]
                        temp[i][j+1] = 0
                        sucessors.append(Puzzle8(temp,'right', self.goal))
        return sucessors
    
    def is_goal(self):
        return np.array_equal(self.board, self.goal)

    def description(self):
        return "8 tiles puzzle"
    
    def cost(self):
        #print("cost value = ",self.cost_value)
        return 1 #self.cost_value

    def h(self):
        '''rows, cols = self.board.shape
        erros = 0
        for i in range(rows):
            for j in range(cols):
                if self.board[i,j] != self.goal[i,j] and self.board[i,j] != 0:
                    erros += 1'''
        erros = self.distanciaManhattan()
        erros += 3*self.calcNilsson()
        #print(erros)
        return erros

    def distanciaManhattan(self):
        s = 0
        for num in range(9):
            if num == 0:
                pass
            else:
                y, x = np.where(self.goal == num)
                #print(f"x,y = {x,y}")
                coords = np.where(self.board == num)
                distX = abs(coords[1]-x)
                distY = abs(coords[0]-y)
                distM = distX+distY
                #print(f"Distancia do {num} = {distM}")
                s += distM
        return int(s[0])

    def calcNilsson(self):
        t = 0
        lista = Puzzle8.caracol(self.board)
        for num in range(1,9):
            if lista.index(num) == 8:
                t += 1
            if num+1 > 8:
                num=0
            elif lista.index(num+1) != (lista.index(num))+1%8:
                t += 2
        return t

    def caracol(nplist):
        temp = nplist.tolist()
        final = [e for e in temp[0]]
        final.append(temp[1][2])
        [final.append(e) for e in temp[2][::-1]]
        [final.append(e) for e in temp[1][:2]]
        return final

    # Extraído do site GeeksFoGeeks: 
    #https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    # A utility function to count
    # inversions in given array 'arr[]'
    def isSolvable(self):
        arr = Puzzle8.caracol(self.board)
        inv_count = 0
        empty_value = 0
        for i in range(9):
            for j in range(i+1,9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return (inv_count % 2 == 0)

    def print(self):
        pass #return str(self.operator)


def main():
    print('Busca A*')
    states = [[[1,2,3],[8,0,4],[7,6,5]], # Goal
              [[8,1,3],[0,7,2],[6,5,4]], # Médio
              [[7,8,6],[2,3,5],[1,4,0]], # Difícil
              [[7,8,6],[2,3,5],[0,1,4]], # Difícil
              [[8,3,6],[7,5,4],[2,1,0]], # Difícil
              [[3,4,8],[1,2,5],[7,0,6]], # Impossível
              [[5,4,0],[6,1,8],[7,3,2]]] # Impossível
    init_state = np.array( states[4] )
    final_state = np.array( [[1,2,3],
                             [8,0,4],
                             [7,6,5]] )
    state = Puzzle8(init_state,'',final_state)
    if state.isSolvable():
        algorithm = AEstrela()
        ts = time.time()
        result = algorithm.search(state)
        tf = time.time()
        if result != None:
            print('Achou!')
            print(result.show_path())
            print(f"Em {tf-ts}")
        else:
            print('Nao achou solucao')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()