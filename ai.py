class WowWowAI(object):
    def __init__(self):
        # ボードの評価マップ (スコアの高い場所を優先)
        self.score_map = [
            [100, -20, 10, 10, -20, 100],
            [-20, -50, -2, -2, -50, -20],
            [10, -2,  0,  0,  -2,  10],
            [10, -2,  0,  0,  -2,  10],
            [-20, -50, -2, -2, -50, -20],
            [100, -20, 10, 10, -20, 100],
        ]
   
    def face(self):
        return "😻"

    def evaluate_move(self, board, stone, x, y):
        """
        その場所に石を置いたときのスコアを評価する。
        """
        return self.score_map[y][x]

    def can_place_x_y(board, stone, x, y):

        if board[y][x] != 0:
            return False  # 既に石がある場合は置けない

        opponent = 3 - stone  # 相手の石 (1なら2、2なら1)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            found_opponent = False

            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
                nx += dx
                ny += dy
                found_opponent = True

            if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
                return True  # 石を置ける条件を満たす

        return False

    def get_possible_moves(self, board, stone):
        """
        現在の石で置けるすべての座標を取得する。
        """
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    moves.append((x, y))
        return moves

    def place(self, board, stone):
        """
        最善の場所を計算して石を置く。
        """
        possible_moves = self.get_possible_moves(board, stone)
        if not possible_moves:
            raise ValueError("No possible moves")
       
        # 各手を評価してスコアの高いものを選ぶ
        best_move = None
        best_score = float('-inf')
        for x, y in possible_moves:
            score = self.evaluate_move(board, stone, x, y)
            if score > best_score:
                best_score = score
                best_move = (x, y)
       
        return best_move

