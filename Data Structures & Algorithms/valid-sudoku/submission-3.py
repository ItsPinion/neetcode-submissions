class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        col: dict[int, set[str]] = {}
        row: dict[int, set[str]] = {}
        grid: dict[tuple[int, int], set[str]] = {}

        for i in range(len(board)):
            for j in range(len(board[i])):
                digit: str = board[i][j]
                if digit != ".":
                    if not row.get(i):
                        row[i] = set()
                    if not col.get(j):
                        col[j] = set()
                    if not grid.get((i // 3, j // 3)):
                        grid[(i // 3, j // 3)] = set()

                    if digit in row[i]:
                        return False
                    if digit in col[j]:
                        return False
                    if digit in grid[(i // 3, j // 3)]:
                        return False

                    row[i].add(digit)
                    col[j].add(digit)
                    grid[(i // 3, j // 3)].add(digit)

        return True

