from django import forms
from django.shortcuts import render


# This form creates the boxes that user fills in the trips page.
class TripForm(forms.Form):
    # max_length is validation, so Django does not accept too much text.
    trip_name = forms.CharField(
        label="Trip Name",
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ex. Peloponnese",
            "pattern": "[A-Za-z ]+",
            "title": "Use only letters and up to 30 characters.",
        })
    )
    trip_location = forms.CharField(
        label="Trip Location",
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ex. Pylos",
            "pattern": "[A-Za-z ]+",
            "title": "Use only letters and up to 30 characters.",
        })
    )
    trip_date = forms.CharField(
        label="Trip Date",
        max_length=20,
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date",
        })
    )
    trip_description = forms.CharField(
        label="Trip Description",
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ex. Area known for sea breams",
            "pattern": "[A-Za-z ]+",
            "title": "Use only letters and spaces, up to 30 characters.",
        })
    )


class SortTripsForm(forms.Form):
    # This small form decides how the trips are ordered.
    sort_order = forms.ChoiceField(
        label="Sort Trips by Date",
        choices=[
            ("earliest", "Earliest First"),
            ("latest", "Latest First"),
        ],
        widget=forms.Select(attrs={
            "class": "form-select",
            "onchange": "this.form.submit()",
        })
    )


# This list is used like the task list from the lesson example.
trips_list = [
    {
        "trip_id": 1,
        "trip_name": "Athens Barracuda Trip",
        "trip_location": "Athens",
        "trip_date": "2026-01-12",
        "trip_description": "A fishing trip near Athens",
        "trip_status": "Completed",
    },
    {
        "trip_id": 2,
        "trip_name": "Pylos Amberjack Trip",
        "trip_location": "Pylos",
        "trip_date": "2026-02-08",
        "trip_description": "A completed trip in Pylos",
        "trip_status": "Completed",
    },
    {
        "trip_id": 3,
        "trip_name": "Laurio Match Fishing Day",
        "trip_location": "Laurio",
        "trip_date": "2026-03-15",
        "trip_description": "A relaxing fishing day",
        "trip_status": "Completed",
    },
    {
        "trip_id": 4,
        "trip_name": "Agia Marina Egi Trip",
        "trip_location": "Agia Marina",
        "trip_date": "2026-04-10",
        "trip_description": "Fishing at Agia Marina",
        "trip_status": "Completed",
    },
    {
        "trip_id": 5,
        "trip_name": "Xylokastro Casting Trip",
        "trip_location": "Xylokastro",
        "trip_date": "2026-05-17",
        "trip_description": "A shore fishing trip",
        "trip_status": "Completed",
    },
]


def next_trip_id():
    # This makes a simple new id for the next trip.
    biggest_id = 0

    for trip in trips_list:
        if trip["trip_id"] > biggest_id:
            biggest_id = trip["trip_id"]

    return biggest_id + 1


# This view opens the trips page and checks the trip form.
def trips(request):
    sort_order = "earliest"
    weather_text = "Partly cloudy (30.5 C)"

    # POST means the user pressed the save button and sent the form.
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "complete":
            # The hidden trip_id tells Django which trip to complete.
            trip_id = int(request.POST["trip_id"])

            for trip in trips_list:
                if trip["trip_id"] == trip_id:
                    trip["trip_status"] = "Completed"
            form = TripForm()
            sort_form = SortTripsForm()

        elif action == "delete":
            # Delete removes one trip from the simple list.
            trip_id = int(request.POST["trip_id"])

            for trip in trips_list:
                if trip["trip_id"] == trip_id:
                    trips_list.remove(trip)
                    break
            form = TripForm()
            sort_form = SortTripsForm()

        elif action == "sort":
            sort_form = SortTripsForm(request.POST)

            if sort_form.is_valid():
                sort_order = sort_form.cleaned_data["sort_order"]
            form = TripForm()

        else:
            form = TripForm(request.POST)
            sort_form = SortTripsForm()

            # is_valid checks the form rules before the data is used.
            if form.is_valid():
                # cleaned_data has the safe data after Django checked the form.
                trips_list.append({
                    "trip_id": next_trip_id(),
                    "trip_name": form.cleaned_data["trip_name"],
                    "trip_location": form.cleaned_data["trip_location"],
                    "trip_date": form.cleaned_data["trip_date"],
                    "trip_description": form.cleaned_data["trip_description"],
                    "trip_status": "Pending",
                })
            else:
                # If something is wrong, show the same form with the errors.
                return render(request, "trips/trips.html", {
                    "form": form,
                    "sort_form": sort_form,
                    "trips": trips_list,
                    "pending_count": 0,
                    "completed_count": 0,
                    "weather_text": weather_text,
                })
    else:
        # This empty form is shown the first time the page opens.
        form = TripForm()
        sort_form = SortTripsForm()

    shown_trips = trips_list[:]

    # This is the same sorting idea, but done in Python.
    if sort_order == "latest":
        shown_trips.sort(key=lambda trip: trip["trip_date"], reverse=True)
    else:
        shown_trips.sort(key=lambda trip: trip["trip_date"])

    pending_count = 0
    completed_count = 0

    # Count pending and completed trips for the small status box.
    for trip in trips_list:
        if trip["trip_status"] == "Completed":
            completed_count += 1
        else:
            pending_count += 1

    # Send the form and the trips list to the html page.
    return render(request, "trips/trips.html", {
        "form": form,
        "sort_form": sort_form,
        "trips": shown_trips,
        "pending_count": pending_count,
        "completed_count": completed_count,
        "weather_text": weather_text,
    })
