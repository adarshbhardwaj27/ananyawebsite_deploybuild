from django.shortcuts import render
from django.http import HttpResponse
from .models import Videos
# Create your views here.
def home(request):
    return render(request,'index.html')
def videos(request):
    videos_list = Videos.objects.all().order_by('-pub_date')
    print(videos_list)
    params = {'videos_list':videos_list}
    return render(request,'videos.html',params)
def search(request):
    query = request.GET['query']
    videos_list_of_query = Videos.objects.filter(video_name__icontains = query)
    print(videos_list_of_query)
    params = {'videos_list':videos_list_of_query}
    return render(request,'search.html',params)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        message = request.POST.get('message','')
    return render(request,'contact.html') 