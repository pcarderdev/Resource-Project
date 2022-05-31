class Player():
    def __init__(self):
        self.score = 0
        self.coordinates = [5, 5]

    # Need to figure out how to allow the Player class to read the board so the board size isn't hardcoded into the checks
    def moveUp(self):
        if self.coordinates[0] != 0:
            self.coordinates[0] -= 1
    
    def moveDown(self):
        if self.coordinates[0] != 9:
            self.coordinates[0] += 1
    
    def moveLeft(self):
        if self.coordinates[1] != 0:
            self.coordinates[1] -= 1
    
    def moveRight(self):
        if self.coordinates[1] != 9:
            self.coordinates[1] += 1
    
    def getScore(self):
        return self.score
    
    def incScore(self, val):
        self.score += val

    def get_coordinates(self):
        return self.coordinates