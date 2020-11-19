class Game():

    def __init__(self):
        self.possible_hands = {
            'rock': 1,
            'paper': 2,
            'scissors': 3    
        }

    def check_valid_hand(self, hand):
        if self.possible_hands.get(hand, None):
            return True
        else:
            return False

    def get_winner(self, player_1, player_2):

        winner = None
        if player_1.choice == player_2.choice:
            return winner
        elif not self.check_valid_hand(player_1.choice) or not self.check_valid_hand(player_2.choice):
            return winner
        elif player_1.choice == 'rock' and player_2.choice == 'scissors':
                winner = player_1
        elif player_1.choice == 'paper' and player_2.choice == 'rock':
                winner = player_1
        elif player_1.choice == 'scissors' and player_2.choice == 'paper':
                winner = player_1
        else:
            winner = player_2

        return winner