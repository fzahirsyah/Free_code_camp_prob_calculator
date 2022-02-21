import copy
import random
import sys

class hat:
    def __init__(self, **kwargs):
        self.contents = []
        print(kwargs)
        for k , v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        print(self.contents)
    
    def draw(self, number):
        all_removed = []
        if number > len(self.contents):
            return self.contents
        for i in range(number):
            remove = self.contents.pop(random.randrange(len(self.contents)))
            all_removed.append(remove)
        return all_removed
        

def experiment(hat, expected_ball, number_ball_drawn, number_experiments):
    count = 0
    for _ in range(number_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(number_ball_drawn)
        balls_req = sum([1 for k, v in expected_ball.items() if balls_drawn.count(k) >= v])
        count += 1 if balls_req == len(expected_ball) else 0

    return count / number_experiments
