from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import BookGuest
from webapp.forms import BookGuestForm
# Create your views here.


def index_views(request):
    guests = BookGuest.objects.order_by('-create').filter(choice='Active')
    return render(request, "index.html", {'guests': guests})


def add_views(request):
    if request.method == "GET":
        form = BookGuestForm()
        return render(request, "add.html", {'form': form})
    elif request.method == "POST":
        form = BookGuestForm(data=request.POST)
        if form.is_valid():
            new_todo = BookGuest.objects.create(
                name=form.cleaned_data['name'],
                content=form.cleaned_data['content'],
                email=form.cleaned_data['email']
            )
            return redirect('index')
        else:
            return render(request, 'add.html', {'form': form})


def update_views(request, pk, **kwargs):
    guest = get_object_or_404(BookGuest, pk=pk)
    if request.method == 'GET':
        form = BookGuestForm(initial={'name': guest.name, 'content': guest.content, 'email': guest.email})
        return render(request, 'update.html', {'form': form})
    elif request.method == "POST":
        form = BookGuestForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data.get('name')
            guest.content = form.cleaned_data.get('content')
            guest.email = form.cleaned_data.get('email')
            guest.save()
            return redirect('index')
        else:
            return render(request, 'update.html', {'form': form})


def delete_views(request, pk):
    guest = get_object_or_404(BookGuest, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'guest': guest})
    elif request.method == 'POST':
        guest.delete()
        return redirect('index')
