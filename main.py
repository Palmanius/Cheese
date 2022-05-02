import chess
import chess.svg

from IPython.display import SVG

board = chess.Board()
board.turn == chess.WHITE
SVG(chess.svg.board(board=board,size=400))




""" 
def player(board):
    ### "Thinking" happens here
    return move_code """