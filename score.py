from abc import abstractmethod
import random
import time

class Environment(object):

    def __init__(self, agent, n):
        self.agent = agent
        self.rooms = [Room(f"Room {i+1}") for i in range(n)]
        self.currentRoom = self.rooms[0]
        self.score = 0
    
    def executeStep(self, n=1):
        for i in range(n):
            self.agent.sense(self)
            action = self.agent.act()
            
            if action == 'clean':
                if self.currentRoom.status == 'dirty':
                    print(f"Score:{self.score}")
                    print("Adding 25 to the Score :)")
                    self.score += 25
                    print(f"Score:{self.score}")
                    self.currentRoom.status = 'clean'
                else:
                    pass
            elif action == 'right':
                print(f"Score:{self.score}")
                print("Substracting 1 to the Score :(")
                self.score -= 1
                print(f"Score:{self.score}")
                idx = (self.rooms.index(self.currentRoom) + 1) % len(self.rooms)
                self.currentRoom = self.rooms[idx]
            elif action == 'left':
                print(f"Score:{self.score}")
                print("Substracting 1 to the Score :(")
                self.score -= 1
                print(f"Score:{self.score}")
                idx = (self.rooms.index(self.currentRoom) - 1) % len(self.rooms)
                self.currentRoom = self.rooms[idx]
            
            if all(room.status == 'clean' for room in self.rooms):
                print(f"All rooms are clean! Final score: {self.score}")
                return
            
            time.sleep(1)
        
        print(f"Score after {n} steps: {self.score}")
        

class Room:
    
    def __init__(self, name, status="dirty"):
        self.name = name 
        self.status = status


class Agent(object):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def sense(self,environment):
        pass
    
    @abstractmethod 
    def act(self):
        pass


class VaccumAgent(Agent):

    def __init__(self):
        pass
    
    def sense(self,env):
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            print(f"Room is currently Dirty :(")
            print(f"Cleaning Room ...")
            print(f"Room is clean now :)")
            return 'clean' 
        
        if random.random() < 0.5:
            print("Moving to the next Room.")
            return 'right'
        else:
            print("Moving to the next Room.")
            return 'left'


if __name__ == '__main__':
    n = 8 
    vcagent = VaccumAgent() 
    env = Environment(vcagent, n)
    env.executeStep(50)
