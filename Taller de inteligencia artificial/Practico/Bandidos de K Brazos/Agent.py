from abc import ABCMeta
from abc import abstractmethod
import numpy as np

class Agent(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name):
        self.name = name        
       
    def play(self, n_steps, environment):        
        self.environment = environment
        self.clear_log()
        self.reset_internal_state()

        game_state = self.environment.reset()
        for _ in range(n_steps):
            environment.render()
            action = self.select_action(game_state)
            observation, reward, done, info = environment.step(action)
            self.update_internal_state(observation, action, reward)
            self.log(action, reward)    
          
        info = self.get_extra_info()
        log = self.get_log()
        return log, info 
    
    def clear_log(self):
        self.rewards = []
        self.selected_actions = []
        self.actions_rewards = dict((action, []) for action in range(self.environment.action_space.n))
    
    def log(self, action, reward):        
        self.rewards.append(reward)
        self.selected_actions.append(action)
        self.actions_rewards[action].append(reward)
    
    def get_log(self):
        best_action = np.argmax(self.environment.r_dist, axis = 0)[0]
        selected_best_action = 1* np.equal(best_action, np.array(self.selected_actions))  
        return  {"rewards": np.array(self.rewards), "selected_best_action": selected_best_action, "actions_rewards": self.actions_rewards, "best_action": best_action}
    
    @abstractmethod
    def reset_internal_state(self):
        pass

    @abstractmethod
    def select_action(self, game_state):
        pass
    
    @abstractmethod
    def update_internal_state(self, observation, action, reward):
        pass

    @abstractmethod
    def get_extra_info(self):
        pass
