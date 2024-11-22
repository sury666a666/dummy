# inventory/views.py

from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    return render(request, 'inventory/home.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})

def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/update_item.html', {'form': form, 'item_id': item_id})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'inventory/delete_item.html', {'item': item})
