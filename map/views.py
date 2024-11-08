from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from map.models import Marker

def index(request):
    context = {}
    return render(request, "map/index.html", context)



@csrf_exempt
def save_marker(request):
    if request.method == 'POST' and request.user.is_authenticated:
        data = json.loads(request.body)
        title = data['title']
        description = data['description']
        latitude = data['latitude']
        longitude = data['longitude']
        
        # Save marker to database
        marker = Marker.objects.create(
            user=request.user,
            title=title,
            description=description,
            latitude=latitude,
            longitude=longitude
        )
        return JsonResponse({'success': True, 'marker_id': marker.id})
    return JsonResponse({'success': False})

def get_markers(request):
    #if request.user.is_authenticated:
        markers = Marker.objects.all()
        markers_data = [
            {
                'id': marker.id, 
                'title': marker.title, 
                'description': marker.description,
                'latitude': marker.latitude, 
                'longitude': marker.longitude,
                'username': marker.user.username
            } 
            for marker in markers
        ]
        return JsonResponse(markers_data, safe=False)
    #return JsonResponse({'success': False})