from django.shortcuts import render
from .models import Position, Player, Staff
# Create your views here.

def team_page(request):
	positions = Position.objects.all()
	players = Player.objects.all()
	staff = Staff.objects.all()

	contex = {
		'positions': positions,
		'players': players,
		'staff': staff,
	}
	return render(request, 'team_page.html', contex)