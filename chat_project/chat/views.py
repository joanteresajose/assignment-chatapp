from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the logged-in user
    return render(request, 'chat/chat.html', {'users': users})

def chat_messages(request, user_id):
    other_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        sender=request.user, recipient=other_user
    ) | Message.objects.filter(
        sender=other_user, recipient=request.user
    ).order_by('timestamp')
    return render(request, 'chat/messages.html', {'messages': messages, 'other_user': other_user})

from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat_view')  # Redirect to chat page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
