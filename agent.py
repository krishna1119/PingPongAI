import torch
import random as rd
from oopspong import PongGame
import numpy as np
from collections import deque
from model import Linear_QNet, QTrainer
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001


class Agent:
    def __init__(self) -> None:
        self.epsilon = 0
        self.gammma=0.9
        self.memory = deque(maxlen = MAX_MEMORY)
        self.model = Linear_QNet(4,10,3)
        self.trainer = QTrainer(self.model , lr=LR, gamma=self.gammma)
        #TODO: model, trainer
        self.model = Linear_QNet(4,256,3)
        self.trainer = QTrainer(self.model, lr =LR,gamma =self.gammma)


    def get_state(self, game):              #to get the current state of the game
        state= [
            game.ball.xcor(),
            game.ball.ycor(), 
            game.paddle_b.ycor(),
            game.ball.dy()
            ]
        return np.array(state)

    def remember(self, state, action, reward, next_state):        
            #to remember the previous state
        self.memory.append((state, action, reward, next_state))#popleft if max memory is reached
        
        
    #if done:
        # def train_long_memory(self):   
        # if len(self.memory) >BATCH_SIZE:
        #       mini_sample = random.sample(Self.memory, BATCH_SIZE)
        #  else:
        #       mini_sample = self.memory
        # states,actions,rewards,next_states = zip(*mini_sample)
        # self.trainer.train_step(states, actions,rewards,next_states)                             #to store all previous actions for a certain large value


    def train_short_memory(self, state, action, reward, next_state):  #to remebr shorter batch size of actions
        self.trainer.train_step(state, action,reward,next_state)


    def get_action(self, state):                                        #to get the action of the next state
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0,200)<self.epsilon:
            move = random.randint(0,2)
            final_move[move] = 1
        else:
            state0= torch.tensor(state, dtype = torch.flaot)
            prediction = self.model(state0)
            move= torch.argmax(prediction).item()
            final_move[move] = 1
        
        return final_move

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = PongGame()
    while True:
        #get the old state
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = agent.get_state(game)

        agent.train_short_memory(state_old, final_move, reward, state_new)
        agent.remember (state_old, final_move, reward, state_new)
       
        #agent.train_long_memory()

        if score > record:
            record= score
            #agent.model.save()

        print('record' , record)



    pass

if __name__ == '__main__':
    train()






