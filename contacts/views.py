import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

@login_required
def dashboard(request):
    total_contacts = Contact.objects.filter(owner=request.user).count()
    recent_contacts = Contact.objects.filter(owner=request.user).order_by('-created_at')[:5]
    return render(request, 'contacts/dashboard.html', {
        'total': total_contacts,
        'recent': recent_contacts
    })

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(owner=request.user)
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

@login_required
def contact_add(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contacts.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'Category'])
    
    contacts = Contact.objects.filter(owner=request.user)
    for c in contacts:
        writer.writerow([c.first_name, c.last_name, c.email, c.phone, c.category])
    
    return response

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form, 'edit_mode': True})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk, owner=request.user)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})