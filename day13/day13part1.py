# floor(earliest time / id) = previous bus
# previous bus + id = next bus

import collections
import math

with open('day13/input.txt', 'r') as file:
    notes = file.read().splitlines()

    earliest_timestamp = int(notes[0])
    buses = notes[1].split(",")

    bus_next_departures = collections.defaultdict(int)
    for bus in buses:
        if bus != "x":
            bus_id = int(bus)
            bus_next_departures[bus_id] = ((math.floor(earliest_timestamp / bus_id)) * bus_id) + bus_id

    bus_to_take = min(bus_next_departures.keys(), key=(lambda k: bus_next_departures[k]))
    bus_departure = bus_next_departures[bus_to_take]
    time_to_wait = bus_departure - earliest_timestamp
    answer = bus_to_take * time_to_wait
    print(answer)
