class Board:
    def __init__(self, tiles, board_size: int) -> None:
        self.tiles: list[list[int]] = tiles
        self.board_size = board_size
        self.goal: list[list[int]] = self.generate_goal()
        

    def generate_goal(self) -> list[list[int]]:
        goal = [[0] * self.board_size for _ in range(self.board_size)]
        num = 1
        for i in range(self.board_size):
            for j in range(self.board_size):
                goal[i][j] = num
                num = (num + 1) % (self.board_size * self.board_size)
        goal[-1][-1] = 0  # Empty space represented by 0
        return goal


    # The Hamming distance betweeen a board and the goal board is the number of tiles in the wrong position
    def hamming(self) -> int:
        counter = 0
        for i in range(0, self.board_size):
            for ii in range(0, self.board_size):
                if self.tiles[i][ii] != self.goal[i][ii] and self.tiles[i][ii] != 0:
                    counter+=1
        return counter


    def get_tile_pos(self, lst: list, to_find: int) -> list[int]:
        for i in range(0, self.board_size):
            if to_find in lst[i]:
                return [i, lst[i].index(to_find)]
        return []


    # The Manhattan distance between a board and the goal board is the sum of the Manhattan distances
    # (sum of the vertical and horizontal distance) from the tiles to their goal positions. 
    def manhattan(self) -> int:
        distance = 0
        for i in range(0, self.board_size):
            for ii in range(0, self.board_size):
                if self.tiles[i][ii] != self.goal[i][ii] and self.goal[i][ii] != 0:
                    tile_pos = self.get_tile_pos(self.tiles, self.goal[i][ii])
                    goal_pos = self.get_tile_pos(self.goal, self.goal[i][ii])
                    for p in range(0,2):
                        distance += abs(goal_pos[p] - tile_pos[p])
        return distance


    def is_goal(self) -> bool:
        return self.tiles == self.goal


    def equals(self, board) -> bool:
        return self.tiles == board


    def get_neighbours(self) -> list[list[int]]:
        neighbours = []
        zero_pos = self.get_tile_pos(self.tiles, 0)
        zero_x, zero_y = zero_pos

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x, y in moves:
            new_zero_x, new_zero_y = zero_x + x, zero_y + y
            
            if 0 <= new_zero_x < self.board_size and 0 <= new_zero_y < self.board_size:
                neighbour = [row[:] for row in self.tiles]

                neighbour[zero_x][zero_y], neighbour[new_zero_x][new_zero_y] = neighbour[new_zero_x][new_zero_y], neighbour[zero_x][zero_y]
                neighbours.append(neighbour)

        return neighbours


    def is_solvable(self) -> bool:
        inversions = 0
        board_flat = [tile for row in self.tiles for tile in row if tile != 0]
        
        for i in range(len(board_flat)):
            for j in range(i + 1, len(board_flat)):
                if board_flat[i] > board_flat[j]:
                    inversions += 1
        return inversions % 2 == 0
