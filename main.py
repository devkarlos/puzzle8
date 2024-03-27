from Board import Board
from Solver import Solver

tiles = [
    [0,1,3],
    [4,2,5],
    [7,8,6]
]

tiles_no = [
    [1,2,3],
    [4,5,6],
    [8,7,0]
]

board = Board(tiles)

print("hamming:", board.hamming())
print("manhattan:", board.manhattan())
i = 0
for neighbour in board.get_neighbours():
    i+=1
    print("neighbour:", i)
    for row in neighbour:
        print(row)
    print("----")
    
print("\n----")
print("neighbours:", i)
print("is solvable: ", board.is_solvable())
board.print_tile()
