from django.shortcuts import render

# This view opens the analytics page with the chart.
def analytics(request):
    return render(request, "analytics/analytics.html")
