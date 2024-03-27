class Board:
    def __init__(self, tiles) -> None:
        self.tiles: list = tiles
        self.size: int = 0
        self.goal: list = [
            [1,2,3],
            [4,5,6],
            [7,8,0] # 0 represents the empty space
        ]


    # The Hamming distance betweeen a board and the goal board is the number of tiles in the wrong position
    def hamming(self) -> int:
        counter = 0
        for i in range(0, 3):
            for ii in range(0, 3):
                if self.tiles[i][ii] != self.goal[i][ii] and self.tiles[i][ii] != 0:
                    counter+=1
        return counter


    def get_item_pos(self, lst: list, to_find: int) -> list:
        for i in range(0,3):
            if to_find in lst[i]:
                return [i, lst[i].index(to_find)]
        return []


    # The Manhattan distance between a board and the goal board is the sum of the Manhattan distances
    # (sum of the vertical and horizontal distance) from the tiles to their goal positions. 
    def manhattan(self) -> int:
        distance = 0
        for i in range(0,3):
            for ii in range(0,3):
                if self.tiles[i][ii] != self.goal[i][ii] and self.goal[i][ii] != 0:
                    tile_pos = self.get_item_pos(self.tiles, self.goal[i][ii])
                    goal_pos = self.get_item_pos(self.goal, self.goal[i][ii])
                    for p in range(0,2):
                        distance += abs(goal_pos[p] - tile_pos[p])
        return distance


    def is_goal(self) -> bool:
        return self.tiles == self.goal
    
    
    def equals(self, board) -> bool:
        return self.tiles == board
    
    
    def replace_item_in_tile(self, tile: list, item_pos: list, replace_with: int) -> list:
        temp_tile: list = [row[:] for row in tile]
        temp_tile[item_pos[0]][item_pos[1]] = replace_with
        return temp_tile
    
    
    def switch_items_in_tile(self, tile: list, item_pos1: list, item_pos2: list) -> list:
        temp_tile: list = [row[:] for row in tile]
        temp_value = temp_tile[item_pos1[0]][item_pos1[1]]
        
        temp_tile[item_pos1[0]][item_pos1[1]] = temp_tile[item_pos2[0]][item_pos2[1]]
        temp_tile[item_pos2[0]][item_pos2[1]] = temp_value
        
        return temp_tile


    # 0 in the corner -> 2 neigbors
    # 0 in the center -> 4 neigbors
    # 0 in the middle of row/column -> 3 neigbors
    def get_neighbours(self) -> list:
        temp_tile: list = [row[:] for row in self.tiles]
        neighbors: list = []

        zero_pos: list = self.get_item_pos(self.tiles, 0)
        zero_x: int = zero_pos[0]
        zero_y: int = zero_pos[1]
        
        # TODO: Recode this algorithm
        if zero_x == 1 and zero_y in [0,2]: # zero is in the left/right center
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x+1, zero_y])) # left/right center
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x-1, zero_y])) # left/right center
            if zero_y == 0:
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y-1])) # right top
            else: # zero_y == 2
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y+1])) # left bottom

        elif zero_x in [0,2] and zero_y == 1: # zero is in the top/bottom center
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y+1])) # left/right center
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y-1])) # left/right center
            if zero_x == 0:
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x+1, zero_y])) # right top
            else: # zero_x == 2
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x-1, zero_y])) # left bottom

        elif zero_x in [0, 2] and zero_y in [0, 2]: # corners
            if zero_x == 0:
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y+1]))
            else: # zero_x == 2
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y-1]))
            if zero_y == 0:
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x+1, zero_y]))
            else: # zero_y == 2
                neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x-1, zero_y]))

        else: # center
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x+1, zero_y]))
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x-1, zero_y]))
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y+1]))
            neighbors.append(self.switch_items_in_tile(temp_tile, zero_pos, [zero_x, zero_y-1]))

        return neighbors
    
   
    def is_solvable(self) -> bool:
        inversions = 0
        board = [tile for row in self.tiles for tile in row]
        
        for i in range(len(board)):
            if i != 0 and board[i] != 0:
                if board[i] < board[i-1]:
                    inversions+=1
                    
        if inversions%2==0:
            return True
        
        return False
            
    def print_tile(self):
        for row in self.tiles:
            print(row)
