from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import song,podcast,audiobook
from tutorials.serializers import songSerializer
from rest_framework.decorators import api_view



@api_view(['GET', 'POST', 'DELETE'])
def song_list(request):
    if request.method == 'GET':
        songs = song.objects.all()
        Id = request.query_params.get('Id', None)
        if Id is not None:
            songs = songs.filter(title__icontains=Id)
        
        songs_serializer = songSerializer(songs, many=True)
        return JsonResponse(songs_serializer.data, safe=False)
         #'safe=False' for objects serialization
 
    elif request.method == 'POST':
    	
        song_data = JSONParser().parse(request)
        song_serializer = songSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #elif request.method == 'DELETE':
        #count = song.objects.all().delete()
       # return JsonResponse({'message': '{} song were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def song_d(request,pk):
    try: 
        song = song.objects.get(pk=pk) 
    except song.DoesNotExist: 
        return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        song_serializer = songSerializer(song) 
        return JsonResponse(song_serializer.data) 
 
    elif request.method == 'PUT': 
        song_data = JSONParser().parse(request) 
        song_serializer = songSerializer(song, data=song_data) 
        if song_serializer.is_valid(): 
            song_serializer.save() 
            return JsonResponse(song_serializer.data) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        song.delete()
        return JsonResponse({'message': 'song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def song_published(request):
    songs = song.objects.filter(published=True)
        
    if request.method == 'GET': 
        song_serializer = songSerializer(tutorials, many=True)
        return JsonResponse(song_serializer.data, safe=False)

def podcast_list(request):
    if request.method == 'GET':
        podcasts = podcast.objects.all()
        Id = request.query_params.get('Id', None)
        if Id is not None:
            podcasts = podcast.filter(title__icontains=Id)
        
        podcast_serializer = podcastSerializer(podcast, many=True)
        return JsonResponse(podcast_serializer.data, safe=False)
         #'safe=False' for objects serialization
 
    elif request.method == 'POST':
    	
        podcast_data = JSONParser().parse(request)
        podcast_serializer = songSerializer(data=podcast_data)
        if podcast_serializer.is_valid():
            podcast_serializer.save()
            return JsonResponse(podcast_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(podcast_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def podcast_d(request,pk):
	try:
		podcast = podcast.objects.get(pk=pk)
	except podcast.DoesNotExist:
		return JsonResponse({'message': 'The podcast does not exist'}, status=status.HTTP_404_NOT_FOUND)
	if request.method == 'GET':
		podcast_serializer = podcastSerializer(podcast)
		return JsonResponse(podcast_serializer.data)
	elif request.method == 'PUT':
		podcast_data = JSONParser().parse(request)
		podcast_serializer = podcastSerializer(podcast, data=podcast_data)
		if podcast_serializer.is_valid():
			podcast_serializer.save()
			return JsonResponse(podcast_serializer.data)
		return JsonResponse(podcast_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		podcast.delete()
		return JsonResponse({'message': 'podcast was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

	


@api_view(['GET'])
def podcast_published(request):
	
	podcast = podcast.objects.filter(published=True)
	if request.method == 'GET':
		podcast_serializer = podcastSerializer(tutorials, many=True)
		return JsonResponse(podcast_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def audiobook_list(request):
    if request.method == 'GET':
        audiobooks = audiobook.objects.all()
        Id = request.query_params.get('Id', None)
        if Id is not None:
            audiobooks = audiobooks.filter(title__icontains=Id)
        
        audiobooks_serializer = audiobookSerializer(audiobooks, many=True)
        return JsonResponse(audiobooks_serializer.data, safe=False)
         #'safe=False' for objects serialization
 
    elif request.method == 'POST':
    	
        song_data = JSONParser().parse(request)
        song_serializer = songSerializer(data=song_data)
        if song_serializer.is_valid():
            song_serializer.save()
            return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def audiobook_d(request,pk):
	if type_slug=="audiobook":
		try:
			audiobook = audiobook.objects.get(pk=pk)
		except audiobook.DoesNotExist:
			return JsonResponse({'message': 'audiobook does not exist'}, status=status.HTTP_404_NOT_FOUND)
		if request.method == 'GET':
			podcast_serializer = podcastSerializer(audiobook)
			return JsonResponse(audiobook_serializer.data)
		elif request.method == 'PUT':
			audiobook_data = JSONParser().parse(request)
			audiobook_serializer = podcastSerializer(audiobook, data=audiobook_data)
			if podcast_serializer.is_valid():
				podcast_serializer.save()
				return JsonResponse(audiobook_serializer.data)
			return JsonResponse(podcast_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif request.method == 'DELETE':
			audiobook.delete()
			return JsonResponse({'message': 'audiobook was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


def audiobook_published(request):
	audiobook = audiobook.objects.filter(published=True)
	if request.method == 'GET':
		song_serializer = songSerializer(tutorials, many=True)
		return JsonResponse(song_serializer.data, safe=False)
	








