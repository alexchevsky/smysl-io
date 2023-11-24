from django.http import JsonResponse

def health(request):
    data = {
        "status_code": 200,
        "message": "API is online"
    }
    return JsonResponse(data)
