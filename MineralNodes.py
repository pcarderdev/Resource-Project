from random import randrange
import Node
import random

## Turn into class ##
def generateCoordinates(file):
    f = open(file, "w")

    for x in range(0,10):
        x = random.randrange(0, 10)
        y = random.randrange(0, 10)
        f.write("{},{}\n".format(x, y))

    f.close()

def generateNodes():
    file = "minNode_coordinates.txt"

    #generateCoordinates(file)

    f = open(file, "r")
    mineral_nodes = []

    for e in f:
        x,y = map(int, e.split(','))
        node_type_int = random.randrange(1, 100)
        if node_type_int <= 70:
            mineral_nodes.append(Node.CopperNode(x, y))
        elif node_type_int <= 95:
            mineral_nodes.append(Node.SilverNode(x, y))
        else:
            mineral_nodes.append(Node.GoldNode(x, y))
    return mineral_nodes