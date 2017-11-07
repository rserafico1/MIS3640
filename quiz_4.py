ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return '{} won {}, with winning {} states.'.format(self.name, self.winning_states, self.votes)

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        if self.winning_states > state.winning_states:
            return True
        elif self.winning_states == state.winning_states:
            if self.votes > state.votes:
                return True
        return False

    def __add__(self, state):
        candidate = Candidate()
        candidate.name = self.name + ' ' + state.name
        candidate.winning_states = self.winning_states + state.winning_states 
        candidate.votes = (self.votes + state.votes)/2 
        return candidate


def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], votes=55)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()
