
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view


from post.models import Post
from post.api.serializers import PostSerializer



@csrf_exempt
def post_list_api(request):
    """
    List all pot view API.
    """
    if request.method == 'GET':
        post_list = Post.objects.all()
        serializer = PostSerializer(post_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    


@api_view(['GET'])
def post_detailed_api(request, pk):
    """
    Post Detailed View API.
    """
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)



@api_view(['DELETE'])
def post_delete_api(request, pk):
    """
    Post Delete API.
    """
    try:
        post = Post.objects.get(pk=pk)
        
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=204)


@api_view(['PUT'])
def post_update_api(request, pk):
    """
    Post Update/Edit API.
    """
    try:
        post = Post.objects.get(pk=pk)
        
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

