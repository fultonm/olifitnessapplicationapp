"""
    Views for root app
"""

from django.http import HttpResponse

def index(_):
    """
        The main endpoint of the interview application app.
    """
    return HttpResponse('<h1>Try curling or navigating to <a href="https://ancient-taiga-22974.herokuapp.com/interview/">https://ancient-taiga-22974.herokuapp.com/interview</a></h1>')

