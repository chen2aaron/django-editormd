from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import EditormdImage
from .forms import ImageUploadForm


@csrf_exempt
def upload_image(request):
    result = {
        'success': 0,
        'message': 'Method not allowed'
    }
    if request.method == 'POST':
        request.FILES['image_file'] = request.FILES['editormd-image-file']
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = EditormdImage(**form.cleaned_data)
            instance.author = request.user
            instance.save()
            result['success'] = 1
            result['message'] = 'Upload image success'
            result['url'] = instance.image_file.url
            return JsonResponse(result)
        result['message'] = 'Upload image failed'
        return JsonResponse(result)
    return JsonResponse(result)
