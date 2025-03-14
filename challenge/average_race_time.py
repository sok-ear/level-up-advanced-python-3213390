# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime
import statistics
import math
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    rhine_times = []

    def get_times(line):
        return re.findall(r'\d{2}:\S+', line)[0]
    
    for line in races.splitlines():
        if "Jennifer Rhines" in line:
            rhine_times.append(get_times(line))
    return rhine_times

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()

    sum = datetime.timedelta()
    for racetime in racetimes:
        time_value = racetime.split(":")
        sum += datetime.timedelta(
            minutes=int(time_value[0]), 
            seconds=float(time_value[1]))

    avg = sum/len(racetimes)
    return f'{avg}'[2:-5]
