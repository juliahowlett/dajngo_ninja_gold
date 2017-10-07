from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime 
import random
from random import randint
import datetime
from datetime import date

def index(request):
	if not ('total' in request.session and 'log' in request.session):
		request.session['total'] = 0
		request.session['log'] = []
	print("total gold =", request.session['total'])
	
	context = {
		'total' : request.session['total'],
		'logs' : request.session['log']
		}
	return render(request, "ninjagold/index.html", context)

def process_money(request):  #/process_money
	timestamp = datetime.datetime.now().strftime("%I:%M %p  %m/%d/%Y")
	location = request.POST['location']
	if request.POST['location'] == 'farm':
		gold = random.randint(10,20)
		request.session['total'] += gold
		message = 'Visited into a farm and dug up {} gold coins at {}'.format(gold,timestamp)
		request.session['log'].append(message)
	elif request.POST['location'] == 'cave':
		gold = random.randint(5,10)
		request.session['total'] += gold
		message = 'Spelunked into a cave and discovered {} gold coins at {}'.format(gold,timestamp)
		request.session['log'].append(message)
	elif request.POST['location'] == 'house':
		gold = random.randint(2,5)
		request.session['total'] += gold
		message = 'Cleaned a house and earned {} gold coins at {}'.format(gold,timestamp)
		request.session['log'].append(message)
	elif request.POST['location'] == "casino":	
		gold = random.randint(-50,50)
		request.session['total'] += gold
		if request.session['total'] > 0:
			if gold > 0:
				message = 'Gambled at a casino and won {} gold coins at {}'.format(gold,timestamp)
			elif gold < 0:
				message = 'Gambled at a casino and LOST {} gold coins at {}'.format(gold,timestamp)	
		else:
			message = 'Better get a real job. You are {} gold coins in debt.'.format(session['total'])
		request.session['log'].append(message)

	
	print ('location= ', request.POST['location'], 'gold= ', gold)	
	print ('message= ', message)
	
	return redirect('/index')   

def reset():
	request.session.pop('total')
	request.session.clear()  #clear session cache
	return redirect('/')  
