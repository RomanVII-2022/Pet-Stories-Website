from django.shortcuts import render, redirect
from datetime import datetime 
from .models import Story, Category, Contact
from django.core.paginator import Paginator
from .forms import AddStoryForm, AddCategoryForm, AddStoryAdminForm
from django.contrib import messages
from django.http import HttpResponse
import csv

# Create your views here.
def home(request):
    categories = Category.objects.all().order_by('name')
    now = datetime.now()
    current_year = now.year
    p = Paginator(Story.objects.all().order_by('title'), 2)
    page = request.GET.get('page')
    stories = p.get_page(page)
    return render(request, 'home.html', {'current_year':current_year, 'stories':stories, 'categories':categories})


def storydetailview(request, story_id):
    story = Story.objects.get(pk=story_id)
    return render(request, 'storydetail.html', {'story':story})


def addstoryview(request):
    if request.method == "POST":
        if request.user.is_superuser:
            form = AddStoryAdminForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "You have added a story successfully")
                return redirect('home')
        else:
            form = AddStoryForm(request.POST, request.FILES)
            if form.is_valid():
                story = form.save(commit=False)
                story.author = request.user
                story.save()
                messages.success(request, "You have added a story successfully")
                return redirect('home')
    else:
        if request.user.is_superuser:
            form = AddStoryAdminForm()
        else:
            form = AddStoryForm()


    return render(request, 'addstory.html', {'form':form})


def editstoryview(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.user.is_superuser:
        form = AddStoryAdminForm(request.POST or None, request.FILES or None, instance=story)
    else:
        form = AddStoryForm(request.POST or None, request.FILES or None, instance=story)
    
    if form.is_valid():
        form.save()
        messages.success(request, "You have updated the story successfully")
        return redirect('home')
    return render(request, 'editstory.html', {'form':form, 'story':story})


def deletestoryview(request, story_id):
    story = Story.objects.get(pk=story_id)
    if request.method == "POST":
        story.delete()
        messages.success(request, "You have deleted the story successfully")
        return redirect('home')

    return render(request, 'deletestory.html', {'story':story})


def addcategoryview(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category was added successfully")
            return redirect('home')
    else:
        form = AddCategoryForm()
        
    return render(request, 'addcategory.html', {'form':form})


def categoryview(request, category):
    category = Category.objects.get(name=category)
    stories = Story.objects.filter(category=category)
    return render(request, 'category.html', {'category':category, 'stories':stories})


def searchedstoryview(request):
    if request.method == "POST":
        searched = request.POST['searched']
        stories = Story.objects.filter(body__contains=searched)
    return render(request, 'searchstory.html', {'stories':stories})


def contactview(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']
        save_data = Contact(first_name=first_name, last_name=last_name, email=email, message=message)
        save_data.save()
        messages.success(request, "Your message was sent successfully")
        return redirect('contact')

    return render(request, 'contact.html')


def messagescsvview(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=messages.csv'

    messages = Contact.objects.all().order_by('first_name')
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Message'])

    for message in messages:
        writer.writerow([message.first_name, message.last_name, message.email, message.message])

    return response