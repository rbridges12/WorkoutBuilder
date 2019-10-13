from Workout import *

file_name = ''
description = ''

test = Workout(units = 'english', file_name = file_name, description = description, time_unit='minutes', ftp_unit='percent')

test.add_interval(12, 30)
test.add_interval_set(5, 3, 110, 1.5, 40)
test.add_interval(10, 30)

# Export workout as an MRP file to the specified destination
test.export_mrp_file('')