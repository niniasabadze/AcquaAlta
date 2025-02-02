from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from map.models import Location, Marker
from django.utils.dateformat import DateFormat
from django.contrib.auth.decorators import login_required
import numpy as np
from django.core.cache import cache

API_KEY = "3534baf72dbcd1d79ae791c8240b6a74"
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
        raindrop_count=data['raindrop_count']

        marker = Marker.objects.create(
            title=title,
            description=description,
            disruption_type=disruption_type,
            raindrop_count=raindrop_count,
            latitude=latitude,
            longitude=longitude,
            user=request.user
        )
        return JsonResponse({'success': True, 'marker_id': marker.id})
    return JsonResponse({'success': False})

def get_markers(request):
    
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
                'raindrop_count': marker.raindrop_count,
                'username': marker.user.username,
                'created_at': DateFormat(marker.created_at).format('Y-m-d H:i:s')
            }
            for marker in markers
        ]
        return JsonResponse({'markers': markers_data, 'authenticated': user_authenticated})

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
            return JsonResponse({
                'status': 'success',
                'thumbs_up_count': marker.like_count,
                'thumbs_down_count': marker.dislike_count
            })
        except Marker.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Marker not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def fetch_street_coordinates(request):
    bbox = "9.1122,45.4215,9.2560,45.5115"

    
    query = f"""
    [out:json];
    way["highway"]({bbox});
    (._;>;);
    out body;
    """
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    response = requests.get(overpass_url, params={'data': query})
    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=500)

# def fetch_street_coordinates(request):
#     cache_key = "milan_street_data"
#     street_data = cache.get(cache_key)
    
#     bbox = "9.1122,45.4215,9.2560,45.5115"

    
#     if not street_data:
#         bbox = "9.1122,45.4215,9.2560,45.5115"
#         query = f"""
#         [out:json];
#         way["highway"~"primary|secondary|tertiary|residential"]({bbox});
#         (._;>;);
#         out body;
#         """
#         overpass_url = "https://overpass-api.de/api/interpreter"
        
#         response = requests.get(overpass_url, params={'data': query})
        
#         if response.status_code == 200:
#             street_data = response.json()
#             cache.set(cache_key, street_data, timeout=3600)  # Cache for 1 hour
#         else:
#             return JsonResponse({'error': 'Failed to fetch street data'}, status=500)
    
#     return JsonResponse(street_data, safe=False)

# def fetch_weather(lat, lon):
#     cache_key = f"weather_{lat}_{lon}"
#     weather_data = cache.get(cache_key)

#     if not weather_data:
#         api_key = '6a1620c55efb7c9d49e20ca92b7b352b'
#         url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             weather_data = response.json()
#             cache.set(cache_key, weather_data, timeout=600)  # Cache for 10 minutes
#         else:
#             return {'error': 'Failed to fetch weather data'}
    
#     return weather_data