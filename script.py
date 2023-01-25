import requests
while True:
 fen = input("Enter FEN: ")
 url = "https://api.chess.com/pub/engine/stockfish"
 response = requests.get(url, params={"fen": fen})
 best_move = response.json()["bestmove"]
 print(best_move)
