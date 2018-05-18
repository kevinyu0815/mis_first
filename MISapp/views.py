from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import MemberTable

# Create your views here.
def login(request):
	if 'ok' in request.POST:
		email = request.POST["email"]
		password = request.POST["password"]
		try:
			correct = MemberTable.objects.get(email=email)
			#用filter 才要 correct = correct[0]
		except:
			correct = None
			
		if email == "f7123442@gmail.com" and password == "29948545":
			manage = True
		elif correct != None and email == correct.email and password == correct.password:
			verified = True
			#template = get_template('dialog.html')
			#html = template.render(locals())
			#return HttpResponse(html)

		else:
			verified = False
			

	template = get_template('login.html')
	members = MemberTable.objects.all()
	html = template.render(locals())
	return HttpResponse(html)


def register(request):
	if 'ok' in request.POST:
		name = request.POST["name"]
		email = request.POST["email"]
		password = request.POST["password"]
		gender = request.POST["gender"]
		birthday = request.POST["birthday"]
		MemberTable.objects.create(name=name, email=email, password=password, gender=gender, birthday=birthday)
	

	template = get_template('register.html')
	html = template.render(locals())
	return HttpResponse(html)


def dialog(request):
	
	template = get_template('dialog.html')
	html = template.render(locals())
	return HttpResponse(html)


def manager(request):
	template = get_template('manager.html')
	html = template.render(locals())
	return HttpResponse(html)



