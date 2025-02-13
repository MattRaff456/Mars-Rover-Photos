import requests
from PIL import Image
from io import BytesIO

api_key = '2IfEbWjWyx60xCYslBXDnk0kQJzl3MxvHbY8ZlL9'
rover = 'curiosity'
sol = 1000 #Martian day
camera = 'fhaz' #Front Hazard Avoidance Camera

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'

params = {
    'sol': sol,
    'camera': camera,
    'api_key': api_key
}

response = requests.get(url, params=params)
data = response.json()

if data['photos']:
    photos = data['photos'][:10]
    photo_url = data['photos'][0]['img_src']
    response = requests.get(photo_url)
    img = Image.open(BytesIO(response.content))
    img.show()
else:
    print('Beep boop beep! No photos found for the given parameters.')