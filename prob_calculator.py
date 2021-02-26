import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            pos = 0
            while pos < value:
                self.contents.append(key)
                pos += 1
            #self.contents.append({key, value})
            #print("{0} = {1}".format(key, value))
        #self.contents
        #print ("Return Start: ")
        #print(', '.join(self.contents))
    def draw(self, num):
        toReturn = []

        pos = 0
        #saveList = self.contents
        while len(self.contents) != 0:
            original = []
            if pos == len(self.contents) or pos  == num:
                #print("break 1")
                break;
            n = random.randrange(0, len(self.contents))
            toReturn.append(self.contents[n])
            #print("rand: " + str(n))
            p2 = 0
            #print ("Broken Draw Test: ")
            #print(', '.join(self.contents))
            for i in self.contents:
                if p2 != n:
                    original.append(i)
                p2 += 1
            self.contents = original
            #print ("Return Original-Test ("+str(pos)+"): ")
            #print(', '.join(original))
            pos += 1

        return toReturn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #print("f")
    pos = 0
    m = 0
    #hatCore = hat
    checkContents = {}
    countContents = {}
    for key, value in expected_balls.items():
        posV = 0
        while posV < value:
            checkContents[key] = value
            countContents[key] = 0

            posV += 1

    while pos < num_experiments:
        #checkContents = {}
        for key, value in countContents.items():
            countContents[key] = 0

        hatcopy = Hat()
        hatcopy.contents = hat.contents
        drawn = hatcopy.draw(num_balls_drawn)

        for key, value in checkContents.items():
            for j in drawn:
                if j == key:
                    countContents[key] += 1

        allowed = True
        for k, l in checkContents.items():
                #print (k,' : ',l)
                if countContents[k] < checkContents[k]:
                    allowed = False
        if allowed:
            m += 1

        pos += 1
    return m / num_experiments
