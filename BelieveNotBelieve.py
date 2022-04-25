from typing import Iterable

from GameStatus import GameStatus


class InvalidOperationException(Exception):
    pass


class BelieveNotBelieve:

    def __init__(self, allowed_misses: int = 3):
        if allowed_misses < 1 or allowed_misses > 4:
            raise ValueError("Number of allowed misses should be between 1 and 4")

        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__right_questions = 0
        self.__open_questions = 0
        self.__game_status = GameStatus.NOT_STARTED
        self.__questions = []

    def generate_questions(self) -> Iterable[Iterable[str]]:
        filename = 'Questions.csv'

        questions = []
        with open(filename, encoding='utf8') as file:
            for line in file:
                questions.append(line.strip('\n').split(';'))
        self.__questions = questions
        self.__game_status = GameStatus.IN_PROGRESS

        return self.__questions

    def answer(self):
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationException(f'Exceeded the max misses number. Allowed {self.allowed_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationException(f'Inappropriate status of game: {self.game_status}')

        for x in self.questions:
            if input(x[0] + ' Yes/No\n') == x[1]:
                self.__right_questions += 1
                print("You're right!")
                print(x[2])
            else:
                self.__tries_counter += 1
                print("You're wrong!")
                print(x[2])
            self.__open_questions += 1

            if self.__is_winning():
                self.__game_status = GameStatus.WON
            elif self.tries_counter == self.allowed_misses or self.open_questions == len(self.questions):
                self.__game_status = GameStatus.LOST

    def __is_winning(self):
        return self.right_questions >= self.allowed_misses

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def questions(self) -> list:
        return self.__questions

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def right_questions(self) -> int:
        return self.__right_questions

    @property
    def open_questions(self) -> int:
        return self.__open_questions
