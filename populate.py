import datetime
from EventQueue import db
from EventQueue.event.event_model import Event

event = Event(
    name = "event 1",
    date = datetime.datetime.now(),
    location= "eventland",
    description = "the first of many. or none. who knows"
)

db.session.add(event)
db.session.commit()
