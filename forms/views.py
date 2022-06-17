import email
from unicodedata import name
from django.shortcuts import render
from.forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            
            print(name, email, body)
            
            
    # unbound form contains no data assosciated with it
    form = ContactForm()
    return render(request, 'forms/form.html', {'form':form})

# def snippet_detail(request):
#     if request.method == 'POST':
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
            
     
#     form = SnippetForm()
#     return render(request, 'forms/form.html', {'form':form})