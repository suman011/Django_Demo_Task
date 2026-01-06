import requests
from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer


@api_view(["GET"])
def task_weather(request, pk: int):
    """GET /api/tasks/<id>/weather/ - Open-Meteo integration"""
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=404)

    if not task.city:
        return Response({"error": "Task.city is empty. Add a city to the task."}, status=400)

    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": task.city, "count": 1},
        timeout=10,
    ).json()

    results = geo.get("results") or []
    if not results:
        return Response({"error": f"No location found for '{task.city}'"}, status=404)

    lat = results[0]["latitude"]
    lon = results[0]["longitude"]

    forecast = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m,wind_speed_10m"},
        timeout=10,
    ).json()

    return Response({
        "task_id": task.id,
        "city": task.city,
        "current": forecast.get("current", {}),
    })


@api_view(["GET"])
def report_tasks(request):
    """GET /api/reports/tasks/ - simple aggregation"""
    by_status = list(Task.objects.values("status").annotate(count=Count("id")).order_by("status"))
    by_priority = list(Task.objects.values("priority").annotate(count=Count("id")).order_by("priority"))

    return Response({
        "total": Task.objects.count(),
        "by_status": by_status,
        "by_priority": by_priority,
    })


def dashboard(request):
    return render(request, "tasks/dashboard.html")
