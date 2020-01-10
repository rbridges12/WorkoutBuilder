from Workout import *

file_name = 'big_interval_mix'
description = '3x5 40/20s, 10min hard, 2x5min hard'

test = Workout(units = 'english', file_name = file_name, description = description, time_unit='minutes',
               ftp_unit='percent')

test.add_10min_easy()
test.add_interval_set(sets = 3, long_rest_duration = 3, reps = 5, effort_duration = 40 / 60, effort_start_ftp = 180,
                      rest_duration=20 / 60)
test.add_interval(duration=5, start_ftp=30)
test.add_interval(duration=10, start_ftp=110)
test.add_interval(duration=3, start_ftp=30)
test.add_interval_block(reps = 2, effort_duration=5, effort_start_ftp=130, rest_duration=3, rest_start_ftp=50)
test.add_10min_easy()

# Export workout as an MRP file to the specified destination
test.export_mrp_file('C:/Users/rlybr/Desktop/Workouts')