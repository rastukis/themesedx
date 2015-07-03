from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from admintheme.models import Instance, User
from admintheme.form import InstanceForm, UserForm


# Create your views here.
def staffdashboard(request):
    message = 'Hola'
    return render_to_response('login/login.html', {'message': message})

def admindashboard(request):
    instances_list = Instance.objects.all()
    paginator = Paginator(instances_list, 15)
    page = request.GET.get('page')
    try:
        instances = paginator.page(page)
    except PageNotAnInteger:
        instances = paginator.page(1)
    except EmptyPage:
        instances = paginator.page(paginator.num_pages)
    return render_to_response('instances/admin_instances.html', {"instances": instances},  context_instance=RequestContext(request))

def add_instance(request):
    if request.method == 'POST':
        form = InstanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = InstanceForm()
    return render_to_response('instances/add_instance.html', {'form': form}, context_instance=RequestContext(request))

def users(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 15)
    page = request.GET.get('page')
    try:
        users_l = paginator.page(page)
    except PageNotAnInteger:
        users_l = paginator.page(1)
    except EmptyPage:
        users_l = paginator.page(paginator.num_pages)
    return render_to_response('users/users_list.html', {"users": users_l},  context_instance=RequestContext(request))

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_db = User(is_staff=1)
            form = UserForm(request.POST, instance=user_db)
            form.save()
            return redirect('/dashboard')
    else:
        form = UserForm()
    return render_to_response('users/add_user.html', {'form': form}, context_instance=RequestContext(request))

def handler404(request):
    response = render_to_response('errors/404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response
