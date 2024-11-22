from django.shortcuts import render, redirect, get_object_or_404
from .models import Friend
from .forms import FriendForm

def friend_list(request):
    friends = Friend.objects.all()
    return render(request, 'friends/friend_list.html', {'friends': friends})

def friend_create(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('friend_list')
    else:
        form = FriendForm()
    return render(request, 'friends/friend_form.html', {'form': form})

def friend_update(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == 'POST':
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            form.save()
            return redirect('friend_list')
    else:
        form = FriendForm(instance=friend)
    return render(request, 'friends/friend_form.html', {'form': form})

def friend_delete(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == 'POST':
        friend.delete()
        return redirect('friend_list')
    return render(request, 'friends/friend_confirm_delete.html', {'friend': friend})
