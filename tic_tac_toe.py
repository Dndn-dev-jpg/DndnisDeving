# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in [0 , 1 , 2] or y not in [0 , 1 , 2] :
        return False
    elif game_board[y][x] != "" :
        return False
    else :
        game_board[y][x] = piece
        return True
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)