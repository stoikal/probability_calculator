import prob_calculator

hat = prob_calculator.Hat(blue=1,red=1)
probability = prob_calculator.experiment(
        hat=hat, 
        expected_balls={ 'blue': 1 }, 
        num_balls_drawn=1, 
        num_experiments=100
    )

print(probability)