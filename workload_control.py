# workload_control.py
# Cesar Aguirre Elias
# This File is to run the main program. 

# import shift and job class
import Shift from shift
import Job from job

# Day 1: Hardcode two weeks of data.
# PSA = Patient Service Associate
# PSA shift -s 8:30am - 5:00pm
# Valet shift is 9am - 9pm
Week_1 = {'Monday': 'PSA', 'Tuesday': 'PSA', 'Wednesday': 'PSA', 'Thursday': 'PSA', 'Friday': 'PSA', 'Saturday': 'Off', 'Sunday': 'Off'}
Week_2 = {'Monday': 'PSA', 'Tuesday': 'PSA', 'Wednesday': 'PSA', 'Thursday': 'PSA', 'Friday': 'PSA', 'Saturday': 'Valet', 'Sunday': 'Valet'}

def main():
  # instantiate psa and valet job
  PSA = Job()
  valet = Job()

if __name__ == "__main__":
    main()
