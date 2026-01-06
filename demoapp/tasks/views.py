import requests
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

@api_view(['GET'])
def task_weather(request, pk):
    task = Task.objects.get(pk=pk)
    if not task.city:
        return Response({'error': 'City not set'})
    geo = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={'name': task.city, 'count': 1}).json()
    lat = geo['results'][0]['latitude']
    lon = geo['results'][0]['longitude']
    weather = requests.get('https://api.open-meteo.com/v1/forecast', params={'latitude': lat, 'longitude': lon, 'current': 'temperature_2m'}).json()
    return Response(weather['current'])

@api_view(['GET'])
def report_tasks(request):
    return Response({
        'total': Task.objects.count(),
        'by_status': list(Task.objects.values('status').annotate(count=Count('id')))
    })

def dashboard(request):
    return render(request, 'tasks/dashboard.html')
