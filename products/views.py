from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def homepage(request):
	return render(request,'homepage.html')

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			#only if all the fields are exist
			product = Product()
			product.Title = request.POST['title']
			product.Body = request.POST['body']
			try:
				Product.Source = request.POST['url']
			except:
				return render(request, 'create.html',{'error':"URL invalid"})
			product.Icon = request.FILES['icon']
			product.Image = request.FILES['image']
			product.Date = timezone.datetime.now()
			product.User_name = request.user
			product.save()
			return redirect('home')
		else:
			return render(request, 'create.html',{'error':"All field's must be filled!"})
	else:
		return render(request, 'create.html')