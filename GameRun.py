from GameStatus import GameStatus
from BelieveNotBelieve import BelieveNotBelieve


game = BelieveNotBelieve()
word = game.generate_questions()

while game.game_status == GameStatus.IN_PROGRESS:
    game.answer()

if game.game_status == GameStatus.LOST:
    print("You're hanged!")
else:
    print('Congratulations! You won!')