"""
    Views for interview app
"""

from django.http import JsonResponse

MYJSON = {}
MYJSON['Name'] = 'Michael Fulton'
MYJSON['Phone Number'] = 8326933348
MYJSON['Email'] = 'mike@michaelfulton.co'

def index(_):
    """
        The main endpoint of the interview application app.
    """
    return JsonResponse(MYJSON)

