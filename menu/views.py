from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User

def homemenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    return render(request,'menu/home.html')



def loginmenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Steps
    # 1. Retrieve input entered by User by using request parameter
    # 2. Authenticate the User by passing username/password
    # 3. If success then return to Home page else show the error and ask for relogin
    if request.method == 'POST':
    	print("I am in POST request")
    	# Pass the field name to get the input value
    	unameEntered=request.POST['username']
    	passEntered=request.POST['password']
    	print("username :",unameEntered)
    	userObject = auth.authenticate(username=unameEntered, password=passEntered)

    	if userObject is not None:
    		# It create a session (Unique ID)
    		auth.login(request,userObject)
    		#messages.success(request, "You are now logged in")
    		print("User logged in")
    		return redirect('myhome')
    	else:
            print("Username/password invalid")
            messages.error(request,"Username/password invalid")
            return redirect("mylogin")
    else: 
    	return render(request,'menu/login.html')

def registermenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Logic to register the User
    # if request is GET then display the registration form
    # else if its POST request then process the Form - validate the user info and perform the action
    if request.method == 'POST':
        print("I am in POST request")
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print("username :",username)
        print("email :",email)
        print("password1 :",password1)
        print("password2 :",password2)

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.error(request,"The username is not available/its already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email)
                user.save()
                print("You are now registered and can login")
                return redirect('mylogin')
        else:
            print('Password do not match,please enter again')
            messages.error(request,"Password do not match,please enter again")
            return redirect("register")
    else:
        print("I am in GET request")
        return render(request,'menu/register.html')


def logoutmenu(request):
	print("In Logout")
	auth.logout(request)
	return redirect('mylogin')

  #if request.method == 'POST':
  #	 auth.logout(request)
#
 # 	 return redirect('mylogin')