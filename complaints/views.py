from django.shortcuts import render, redirect, get_object_or_404
from .models import Complaint
from .forms import ComplaintForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count

@login_required
def dashboard(request):
    total = Complaint.objects.filter(user=request.user).count()
    pending = Complaint.objects.filter(user=request.user, status='Pending').count()
    in_progress = Complaint.objects.filter(user=request.user, status='In Progress').count()
    resolved = Complaint.objects.filter(user=request.user, status='Resolved').count()

    context = {
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
        'username': request.user.username,
    }
    return render(request, 'complaints/dashboard.html', context)

# List all complaints for current user

@login_required
def complaint_list(request):
    complaints = Complaint.objects.filter(user=request.user)

    category = request.GET.get('category')
    status = request.GET.get('status')
    query = request.GET.get('q')

    if category:
        complaints = complaints.filter(category=category)
    if status:
        complaints = complaints.filter(status=status)
    if query:
        complaints = complaints.filter(title__icontains=query)

    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

# Add new complaint
@login_required
def complaint_create(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_form.html', {'form': form})

# Update existing complaint
@login_required
def complaint_update(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    form = ComplaintForm(request.POST or None, instance=complaint)
    if form.is_valid():
        form.save()
        return redirect('complaint_list')
    return render(request, 'complaints/complaint_form.html', {'form': form})

# Delete complaint
@login_required
def complaint_delete(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk, user=request.user)
    if request.method == 'POST':
        complaint.delete()
        return redirect('complaint_list')
    return render(request, 'complaints/complaint_confirm_delete.html', {'complaint': complaint})

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('complaint_list')
    else:
        form = UserCreationForm()
    return render(request, 'complaints/signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirects to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})