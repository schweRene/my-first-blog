from django.shortcuts import render

# Create youre views here

def post_list(request):
    return render(request, 'blog/post_list.html', {})
