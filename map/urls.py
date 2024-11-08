from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="map-index"),
    path('save_marker/', views.save_marker, name='save_marker'),
    path('get_markers/', views.get_markers, name='get_markers'),
]