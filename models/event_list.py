from models.event import *
import datetime

event1 = Event(
    datetime.date(2022, 6, 5),
    "Queen's Jubilee",
    500,
    "Edinburgh",
    "Street party to celebrate the Queen",
    False,
)

event2 = Event(
    datetime.date(2022, 7, 3), "Moath's Birthday", 15, "Newcastle", "Party", True
)

event3 = Event(
    datetime.date(2022, 2, 21),
    "Sandy's Birthday",
    2,
    "Ottawa",
    "Opening presents",
    True,
)

events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)


def delete_event(index):
    events.pop(index)
