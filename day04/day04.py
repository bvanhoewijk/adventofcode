#!/usr/bin/env python3
import re
from pprint import pprint
from datetime import datetime
import numpy as np

# [1518-11-22 00:00] Guard #1231 begins shift
# [1518-04-13 00:00] falls asleep
# [1518-09-09 00:02] falls asleep
# [1518-04-06 00:58] wakes up
def parse_input(date_item):
    # Pretty regex:
    m = re.search(r"\[(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2})\] (.+)", date_item)
    # Cast dates to int and stick it in a date object
    # @joachim: pretty aint it?  :-)
    dt = datetime(*[int(group) for group in m.groups()[0:5]])
    return {"status": m.group(6), "datetime": dt}


def guardid(status):
    m = re.search(r"Guard #(\d+)", status)
    return int(m.group(1))


def minutes_asleep(list_of_dates):
    guard_sleep = {}
    current_guard = ""
    asleep = 0

    for entry in list_of_dates:
        if entry["status"].startswith("Guard"):
            current_guard = guardid(entry["status"])
        elif entry["status"].startswith("falls"):
            asleep = entry["datetime"].minute
        elif entry["status"].startswith("wakes"):
            awake = entry["datetime"].minute
            if current_guard != "":
                if current_guard in guard_sleep:
                    guard_sleep[current_guard]["minutes"] += awake - asleep
                    guard_sleep[current_guard]["timetable"][asleep:awake] += 1
                else:
                    timetable = np.zeros(60)
                    timetable[asleep:awake] += 1
                    guard_sleep[current_guard] = {
                        "minutes": awake - asleep,
                        "timetable": timetable,
                    }

    return guard_sleep


if __name__ == "__main__":
    list_of_dates = [parse_input(line.rstrip()) for line in open("input.txt")]
    list_of_dates = sorted(list_of_dates, key=lambda k: k["datetime"])
    guard_sleep = minutes_asleep(list_of_dates)

    # Ugly ugly for loop, but gets the job done:
    guardname = None
    timetable = None
    max_sleep = 0
    for guard in guard_sleep:
        if guard_sleep[guard]["minutes"] > max_sleep:
            max_sleep = guard_sleep[guard]["minutes"]
            guardname = guard
            timetable = guard_sleep[guard]["timetable"]

    most_asleep = np.argmax(timetable)
    ## Part1
    print(
        "Guard #%s slept the most with %s minutes! At most at minute %s"
        % (guardname, max_sleep, most_asleep)
    )
    print(
        "Code for part1 %s x %s = %s"
        % (guardname, most_asleep, guardname * most_asleep)
    )

    print("--------")
    ## Part2
    max_per_guard = [np.max(guard_sleep[guard]["timetable"]) for guard in guard_sleep]
    guardnames = [guard for guard in guard_sleep]
    guard_id = guardnames[np.argmax(max_per_guard)]
    print("Max per guard %s" % np.max(max_per_guard))
    print("Guardname with max minutes a sleep: %s" % guard_id)
    print(
        "Minute most asleep                : %s"
        % np.argmax(guard_sleep[guard_id]["timetable"])
    )
    print(
        "Code for part2                    : %s"
        % (guard_id * np.argmax(guard_sleep[guard_id]["timetable"]))
    )

