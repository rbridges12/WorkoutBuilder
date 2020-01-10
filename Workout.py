# class to represent workout files
# Riley Bridges
# 9/29/2019

import os


class Workout:



    def __init__(self, file_name: str, description: str, units: str = 'english', time_unit: str = 'minutes',
                 ftp_unit: str = 'percent', rest_ftp : int = 30):
        self.units = units
        self.description = description
        self.file_name = file_name
        self.time_unit = time_unit
        self.ftp_unit = ftp_unit
        self.default_rest_ftp = rest_ftp

        self.file_extension = '.mrc'
        self.VERSION = 2
        self.course_data = []
        self.current_time = 0



    # add an interval to the file with the specified duration and ftp percentage
    def add_interval(self, duration: float, start_ftp: float, end_ftp: float = None):
        if end_ftp is None: end_ftp = start_ftp

        start_point = (self.current_time, start_ftp)
        self.current_time += duration
        end_point = (self.current_time, end_ftp)

        self.course_data.append(start_point)
        self.course_data.append(end_point)



    # add a block of intervals, for each rep there will be an effort interval and a rest interval
    def add_interval_block(self, reps : int, effort_duration : float, effort_start_ftp : float, rest_duration : float,
                           rest_start_ftp : float = None, effort_end_ftp : float = None, rest_end_ftp : float = None):

        # if no rest_ftp is specified, make it the default
        if rest_start_ftp is None: rest_start_ftp = self.default_rest_ftp

        # add all reps but the last one
        for i in range(reps -1):
            self.add_interval(effort_duration, effort_start_ftp, effort_end_ftp)
            self.add_interval(rest_duration, rest_start_ftp, rest_end_ftp)

        # add the last rep with no rest, as it is the end of the set
        self.add_interval(effort_duration, effort_start_ftp, effort_end_ftp)



    # add a set of interval blocks, with longer rests between each set
    def add_interval_set(self, sets : int, long_rest_duration : int, reps : int, effort_duration :
    float, effort_start_ftp : float, rest_duration : float, rest_ftp : float = None, rest_start_ftp : float = None,
                         effort_end_ftp : float = None, rest_end_ftp : float = None):

        # if no rest_ftp is specified, make it the default
        if rest_ftp is None: rest_ftp = self.default_rest_ftp
        # add all blocks but the final one
        for i in range(sets - 1):
            self.add_interval_block(reps, effort_duration, effort_start_ftp, rest_duration, rest_start_ftp,
                                    effort_end_ftp, rest_end_ftp)
            self.add_interval(long_rest_duration, rest_ftp)

        # add the final block with no long rest afterwards
        self.add_interval_block(reps, effort_duration, effort_start_ftp, rest_duration, rest_start_ftp,
                                effort_end_ftp, rest_end_ftp)



    def add_10min_easy(self):
        # add a 10 min easy interval for warmup or cooldown
        self.add_interval(duration=10, start_ftp=50)



    def export_mrp_file(self, path):
        # Header
        file_str = '[COURSE HEADER]\nVERSION = ' + str(self.VERSION)
        file_str += '\nUNITS = {}'.format(self.units.upper())
        self.description += ', Total Time: ' + str(self.current_time)
        file_str += '\nDESCRIPTION = ' + str(self.description)
        file_str += '\nFILE NAME = ' + str(self.file_name)
        file_str += '\n' + str(self.time_unit).upper() + ' ' + str(self.ftp_unit).upper() + '\n[END COURSE HEADER]'

        # Data
        file_str += '\n[COURSE DATA]'
        for (time, ftp) in self.course_data:
            file_str += '\n{0:.2f}\t{1}'.format(time, ftp)
        file_str += '\n[END COURSE DATA]\n'

        if not os.path.exists(path): os.makedirs(path)

        with open(os.path.join(path, self.file_name + self.file_extension), 'w') as file:
            file.write(file_str)



    def get_current_time(self):
        return self.current_time
