from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('home')  # या उस पेज पर जहाँ आप रीडायरेक्ट करना चाहते हैं
        
    return render(request, 'index.html')