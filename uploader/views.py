from django.http import FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from uploader.models import Document


@csrf_exempt
def download(request):
    file_id = int(request.POST['file_id'])
    doc = Document.objects.get(id=file_id)
    opened_file = open(doc.doc.path, mode='rb')
    return FileResponse(opened_file, as_attachment=True)


@csrf_exempt
def upload(request):
    try:
        file = request.FILES['attachment']
        Document.objects.create(doc=file)
        return JsonResponse(status=200, data={'msg': 'done'})
    except Exception as e:
        return JsonResponse(status=500, data={'msg': 'error'})
