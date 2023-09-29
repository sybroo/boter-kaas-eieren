import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
 
random.seed(1) #seed bepaald het begin getal van de gegevens die je terug krijgt
 
my_agent = MyAgent()
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

#door deze code ontstaat een grafiek die laat zien hoevaak je hem traint en hoe vaak je hem valideert, iterations is hoe vaak die herhaald word