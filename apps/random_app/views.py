from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'random_app/index.html') 

# def show(request):
# 	return render(request, 'vinmyMVC/show_users.html')

# def create(request):
# 	if request.method == "POST":
# 		print('*'*50)
# 		print (request.POST)
# 		print('*'*50)
# 		request.session['name'] =request.POST['first_name']
# 		return redirect('/')
# 	else:
# 		return redirect('/')