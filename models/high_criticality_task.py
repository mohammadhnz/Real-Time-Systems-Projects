import configs
from . import BaseTask


class HighCriticalityTask(BaseTask):
    def __init(self, little_computation_time: int, big_computation_time: int, period: int):
        super().__init__(period, configs.CriticalityValues.HIGH)
        self.little_computation_time = little_computation_time
        self.big_computation_time = big_computation_time
        self.period = period
        self.virtual_deadline = None

    def get_deadline(self, mode: configs.Mode):
        release_time = self.current_job * self.period
        if mode == configs.Mode.NORMAL:
            return release_time + self.deadline
        else:
            return release_time + self.virtual_deadline

    def get_computation_time(self, mode: configs.Mode):
        if mode == configs.Mode.NORMAL:
            return self.little_computation_time
        else:
            return self.big_computation_time
