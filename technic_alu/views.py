from django.http import JsonResponse
from technic_alu.controllers.gallery_image import get_gallery_images_by_page_id


def get_gallery_images(request):
    page_id = request.GET.get('page_id', None)
    return JsonResponse(
        {
            'data': get_gallery_images_by_page_id(page_id)
        },
        json_dumps_params={'indent': 2}
    )
