from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import LimitForm
from .models import Limit
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_validate=True, no_store=True)
@login_required 
def list_limits(request):
    limits = Limit.objects.all()
    context = {'limits': limits}
    return render(request, 'monitor/limit_list.html', context)

@login_required 
def create_limit(request):
    if request.method == 'POST':
        form = LimitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('limit_list')
    else:
        form = LimitForm()
    return render(request, 'monitor/limit_form.html', {'form': form})

@login_required 
def update_limit(request, limit_id):
    limit = get_object_or_404(Limit, pk=limit_id)
    if request.method == 'POST':
        form = LimitForm(request.POST, instance=limit)
        if form.is_valid():
            form.save()
            return redirect('limit_list')
    else:
        form = LimitForm(instance=limit)
    return render(request, 'monitor/limit_form.html', {'form': form})

@login_required 
def delete_limit(request, limit_id):
    limit = get_object_or_404(Limit, pk=limit_id)
    limit.delete()
    return redirect('limit_list')

