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
 
my_agent = MyAgent(alpha=0.1, epsilon=0.05) 

#hier wordt bepaald hoe snel de agent nieuwe kennis adopteert hoe hoger dit getal hoe sneller de agent geneigd zal zijn om oude kennis te vervangen door nieuwe kennis

random_agent = RandomAgent()
 
train_and_plot(
    agent=my_agent,
    validation_agent=random_agent,
    iterations=100,
    trainings=100,
    validations=1000)
#hier wordt my_agent getraind tegen de random agent met 100 herhalingen en 100 trainingen en daarbij worden de gegevens 1000 keer gechecked. 

validation_agent = RandomAgent()
 
validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)
 
plot_validation(validation_result)

#hier wordt de getrainde my_agent tegen een nieuwe random agent gezet en spelen ze 100 potjes daarvan wordt de grafiek gegeven hoeveel er gewonnen worden