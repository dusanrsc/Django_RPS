from django.shortcuts import render

import random
from random import randint

# Create your views here.
# 0 stands for rock
# 1 stands for paper
# 2 stands for scissors
def index(request):
	cpu = random.randint(0, 2)
	player = random.randint(0, 2)
	return render(request, "index.html", {"cpu": cpu, "player": player})

def rock(request):
	cpu = random.randint(0, 2)
	player = 0
	return render(request, "rock.html", {"cpu": cpu, "player": player})

def paper(request):
	cpu = random.randint(0, 2)
	player = 1
	return render(request, "paper.html", {"cpu": cpu, "player": player})

def scissors(request):
	cpu = random.randint(0, 2)
	player = 2
	return render(request, "scissors.html", {"cpu": cpu, "player": player})