
from SearchAlgorithms import AEstrela
from Puzzle8 import Puzzle8
import numpy as np
import time

line = "--------------------------------------------"
name = "\t 8 Puzzle - Edgard Ortiz Neto "

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
    print("\n")


def path(instrucions,board):
    temp = board.copy() 
    for instruction in instrucions:
        i,j = np.where(temp==0)
        i = int(i[0])
        j = int(j[0])
        matprint(np.array(temp))
        #move up
        if instruction == 'up':
            temp[i][j] = temp[i-1][j]
            temp[i-1][j] = 0
            
        #move down
        elif instruction == 'down':
            temp[i][j] = temp[i+1][j]
            temp[i+1][j] = 0
            
        #move left
        elif instruction == 'left':
            temp[i][j] = temp[i][j-1]
            temp[i][j-1] = 0
            
        #move right
        elif instruction == 'right':
            temp[i][j] = temp[i][j+1]
            temp[i][j+1] = 0
        
        else:
            raise ValueError
        print(" || \n \/")
        
    matprint(np.array(temp))

def main():
    print(line)
    print(name)
    print(line)
    states = [[[1,2,3],[8,0,4],[7,6,5]], # Goal
              [[8,1,3],[0,7,2],[6,5,4]], # Médio
              [[7,8,6],[2,3,5],[1,4,0]], # Difícil
              [[7,8,6],[2,3,5],[0,1,4]], # Difícil
              [[8,3,6],[7,5,4],[2,1,0]], # Difícil
              [[3,4,8],[1,2,5],[7,0,6]], # Impossível
              [[5,4,0],[6,1,8],[7,3,2]]] # Impossível

    print("Este programa recebe uma configuração inicial\n e devolve o passo a passo até o estado final")
    print("Deseja iniciar com um estado já configurado ou embaralhar um novo?\n Digite 1 caso queira embaralhar um novo, caso contrário aperte qualquer tecla: ")
    io = int(input())
    if io == 1:
        init_state = np.arange(9).reshape((3, 3))
        np.random.shuffle(init_state)
        print("Estado inicial gerado: \n")
        matprint(init_state)
    else:
        print("\nEstados existentes:\n")
        [matprint(np.array(arr)) for arr in states[1:]]
        io = int(input("Digite qual estado escolhido (de 1 a 6, o 0 é o próprio objetivo): "))
        init_state = np.array( states[io] )
    final_state = np.array( [[1,2,3],
                             [8,0,4],
                             [7,6,5]] )
    state = Puzzle8(init_state,'',final_state)
    if state.isSolvable():
        print('Busca A*')
        algorithm = AEstrela()
        ts = time.time()
        result = algorithm.search(state)
        tf = time.time()
        if result != None:
            print('Achou!')
            #print(result.show_path().replace(';',"").split())
            path(result.show_path().replace(';',"").split(),init_state)
            #[matprint(np.array(arr)) for arr in path(result.show_path().replace(';',"").split(),init_state)]
            print(f"Em {tf-ts}")
        else:
            print('Nao achou solucao')
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()