import math
from typing import List
from models import HighCriticalityTask, LowCriticalityTask
import random


def generate_task(core_utilization, count_of_cores, count_of_tasks, ratio) -> (List[HighCriticalityTask], List[LowCriticalityTask]):
    utilizations = []
    for i in range(count_of_cores):
        new_utilizations = _uunifast_algorithm(core_utilization, count_of_tasks // count_of_cores)
        utilizations.extend(new_utilizations)

    count_of_hc_tasks = int(count_of_tasks * ratio)
    hc_utilization = utilizations[:count_of_hc_tasks]
    lc_utilization = utilizations[count_of_hc_tasks:]

    hc_tasks = []
    for u in hc_utilization:
        # u = float(format(u, ".3f"))
        period = random.randint(10 ** 4, 10 ** 5)
        little_computation_time = math.ceil(u * period)
        big_computation_time = random.randint(little_computation_time, 2 * little_computation_time)
        hc_task = HighCriticalityTask(little_computation_time, big_computation_time, period, u)
        hc_tasks.append(hc_task)

    lc_tasks = []
    for u in lc_utilization:
        # u = float(format(u, ".3f"))
        period = random.randint(10 ** 4, 10 ** 5)
        computation_time = math.ceil(u * period)
        lc_task = LowCriticalityTask(computation_time, period, u)
        lc_tasks.append(lc_task)

    return hc_tasks, lc_tasks


def _uunifast_algorithm(core_utilization, count_of_tasks) -> List:
    utilizations = []
    sum_u = core_utilization
    for i in range(count_of_tasks - 1):
        next_sum_u = sum_u * random.random() ** (core_utilization / (count_of_tasks - i))
        utilizations.append(sum_u - next_sum_u)
        sum_u = next_sum_u
    utilizations.append(sum_u)

    sets = []
    if all(ut <= core_utilization for ut in utilizations):
        sets.extend(utilizations)

    return sets
