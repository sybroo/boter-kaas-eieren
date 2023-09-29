import random
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, validate, plot_validation
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
 
random.seed(1)
 
my_agent = MyAgent()
random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=50,
    trainings=100,
    validations=1000)

validation_result = validate(agent_x=my_agent, agent_o=random_agent, iterations=50)
 
plot_validation(validation_result)