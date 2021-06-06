import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.contents = []

        for key, val in colors.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        result = []
        if num_balls_drawn >= len(self.contents):
            result = self.contents
            self.contents = []
            return result
        
        for i in range(num_balls_drawn):
            index_to_pop = random.randint(0, len(self.contents) - 1)
            result.append(self.contents.pop(index_to_pop))

        return result

def __is_expected(result, expected):
    is_expected = True
    for name, expected_value in expected.items():
        if result.count(name) < expected_value:
            return False

    return is_expected

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0

    for i in range(N):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        if __is_expected(drawn, expected_balls):
            M += 1

    if M: 
        return M / N
    else:
        return M