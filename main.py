from Board import Board
from Solver import Solver


class CLI:
    def __init__(self) -> None:
        self.user_choice = 0
        self.input_board: list[list[int]] = []
        self.input_board_size: int = 0

        while True:
            self.input_method()

            if self.user_choice == 1:
                self.board_from_input()
                break
            elif self.user_choice == 2:
                self.board_from_file_input()
                break
            else:
                print("Invalid input")


    def input_method(self) -> None:
        print("Choose input method:")
        print("1. Manual")
        print("2. Read from file")
        
        self.user_choice =  int(input("Enter your choice: "))


    def board_from_input(self) -> None:
        size = int(input("Enter the size of the board (e.g., 3 for 3x3): "))
        board = []

        print(f"Enter your {size}x{size} puzzle by rows, with '0' representing the empty space. Use space or commas between numbers.")
        for i in range(size):
            while True:
                row_input = input(f"Enter row {i+1}: ")
                row = [int(num) for num in row_input.replace(',', ' ').split() if num.isdigit()]
                
                if len(row) == size:
                    board.append(row)
                    break
                else:
                    print(f"Each row only has {size} numbers")

        self.input_board = board


    def board_from_file_input(self):
        file_path = input("Enter the file path (default is 'puzzle.txt'): ")
        if not file_path:
            file_path = "puzzle.txt"

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.input_board_size = int(lines[0])
                board = []
                for line in lines[1:]:
                    row = [int(num) for num in line.split()]
                    board.append(row)
            self.input_board = board

        except FileNotFoundError:
            print(f"No such file found: '{file_path}'")


cli = CLI()

if not cli.input_board:
    print("Board input failed")

board = Board(cli.input_board, cli.input_board_size)
solver = Solver(board)

print(f"hamming: {board.hamming()}")
print(f"manhattan: {board.manhattan()}")
print()
neighbours = 0

for neighbour in board.get_neighbours():
    neighbours += 1
    print(f"neighbour: {neighbours}")
    for row in neighbour:
        print(row)
    print("----\n")

print("\n----")
print(f"neighbours: {neighbours}")

if board.is_solvable():
    solution = solver.get_solution()
    step = 1
    for state in solution:
        print(f"Step {step}:")
        for row in state:
            print(row)
        step += 1
        print("----\n")
        
    print("solution:")
    for row in solution[-1]:
        print(row)

else:
    print("The board is not solvable.")
