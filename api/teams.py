from api.models import team
import json
from django.http import HttpResponse

def insert_team(name, number):
    try:
        t = team(teamName=name, teamNumber=number)
        t.save()
        return True
    except:
        return False

def add_team(request):
    name = request.GET['name']
    number = request.GET['number']

    try:
        repeat_number = True
        team.objects.get(teamNumber=number)
    except:
        repeat_number = False

    if repeat_number:
        response = {'success': False, 'message': 'This team already exists!'}
    elif len(name) > 50:
        response = {'success': False, 'message': 'Come on. The team name is not that long.'}
    elif len(name) == 0:
        response = {'success': False, 'message': 'I am sure the team has a name.'}
    else:
        success = insert_team(name, number)

        if success:
            response = {'success': True, 'message': 'Success!'}
        else:
            response = {'success': False, 'message': 'This is an error with an incredibly horrible response message'}

    return HttpResponse(json.dumps(response), content_type="application/json")
