from django.http import JsonResponse
from django.shortcuts import render
from app import models


# Create your views here.
def index(request):
    if request.method == 'GET':
        meetings = models.Meetings.objects.all().order_by('-created_at')
        return render(request, 'index.html', {'meetings': meetings})
    elif request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date') 
        models.Meetings.objects.create(title=title, date=date)
        return JsonResponse('Meeting recorded successfully.', safe=False)
    else:
        return JsonResponse('This method is not available!')