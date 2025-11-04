from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_api(request):
    if request.method == 'GET':
        return JsonResponse({
            'message': 'API is working!',
            'status': 'success',
            'data': {
                'version': '1.0',
                'framework': 'Django'
            }
        })