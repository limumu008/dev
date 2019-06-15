from django.shortcuts import render

# Create your views here.

#salmon_roll = model.BooleanField(default=False)
#tuna_roll = model.BooleanField(default=False)
#mackeral_roll = model.BooleanField(default=False)
#eel_roll = model.BooleanField(default=False)
#yellow_tail_roll = model.BooleanField(default=False)
#california_roll = model.BooleanField(default=False)



def new_provider(request):
	if request.method == "POST":
		form = ProviderForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request,'provider_details.html',{'post':post})
	else:
		form = ProviderForm()
		return render(request,'provider_details.html',{'form':form})

def new_kitchen(request):
	if request.method == "POST":
		form = KitchenForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request,'kitchen_register.html',{'post':post})
	else:
		form = KitchenForm()
		return render(request,'kitchen_register.html',{'form':form})


def new_menu(request):
	if request.method == "POST":
		form = MenuForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return render(request,'kitchen_register.html',{'post':post})
	else:
		form = MenuForm()
		return render(request,'kitchen_register.html',{'form':form})