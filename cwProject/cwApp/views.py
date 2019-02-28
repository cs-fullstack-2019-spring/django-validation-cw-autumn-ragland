from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewCarForm
from .models import NewCarModel


# render form, check if form is valid, throw up errors or render submission page
def index(request):
    if request.method == 'POST':
        form = NewCarForm(request.POST)
        if form.is_valid():
            NewCarModel.objects.create(make=request.POST['make'], modelYear=request.POST['modelYear'], mpg=request.POST['mpg'])
            return render(request, 'cwApp/submit.html')
        else:
            allCars = NewCarModel.objects.all()
            context = {
                'errors': form.errors,
                'form': form,
                'allCars': allCars
            }
            return render(request, 'cwApp/index.html', context)

    allCars = NewCarModel.objects.all()
    form = NewCarForm()
    context = {
        'form': form,
        'allCars': allCars
    }
    return render(request, 'cwApp/index.html', context)

# function called if form is valid
def submission(request):
    return render(request, 'cwApp/submit.html')
