class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.size = 0
        self.goal = [
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
            else:
                continue
        return None

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

    def isGoal(self) -> bool:
        return self.tiles == self.goal
    
    def equals(self, board) -> bool:
        return self.tiles == board

    # 0 in the corner -> 2 neigbors
    # 0 in the center -> 4 neigbors
    # 0 in the middle of row/column -> 3 neigbors
    def neighbours(self) -> list:
        neighbours = 0

        zero_pos = self.get_item_pos(self.tiles, 0)
        zero_x = zero_pos[0]
        zero_y = zero_pos[1]

        if zero_x == 1 and zero_y in [0,2]: # above and bellow the center
            neighbours = 3
        elif zero_x in [0,2] and zero_y == 1: # next to the center
            neighbours = 3
        elif zero_x in [0, 2] and zero_y in [0, 2]: # corners
            neighbours = 2
        else: # center
            neighbours = 4

        return neighbours
    
    def isSolvable(self):
        pass

tiles = [
    [8,1,3],
    [4,0,2],
    [7,6,5]
]

board = Board(tiles)

print(board.hamming())
print(board.manhattan())
print(board.neighbours())
