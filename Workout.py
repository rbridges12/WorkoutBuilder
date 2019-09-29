# class to represent workout files
# Riley Bridges
# 9/29/2019

import os

class Workout:

    def __init__(self, units, description, file_name, time_unit, ftp_unit):
        self.units = units
        self.description = description
        self.file_name = file_name
        self.time_unit = time_unit
        self.ftp_unit = ftp_unit

        self.file_extension = '.mrc'
        self.VERSION = 2
        self.course_data = []
        self.current_time = 0

    def add_interval(self, duration, start_ftp, end_ftp = None):
        if end_ftp is None: end_ftp = start_ftp

        start_point = (self.current_time, start_ftp)
        self.current_time += duration
        end_point = (self.current_time, end_ftp)

        self.course_data.append(start_point)
        self.course_data.append(end_point)

    def add_interval_set(self, reps, effort_duration, effort_start_ftp, rest_duration, rest_start_ftp, effort_end_ftp = None, rest_end_ftp = None):
        for i in range(reps):
            self.add_interval(effort_duration, effort_start_ftp, effort_end_ftp)
            self.add_interval(rest_duration, rest_start_ftp, rest_end_ftp)

    def export_mrp_file(self, path):
        # Header
        file_str = '[COURSE HEADER]\nVERSION = ' + str(self.VERSION)
        file_str += '\nUNITS = {}'.format(self.units.upper())
        file_str += '\nDESCRIPTION = ' + str(self.description)
        file_str += '\nFILE NAME = ' + str(self.file_name)
        file_str += '\n' + str(self.time_unit).upper() + ' ' + str(self.ftp_unit).upper() + '\n[END COURSE HEADER]'

        #Data
        file_str += '\n[COURSE DATA]'
        for (time, ftp) in self.course_data:
            file_str += '\n{0:.2f}\t{1}'.format(time, ftp)
        file_str += '\n[END COURSE DATA]\n'

        if not os.path.exists(path): os.makedirs(path)

        with open(os.path.join(path, self.file_name + self.file_extension), 'w') as file:
            file.write(file_str)
