from abc import abstractmethod

class Environment(object):

    @abstractmethod
    def __init__(self, agent, rooms):
        self.agent = agent
        self.rooms = rooms
        self.currentRoom = self.rooms[0]

    @abstractmethod
    def executeStep(self, n=1):
        for i in range(n):
            self.agent.sense(self)
            action = self.agent.act()
            if action == 'clean':
                self.currentRoom.status = 'clean'
            elif action == 'right':
                if self.currentRoom.location == 'A':
                    self.currentRoom = self.rooms[1]
                elif self.currentRoom.location == 'B':
                    self.currentRoom = self.rooms[2]
            elif action == 'left':
                if self.currentRoom.location == 'B':
                    self.currentRoom = self.rooms[0]
                elif self.currentRoom.location == 'C':
                    self.currentRoom = self.rooms[1]

    @abstractmethod
    def executeAll(self):
        while any(room.status == 'dirty' for room in self.rooms):
            self.executeStep()
    
    def delay(self, n=100):
        self.delay = n


class Room:
    
    def __init__(self, location, status="dirty"):
        self.location = location 
        self.status = status


class Agent(object):

    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def sense(self, environment):
        pass
    
    @abstractmethod 
    def act(self):
        pass


class VaccumAgent(Agent):

    def __init__(self):
        pass
    
    def sense(self, env):
        self.environment = env
    
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean' 
        
        if self.environment.currentRoom.location == 'A':
            return 'right'
        
        if self.environment.currentRoom.location == 'B':
            if self.environment.rooms[1].status == 'dirty':
                return 'left'
            else:
                return 'right'
        
        if self.environment.currentRoom.location == 'C':
            return 'left'
    


if __name__ == '__main__': 
    roomA = Room('A', 'dirty')
    roomB = Room('B', 'dirty')
    roomC = Room('C', 'dirty')
    rooms = [roomA, roomB, roomC]
    vcagent = VaccumAgent() 
    env = Environment(vcagent, rooms)
    env.executeAll()
    print("Environment cleaned successfully!")
