from django.urls import path
from .views import AdminDashboardView, StudentDashboardView, dashboard_redirect

urlpatterns = [
    path("", dashboard_redirect, name="home"),
    path("dashboard/", dashboard_redirect, name="dashboard_redirect"),
    path("dashboard/student/", StudentDashboardView.as_view(), name="student_dashboard"),
    path("dashboard/admin/", AdminDashboardView.as_view(), name="admin_dashboard"),
]