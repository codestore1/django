from django.http import HttpResponse,JsonResponse

def home(request):
    friend=[
        'ankit',
        'ravi',
        'raftaar'
    ]
    return JsonResponse(friend,safe=False)

