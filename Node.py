class Node():
    def __init__(self, x, y):
        self.coordinates = [x, y]
        self.value = 0
        self.respawn_timer = 300
        self.node_active = True

    def gatherNode(self):
        self.node_active = False
        
    def get_value(self):
        return self.value
    
    def set_value(self, newValue):
        self.value = newValue
    
    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, x, y):
        self.coordinates = [x, y]

class CopperNode(Node):
    def __init__(self, x, y):
        self.coordinates = [x, y]
        self.value = 10
        self.respawn_timer = 300

class SilverNode(Node):
    def __init__(self, x, y):
        self.coordinates = [x, y]
        self.value = 50
        self.respawn_timer = 1200

class GoldNode(Node):
    def __init__(self, x, y):
        self.coordinates = [x, y]
        self.value = 150
        self.respawn_timer = 3600