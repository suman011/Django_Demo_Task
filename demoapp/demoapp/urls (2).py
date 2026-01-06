from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, task_weather, report_tasks, dashboard

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/tasks/<int:pk>/weather/", task_weather),
    path("api/reports/tasks/", report_tasks),
    path("", dashboard),
]
