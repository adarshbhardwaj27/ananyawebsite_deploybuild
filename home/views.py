from django.shortcuts import render
from django.http import HttpResponse
from home.models import Video
from home.models import Message
# Create your views here.
def home(request):
    return render(request,'index.html')
def videos(request):
    videos_list = Video.objects.all().order_by('-pub_date')
    print(videos_list)
    params = {'videos_list':videos_list}
    return render(request,'videos.html',params)
def search(request):
    query = request.GET['query']
    videos_list_of_query = Video.objects.filter(video_name__icontains = query)
    print(videos_list_of_query)
    params = {'videos_list':videos_list_of_query}
    return render(request,'search.html',params)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')
        contact = Message(name=name,email=email,phone=phone,desc=message)
        contact.save()
        print(name,email,phone,message)
    return render(request,'contact.html') 
def about(request):
    return render(request,'about.html')