import random
from collections import deque

times = {'Change oil': 2, 'Inflate tires': 5, 'Get diagnostic': 30, }
_all = [0]
menu = {'change_oil': "Change oil", 'inflate_tires': "Inflate tires", 'diagnostic': "Get diagnostic", }
tickets = {'Change oil': [0, deque()], 'Inflate tires': [0, deque()], 'Get diagnostic': [0, deque()], }
next_ticket = 0


def get_waiting_time(service_type):
    time = 0
    if _all[0] < 2:
        return time
    for k, v in tickets.items():
        if times[k] <= times[service_type]:
            time += times[k] * v[0]
    return time


def do_next():
    global next_ticket
    for k, v in tickets.items():
        if v[0] > 0:
            v[0] -= 1
            next_ticket = v[1].popleft()
            # _all[0] -= 1
            return
    next_ticket = 0
    return


def get_next():
    return next_ticket

