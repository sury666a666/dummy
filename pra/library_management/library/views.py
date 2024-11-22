from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member
from django.utils import timezone
from django.contrib import messages

def index(request):
    books = Book.objects.all().order_by('-date_added')
    members = Member.objects.all().order_by('-date_registered')
    return render(request, 'library/index.html', {'books': books, 'members': members})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        published_date = request.POST.get('published_date')
        available = 'available' in request.POST  # Check if checkbox is checked

        if not published_date:
            published_date = None
        
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            date_added=timezone.now(),
            published_date=published_date,
            available=available
        )
        return redirect('index')
    return render(request, 'library/add_book.html')

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.isbn = request.POST.get('isbn')
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('index')
    return render(request, 'library/edit_book.html', {'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('index')
    return render(request, 'library/delete_book.html', {'book': book})

def add_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        member_id = request.POST.get('member_id')
        Member.objects.create(name=name, member_id=member_id, date_registered=timezone.now())
        messages.success(request, 'Member added successfully!')
        return redirect('index')
    return render(request, 'library/add_member.html')

def search_books(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'library/index.html', {'books': books, 'members': Member.objects.all()})
