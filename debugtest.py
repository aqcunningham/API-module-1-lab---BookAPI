from django.http import HttpResponse

def even(request):
    response = ''
    num = [1,2,3,4,5,6,7,8,9]
    for i in num:
        rem = 1/2
        if rem == 0:
            response += str(i) +"<br/>"
    return HttpResponse(response)