from django.http import HttpResponse


def monday(request):
    return HttpResponse('monday')


def tuesday(request):
    return HttpResponse('tuesday')
