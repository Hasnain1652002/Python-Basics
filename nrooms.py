from abc import abstractmethod

class Environment(object):

    @abstractmethod
    def __init__(self, agent, rooms):
        self.agent = agent
        self.rooms = rooms
        self.currentRoom = self.rooms[0]

    @abstractmethod
    def executeStep(self, n=1):
        if n <= 0:
            return
        
        self.agent.sense(self)
        action = self.agent.act()
        
        if action == 'clean':
            self.currentRoom.status = 'clean'
        elif action == 'right':
            self.currentRoom = self.rooms[(self.rooms.index(self.currentRoom)+1) % len(self.rooms)]
            self.executeStep(n-1)
        elif action == 'left':
            self.currentRoom = self.rooms[(self.rooms.index(self.currentRoom)-1) % len(self.rooms)]
            self.executeStep(n-1)
    
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
        
        if self.environment.currentRoom.location == 'C':
            return 'left'
        
        # Default action is to go right
        return 'right'
    


if __name__ == '__main__': 
    roomA = Room('A', 'dirty')
    roomB = Room('B', 'dirty')
    roomC = Room('C', 'dirty')
    roomD = Room('D', 'dirty')
    roomE = Room('E', 'dirty')
    roomF = Room('F', 'dirty')
    roomG = Room('G', 'dirty')
    roomH = Room('H', 'dirty')
    rooms = [roomA, roomB, roomC, roomD, roomE, roomF, roomG, roomH]
    vcagent = VaccumAgent() 
    env = Environment(vcagent, rooms)
    env.executeStep(100)
    print("Environment cleaned successfully!")
