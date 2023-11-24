from django.http import JsonResponse, Http404, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Task, Token
from django.utils import timezone

def health(request):
    data = {
        "status_code": 200,
        "message": "API is online"
    }
    return JsonResponse(data)

def tasks(request):
    tasks = Task.objects.all().values('id', 'is_public')
    return JsonResponse(list(tasks), safe=False)

def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")

    if not task.is_public:
        token_value = request.headers.get('Authorization')
        if not token_value:
            return HttpResponseForbidden("Access denied: No token provided for private task")

        try:
            token = Token.objects.get(token=token_value, expires_at__gt=timezone.now())
        except Token.DoesNotExist:
            return HttpResponseForbidden("Access denied: Invalid or expired token for private task")

    data = {
        'id': task.id,
        'description': task.description,
        'is_public': task.is_public
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    
@require_POST
@csrf_exempt
def get_token(request):
    email = request.POST.get('email')
    if not email:
        return JsonResponse({'error': 'Email is required'}, status=400)

    token = Token.objects.create(email=email)
    return JsonResponse({
        'api_token': token.token,
        'expires_at': token.expires_at.isoformat()
    })