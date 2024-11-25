from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from map.models import Location, Marker
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required

API_KEY = "6a1620c55efb7c9d49e20ca92b7b352b"
API_URL = "http://api.openweathermap.org/data/2.5/weather"

def index(request):
    context={}
    return render(request, "map/index.html", context)



@csrf_exempt
@login_required
def save_marker(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        description = data['description']
        disruption_type = data['disruption_type']
        latitude = data['latitude']
        longitude = data['longitude']

        marker = Marker.objects.create(
            title=title,
            description=description,
            disruption_type=disruption_type,
            latitude=latitude,
            longitude=longitude,
            user=request.user
        )
        return JsonResponse({'success': True, 'marker_id': marker.id})
    return JsonResponse({'success': False})
def get_markers(request):
    #if request.user.is_authenticated:
        markers = Marker.objects.all()
        user_authenticated = request.user.is_authenticated
        markers_data = [
            {
                'id': marker.id, 
                'title': marker.title, 
                'description': marker.description,
                'latitude': marker.latitude, 
                'longitude': marker.longitude,
                'disruption_type': marker.disruption_type,
                'like_count': marker.like_count,
                'dislike_count': marker.dislike_count,
                'username': marker.user.username,
                'created_at': DateFormat(marker.created_at).format('Y-m-d H:i:s')
            }
            for marker in markers
        ]
        return JsonResponse({'markers': markers_data, 'authenticated': user_authenticated})
    #return JsonResponse({'success': False})

def get_rainfall_data(request):
    api_key = "your_openweather_api_key"
    locations = Location.objects.all()
    rain_locations = []

    for loc in locations:
        # Fetch weather data for each location
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": loc.latitude,
                "lon": loc.longitude,
                "appid": api_key,
                "units": "metric"
            },
        )
        data = response.json()
        rain = data.get("rain", {}).get("1h", 0)  # Rainfall in mm/h
        
        if rain > 0.1:
            rain_locations.append({
                "address": loc.address,
                "latitude": loc.latitude,
                "longitude": loc.longitude,
                "rain": rain
            })

    return JsonResponse(rain_locations, safe=False)

@csrf_exempt
def vote_marker(request, marker_id):
    if request.method == 'POST':
        try:
            marker = Marker.objects.get(id=marker_id)
            data = json.loads(request.body)
            if data.get('thumbs_up'):
                marker.like_count += 1
            else:
                marker.dislike_count += 1
            marker.save()
            return JsonResponse({'status': 'success', 'thumbs_up_count': marker.like_count, 'thumbs_down_count': marker.dislike_count})
        except Marker.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Marker not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)