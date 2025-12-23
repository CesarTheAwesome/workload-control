# This file contains the Shift class for workload-control.py

class Shift:
  def __init__(self, date, start_time, end_time, job, hours_worked):
    # Initializes the attributes for a new shift instance
    self.date = ''
    self.start_time = '' 
    self.end_time = ''
    self.job = ''
    self.hours_worked = 0.0

  def calculate_hours_worked(self):
        duration = self.end_time - self.start_time
        
        # Handle overnight shifts
        if duration.total_seconds() < 0:
            duration += timedelta(days=1)
        
        self.hours_worked = duration.total_seconds() / 3600  # convert to hours
        return self.hours_worked
