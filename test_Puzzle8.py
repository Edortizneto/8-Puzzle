
from SearchAlgorithms import AEstrela
from Puzzle8 import Puzzle8
from datetime import date, datetime
import numpy as np

states = [[[1,2,3],[8,0,4],[7,6,5]], # Goal
          [[8,1,3],[0,7,2],[6,5,4]], # Médio
          [[7,8,6],[2,3,5],[1,4,0]], # Difícil
          [[7,8,6],[2,3,5],[0,1,4]], # Difícil
          [[8,3,6],[7,5,4],[2,1,0]], # Difícil
          [[3,4,8],[1,2,5],[7,0,6]], # Impossível
          [[5,4,0],[6,1,8],[7,3,2]]] # Impossível
          

def test_1():
    init_state = np.array( states[1] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert np.array_equal(result.state.board, final_state)#np.result.show_path() == 

def test_2():
    init_state = np.array( states[2] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert np.array_equal(result.state.board, final_state)#np.result.show_path() == 

def test_3():
    init_state = np.array( states[3] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert np.array_equal(result.state.board, final_state)#np.result.show_path() == 

def test_4():
    init_state = np.array( states[4] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert np.array_equal(result.state.board, final_state)#np.result.show_path() == 

def test_5():
    init_state = np.array( states[5] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    assert state.isSolvable() == False

def test_6():
    init_state = np.array( states[6] )
    final_state = np.array( states[0])
    state = Puzzle8(init_state,'',final_state)
    assert state.isSolvable() == False
