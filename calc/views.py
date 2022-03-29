from django.shortcuts import render, redirect
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from .forms import RecordForm, HistoryForm
from .models import Record, History

# Create your views here.

def home(request):
    return render(request, 'index.html')


def enter(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recordPG')
        else:
            print(form.errors)
    else:
        form = RecordForm()
    context = {
        'form' : form,
    }
    return render(request, 'content/wallet/form.html', context)


def enterdebt(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        entries = History.objects.filter(name=name)
        form = HistoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('recordPG')
        else:
            print(form.errors)
    else:
        form = HistoryForm()
    context = {
        'form' : form,
    }
    return render(request, 'content/wallet/form2.html', context)


def listdisplay(request):
    records = Record.objects.all()

    return render(request, 'content/wallet/articles.html', {'records':records})


def ceetdisplay(request, pk):
    record = Record.objects.get(id=pk)
    
    return render(request, 'content/wallet/item.html', {'record':record})
