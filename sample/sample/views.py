from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404

def post_index(request):
    posts_list = [1,2,3,4,5]
    return render(request,'posts.html',{'posts': posts_list})
