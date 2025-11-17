from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Registratoin, Room, Message
import logging
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Registratoin, Room, Message
import logging
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Configure logging
logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        user_name = request.POST['UserName']
        email = request.POST['Email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        if Registratoin.objects.filter(user_name=user_name).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        
        if Registratoin.objects.filter(Email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')
        
        s = Registratoin.objects.create(user_name=user_name, Email=email, Password=password)
        s.save()
        messages.success(request, "Registration successful")
        return redirect('login')
     
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        full_name = request.POST['username']
        password = request.POST['password']
        all_data = Registratoin.objects.filter(user_name=full_name, Password=password)
        
        if all_data.exists():
            request.session['username'] = full_name  # Store the username in session
            messages.success(request, "Login successful")
            return redirect('room')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
            
    return render(request, 'login.html')



def room(request):
    if 'username' not in request.session:
        return redirect('login')
    
    username = request.session['username']
    user = Registratoin.objects.get(user_name=username)
    messages = Message.objects.filter(room__name='main').order_by('timestamp')
    users = Registratoin.objects.all()
    
    return render(request, 'room.html', {
        'username': username,
        'messages': messages,
        'users': users
    })

@csrf_exempt
@require_POST
def post_message(request):
    try:
        username = request.POST['username']
        content = request.POST.get('message', '')
        image = request.FILES.get('image','')  # Handle image file
        user = Registratoin.objects.get(user_name=username)

        # Ensure the room exists
        room, created = Room.objects.get_or_create(name='main')

        # Save the message
        message = Message.objects.create(user=user, content=content, room=room, image=image)

        # Print the image URL to the terminal
        if message.image:
            print(f"Image URL: {message.image.url}")
        else:
            print("No image uploaded.")

        return JsonResponse({
            'status': 'Message sent',
            'message': message.content,
            'image_url': message.image.url if message.image else None,
        })
    except Exception as e:
        logger.error(f"Error posting message: {e}")
        return JsonResponse({'status': 'Failed to send message', 'error': str(e)})



