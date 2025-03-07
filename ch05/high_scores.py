class GameEntry:
    """
    Represents one entry of a list of high scores.
    """

    def __init__(self, name, score):
        # Create an entry with given name and score.
        self._name = name
        self._score = score

    def get_name(self):
        # Return the name of the person for this entry.
        return self._name

    def get_score(self):
        # Return the score of this entry.
        return self._score

    def __str__(self):
        # Return string representations of the entry.
        return "({0}, {1})".format(self._name, self._score)


class Scoreboard:
    """
    Fixed-length sequence of high scores in nondecresing order.
    """
    
    def __init__(self, capacity = 10):
        # Initialize scoreboard with given maximum capacity.
        # All entries are initially None.
        self._board = [None] * capacity     # reserve space for future scores
        self._n = 0     # number of actual entries

    def __getitem__(self, i):
        # Return entry at index i
        return self._board[i]

    def __str__(self):
        # Return a string representation of the high score list.
        return '\n'.join(str(self._board[i]) for i in range(self._n))

    def add(self, entry):
        # Consider adding to high scores.
        score = entry.get_score()

        # Does this new entry qualify as a high score?
        # Yes if board is not full or Score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):      # no score drops from list
                self._n += 1        # so overall number increases

            # shift lower scores rightward to make room for new entry
            i = self._n - 1
            while i > 0 and self._board[i - 1].get_score < score:
                self._board[i] = self._board[i - 1]     # shift entry from j - 1 to j
                i -= 1      # and decrement j
            self.board[i] = entry       # when done, add new entry



if __name__ == '__main__':
    board = Scoreboard(5)

    for e in (
        ('Rob', 750), ('Mike', 1105), ('Rose', 590), ('Jill', 740),
        ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400),
    ):
        gameEntry = GameEntry(e[0], e[1])
        
        board.add(gameEntry)
        print("After considering {0}, scoreboard is: ".format(gameEntry))
        print(board)
        print()
