from Workout import *

test = Workout('english', 'test workout, 5x40/20s', 'Test Workout', 'minutes', 'percent')
test.add_interval_set(5, 40/60, 150, 20/60, 20)
test.export_mrp_file('C:/Users/rlybr/Desktop/Workouts')