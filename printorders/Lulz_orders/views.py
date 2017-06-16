from django.shortcuts import render, redirect
from django.http import HttpResponse

from Lulz_orders.forms import GenericSTLForm


# Create your views here.
def index(request):
    return HttpResponse("This will be the place where student can order their prints")


def submit_stl(request):
    if request.method == 'POST':
        form = GenericSTLForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GenericSTLForm()
    return render(request, 'Lulz_orders/test_form.html', {'form': form})
