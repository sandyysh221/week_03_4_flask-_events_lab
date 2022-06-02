from flask import render_template, request
from app import app
from models.event_list import *
from models.event import Event


@app.route("/events")
def index():
    return render_template("index.html", title="Home", events=events)


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_number_of_guests = request.form["number_of_guests"]
    event_location = request.form["location"]
    event_description = request.form["description"]
    event_recurring = "recurring" in request.form
    new_event = Event(
        event_date,
        event_name,
        event_number_of_guests,
        event_location,
        event_description,
        event_recurring,
    )
    add_new_event(new_event)
    return render_template("index.html", title="Home", events=events)


@app.route("/events/delete/<index>", methods=["POST"])
def deletion_request(index):
    delete_event(int(index))
    return render_template("index.html", title="Home", events=events)
