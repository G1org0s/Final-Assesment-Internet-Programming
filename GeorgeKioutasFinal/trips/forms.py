from django import forms


# This form creates the boxes that user fills in the trips page
class TripForm(forms.Form):
    # max_length is validation, so Django does not accept too much text
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


# This small form decides how the trips are ordered
class SortTripsForm(forms.Form):
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
