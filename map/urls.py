from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="map-index"),
    path('save_marker/', views.save_marker, name='save_marker'),
    path('get_markers/', views.get_markers, name='get_markers'),
    path("get_rainfall_data/", views.get_rainfall_data, name="get_rainfall_data"),
    path('vote/<int:marker_id>/', views.vote_marker, name='vote_marker'),
]