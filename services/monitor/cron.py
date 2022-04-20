"""
Module to house the classes for the cron that will monitor youtube channels.
"""
import enum
from apscheduler.schedulers.background import BackgroundScheduler

class CadenceType(enum.Enum):
    """
    Enum to define some constants just to improve
    """
    SECONDS = 'every_x_seconds'
    MINUTES = 'every_x_minutes'
    HOURS = 'every_x_hours'
    DAYS = 'every_x_days'

class Cron():
    """
    Cron class which will be used to configure and run cron jobs.
    """
    def __init__(self):
        self.sched = BackgroundScheduler(daemon=True)

    def schedule_job(self, func, job_type='cron', frequency='*', cadence_type: CadenceType=CadenceType.HOURS):
        """
        Schedule the job stored in this object.
        """
        if cadence_type is CadenceType.SECONDS:
            self.sched.add_job(func, job_type, second=frequency)
        elif cadence_type is CadenceType.MINUTES:
            self.sched.add_job(func, job_type, minute=frequency)
        elif cadence_type is CadenceType.HOURS:
            self.sched.add_job(func, job_type, hour=frequency)
        elif cadence_type is CadenceType.DAYS:
            self.sched.add_job(func, job_type, day=frequency)
        else:
            raise Exception(f'Cadence Type {cadence_type} is not valid.')

    def stop_scheduler(self):
        """
        Cancel the job stored in this object.
        """
        self.sched.shutdown()

    def start_scheduler(self):
        """
        Start the job loop for scheduled jobs.
        """
        self.sched.start()
