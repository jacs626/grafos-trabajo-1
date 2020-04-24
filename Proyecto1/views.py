from django.http import HttpResponse

def saludo (request):

    return HttpResponse("Primer pagina con django")

    