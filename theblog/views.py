from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForms
from django.urls import reverse_lazy
#Create your views here.
#def home(request):
#return render(request,'home.html',{})
class HomeView(ListView):
    model=Post
    template_name = 'home.html'
    #ordering = ['-id']
    ordering = ['-post_date']
   
class ArticleDetailsView(DetailView):
    model = Post
    template_name = 'articleview.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'addpost.html'
   # fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForms
    template_name = 'updatepost.html'
   # fields =['title','title_tag','body']
        
class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('')