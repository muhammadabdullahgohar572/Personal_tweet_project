from django.shortcuts import render,redirect,get_object_or_404
from .models import Tweet
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from  django.contrib.auth import login,logout

# Create your views here.



def HomePage(request):
   getallData=Tweet.objects.all()
   return render(request,"tweets/ShowAllTweet.html",{"getallData":getallData})

@login_required
def Tweet_Create(request):
    if request.method == "POST":
        person_text = request.POST.get("Person_text")
        person_photo = request.FILES.get("Person_photo")  # Changed to FILES
        
        Data = Tweet(
            text=person_text,
            photo=person_photo,
            user=request.user
        )
        Data.save()
        
        return redirect("Home_Page")  
    
    return render(request, "tweets/Create_tweet.html")

@login_required
def DeleteTweet(request,emp_id):
    DeletedTweet=get_object_or_404(Tweet,pk=emp_id)
    DeletedTweet.delete()
    return  redirect("Home_Page") 

@login_required
def Tweet_Update(request,emp_id):
    UpdatedTweet=get_object_or_404(Tweet,pk=emp_id)
    return render(request,"tweets/Updated_Tweet.html",{"UpdatedTweet":UpdatedTweet})

@login_required
def Updated_Tweet(request, emp_id):
    tweet = get_object_or_404(Tweet, pk=emp_id)
    
    if request.method == "POST":
        # Get the form data
        tweet.text = request.POST.get("Person_text")
        
        # Handle image removal
        remove_image = request.POST.get("remove_image") == "true"
        if remove_image:
            tweet.photo.delete()  # Remove the current image
            tweet.photo = None
        
        # Handle new image upload (only if not removing image and new file provided)
        if 'Person_photo' in request.FILES and not remove_image:
            tweet.photo = request.FILES['Person_photo']
        
        tweet.save()
        return redirect("Home_Page")
    
    return redirect("updatedtweet", emp_id=emp_id)



def Register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Home_Page")
       
    else:
        form = UserCreationForm()
    
    return render(request, "auth/Register.html", {"form": form})
           
           
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("Home_Page")
    else:
        form = AuthenticationForm()
    
    return render(request, "auth/Login.html", {"form": form})                              



def logout_view(request):
     logout(request)
     return redirect("Home_Page")
                                   