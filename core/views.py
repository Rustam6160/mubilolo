from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

def home(request):
    query = request.GET.get('q')
    if query:
        gifts = Gift.objects.filter(title__icontains=query)
    else:
        gifts = Gift.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'gifts': gifts, 'query': query})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Gift
from .forms import GiftForm
from django.contrib.auth.decorators import login_required

def home(request):
    gifts = Gift.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'gifts': gifts})

@login_required
def add_gift(request):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GiftForm()
    return render(request, 'add_gift.html', {'form': form})

@login_required
def edit_gift(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    form = GiftForm(request.POST or None, instance=gift)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'edit_gift.html', {'form': form})

@login_required
def delete_gift(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    if request.method == 'POST':
        gift.delete()
        return redirect('home')
    return render(request, 'delete_gift.html', {'gift': gift})
