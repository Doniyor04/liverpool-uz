from django.shortcuts import render
from .models import Stadium, ClubAchievement, ImportantDate, Legend

# Create your views here.

def home_page(request):
    
    return render(request, 'home_page.html')

def stadium_page(request):
    stadium = Stadium.objects.get(name="Anfield")
    gallery = stadium.images.all()
    return render(request, 'stadium.html', {'stadium': stadium, 'gallery': gallery})

def contact_page(request):
    return render(request, 'contact_page.html')

def club_history_page(request):
    achievements = ClubAchievement.objects.all()
    importantDates = ImportantDate.objects.all()
    legends = Legend.objects.all()
    
    contex = {
        'achievements': achievements,
        'importantDates': importantDates,
        'legends': legends
    }
    return render(request, 'club_history.html', contex)
