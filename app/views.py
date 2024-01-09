from django.shortcuts import render

import random
from random import randint

# Create your views here.
def index(request):
	cpu = random.randint(0, 2)
	player = random.randint(0, 2)

	# game logic
	# tie
	# if cpu == 0 and player == "rock":
	# 	# its tie
	# elif cpu == 1 and player == "paper":
	# 	# its tie
	# elif cpu == 2 and player == "scissors":
	# 	# its tie

	return render(request, "index.html", {"cpu": cpu, "player": player})