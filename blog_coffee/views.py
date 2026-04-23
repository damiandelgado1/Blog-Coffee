from django.shortcuts import render

# Display Main Page of the Blog
def main_page(request):
    return render(request, "home/layout.html")

# Display Blog's by the Site
def blog_list(request):
    return render(request, "blog/blog_list.html")

# Display Main Page of the Blog
def blog_detail(request):
    return render(request, "blog/blog_detail.html")

# Display Main Page of the Blog
def form_page(request):
    return render(request, "home/form.html")