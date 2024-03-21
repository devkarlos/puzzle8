# https://www.cs.princeton.edu/courses/archive/spring18/cos226/assignments/8puzzle/index.html

class Board:
    def __init__(self, tiles): # create a board from an n-by-n array of tiles
        self.tiles = tiles
        self.size = 0
        self.goal = [
            [1,2,3],
            [4,5,6],
            [7,8,0] # 0 represents the empty space
        ]

    def size(self) -> int:
        return self.size

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

    # The Manhattan distance between a board and the goal board is the sum of the Manhattan distances (sum of the vertical and horizontal distance) from the tiles to their goal positions. 
    def manhattan(self):
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

tiles = [
    [8,1,3],
    [4,0,2],
    [7,6,5]
]

board = Board(tiles)

print(board.hamming())
print(board.manhattan())
