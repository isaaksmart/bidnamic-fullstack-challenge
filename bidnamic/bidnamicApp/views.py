from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Bidnamic

from .forms import BidnamicForm

def return_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BidnamicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.clean_birthday()
            form.save()
            # redirect to a new URL:
            return BidnamicForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        return BidnamicForm()

def index(request):
    bidnamic_objects = Bidnamic.objects.all()
    form = return_form(request)
    context = {'form': form, 'model': bidnamic_objects}
    return render(request, 'form.html', context)


def delete(request, item):
    print(request)
    Bidnamic.objects.filter(id=item).delete()
    bidnamic_objects = Bidnamic.objects.all()
    form = return_form(request)
    context = {'form': form, 'model': bidnamic_objects}
    return render(request, 'form.html', context)