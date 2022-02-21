import prob_calculator
from unittest import main


hat = prob_calculator.hat(blue = 4, red = 2, green = 6)
probability = prob_calculator.experiment(
    hat = hat,
    expected_ball={'blue':2,"red":1},
    number_ball_drawn = 4,
    number_experiments = 3000
)
print("Probability : {probability}")

main(module = 'Test_Module', exit = False)