from django.shortcuts import render
from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Muh. Syarief Mulyadi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
