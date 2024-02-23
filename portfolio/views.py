from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
import json
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import QueryDict
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from portfolio.models import Portfolio
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import PortfolioForm, FieldOfficeForm
from .models import Portfolio, FieldOffice

@login_required(login_url='login')
def portfolios(request):
    portfolios = Portfolio.objects.all().order_by('id')
    context = {'portfolios': portfolios}
    return render(request, 'portfolios.html', context)


@login_required(login_url='login')
def portfolios_list(request):
    portfolios = Portfolio.objects.all().order_by('id')
    context = {'portfolios': portfolios}
    return render(request, 'partial/portfolios_list.html', context)

def edit_portfolio(request, id):
    portfolio = get_object_or_404(Portfolio, id=id)
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            isinstance =form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "PortfolioListChanged": None,
                        "showMessage": f"{isinstance.title} updated."
                    })
                }
            )
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'partial/portfolio_form.html', {
        'form': form,
        'portfolio': portfolio,
    })

def add_porfolio(request):
    
    form = PortfolioForm()
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            
            instance = form.save()
            
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "PortfolioListChanged": None,
                         "showMessage": f"{instance.title} updated."

                        
                    })
                }
            )
    else:
        form = PortfolioForm()
    return render(request, 'partial/portfolio_form.html', {
        'form': form,
    })

def delete_portfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    portfolio.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "PortfolioListChanged": None,
                "showMessage": f"{portfolio.title} deleted."
            })
        })

def portfolio_filter(request):
    query = request.GET.get('search', '')
    
    
    
    if query:
        qs1 = Portfolio.objects.filter(title__icontains=query)
        qs2 = Portfolio.objects.distinct().filter(type__name__icontains=query)
        qs3 = Portfolio.objects.distinct().filter(category__name__icontains=query)
        
        portfolios = qs1.union(qs2, qs3).order_by('id')
       
        
    else:
        portfolios = Portfolio.objects.all()

    context = {'portfolios': portfolios}
    return render(request, 'partial/portfolios_list.html', context)

def categories(request):
    form = PortfolioForm(request.GET)
    return HttpResponse(form['category'])

def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio.html', context)

def pregion(request, id):
    portfolio = get_object_or_404(Portfolio, pk=id)
    if request.method == "POST":
        form = FieldOfficeForm(request.POST or none)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.portfolio = Portfolio.objects.get(pk=id)
            instance.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FieldOfficeListChanged": None,
                        "showMessage": f"{instance.woreda} added."
                    })
                })
    
    form = FieldOfficeForm()
    context = {'form': form}
    
    return render(request, 'partial/portfolio_area_form.html', context)


def pzones(request):
    form = FieldOfficeForm(request.GET)
    return HttpResponse(form['zone'])


   

def pworedas(request):
    form = FieldOfficeForm(request.GET)
    return HttpResponse(form['woreda'])

def fieldoffices(request, id):
    return render(request, 'partial/portfolio_fieldoffice.html', {
        'fieldoffices': FieldOffice.objects.filter(portfolio_id=id),
    })

def portfolio_profile(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {'portfolio': portfolio}
    return render(request, 'partial/portfolio_profile.html', context)

def fieldoffice_edit(request, pk):
    fieldoffice = get_object_or_404(FieldOffice, pk=pk)
    if request.method == "POST":
        form = FieldOfficeForm(request.POST, instance=fieldoffice)
        if form.is_valid():
            instance = form.save()
            
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "FieldOfficeListChanged": None,
                        "showMessage": f"{instance.woreda} added."
                    })
                })
    
    form = FieldOfficeForm(instance=fieldoffice)
    context = {'form': form, 'fieldoffice':fieldoffice}
    
    return render(request, 'partial/portfolio_area_form.html', context)

def remove_fieldoffice(request, pk):
    fieldoffice = get_object_or_404(FieldOffice, pk=pk)
    fieldoffice.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "FieldOfficeListChanged": None,
                "showMessage": f"{fieldoffice.woreda} deleted."
            })
        })