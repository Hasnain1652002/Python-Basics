from typing import List, Set


class NQueenSolution:
    def __init__(self, N: int) -> None:
        self.N: int = N  # Number of chess queens in board
        self.board: List[List[str]] = [
            ["x"] * N for _ in range(N)
        ]  # simulating a chess board to store result

    def solve(self) -> None:
        queen_columns: Set[
            int
        ] = set()  # tracks those columns which can be attacked by other queen
        queen_pos_diagonals: Set[
            int
        ] = (
            set()
        )  # tracks those positive diagonals which can be attacked by other queen
        queen_neg_diagonals: Set[
            int
        ] = (
            set()
        )  # tracks those negative diagonals which can be attacked by other queen

        def is_safe(row: int, col: int) -> bool:
            return not (
                col in queen_columns
                or row + col in queen_pos_diagonals
                or row - col in queen_neg_diagonals
            )

        def backtrack(row: int) -> bool:
            if row == self.N:
                return True

            for col in range(self.N):
                if is_safe(row, col):
                    queen_columns.add(col)
                    queen_pos_diagonals.add(row + col)
                    queen_neg_diagonals.add(row - col)
                    self.board[row][col] = "Q"

                    if backtrack(row + 1):
                        return True

                    queen_columns.remove(col)
                    queen_pos_diagonals.remove(row + col)
                    queen_neg_diagonals.remove(row - col)
                    self.board[row][col] = "x"

            return False

        backtrack(0)

    def __str__(self):
        return "\n".join([" ".join(row) for row in self.board])


if __name__ == "__main__":
    _8queen_problem = NQueenSolution(4)
    _8queen_problem.solve()
    print(_8queen_problem)
