from django.shortcuts import render,redirect

from   .models import Tweet

# Create your views here.


def HomePage(request):
    return render(request,"Navbar/navbar.html")

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