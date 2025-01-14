from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
@csrf_exempt
# decorator - helper function

def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)}) 
        # returns typecasted books dictionary into list
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)

        return JsonResponse(model_to_dict(book), status=201)
    
def even(request):
    response = ''
    num = [1,2,3,4,5,6,7,8,9]
    for i in num:
        rem = i%2
        if rem == 0:
            response += str(i) +"<br/>"
    return HttpResponse(response)    