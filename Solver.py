import heapq
from Board import Board


class Solver:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.solution_path: list[list[int]] = []


    def solve(self) -> int:
        priority_queue = [(self.board.manhattan(), 0, self.board, None)]
        visited = set()

        while priority_queue:
            current_cost, moves, current_board, parent = heapq.heappop(priority_queue)

            if current_board.is_goal():
                self.reconstruct_path(current_board, parent)
                return moves

            if str(current_board.tiles) in visited:
                continue

            visited.add(str(current_board.tiles))

            for neighbour in current_board.get_neighbours():
                if str(neighbour) not in visited:
                    neighbour_board = Board(neighbour, current_board.board_size)
                    heapq.heappush(priority_queue, (moves + neighbour_board.manhattan() + 1, moves + 1, neighbour_board, (current_board, parent))) # type: ignore - due to static type checker
    
        return -1


    def reconstruct_path(self, board: Board, parent) -> None:
        if parent:
            self.reconstruct_path(parent[0], parent[1])
        self.solution_path.append(board.tiles) # type: ignore


    def move_count(self) -> int:
        return len(self.get_solution()) - 1 if self.get_solution() else -1


    def get_solution(self) -> list[list[int]]:
        if not self.solution_path:
            self.solve()
        return self.solution_path
