from django.shortcuts import render

from django.http import JsonResponse
from uuid import uuid4


from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from server.settings import MEDIA_URL
import os
from .decorators import user_is_superuser

@csrf_exempt
@user_is_superuser
def upload_image(request):
    if request.method != 'POST':
        return JsonResponse({"Error Message": "Wrong request"})

    # matching_post = Post.objects.filter(post=post).first()
    # if not matching_post:
    #     return JsonResponse({"Error Message": f"Wrong post ({post})"})
    
    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split('.')[-1]
    if file_name_suffix not in ['jpg', 'png', 'gif', 'jpeg']:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .git, .pjeg"})

    file_path = os.path.join(settings.MEDIA_ROOT, 'Posts', file_obj.name)
    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(settings.MEDIA_ROOT, 'Posts', file_obj.name)
    
    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

    return JsonResponse({
        "Message": "Image upload successfully",
        "location": os.path.join(settings.MEDIA_URL, 'Posts', file_obj.name)
    })


def image_list(request):
#     image_list: [
#     {title: 'Cat', value: 'cat.png'},
#     {title: 'Dog', value: 'dog.jpg'}
#   ]
    image_list = []
    my_list = os.listdir(os.path.join(settings.MEDIA_ROOT, 'Posts'))
    for file_name in my_list:
        image_list.append({
            "title": file_name,
            "value": os.path.join(settings.MEDIA_URL, 'Posts', file_name)
        })
    return JsonResponse(image_list, safe=False)