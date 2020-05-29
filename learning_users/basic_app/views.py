from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm,EmployeeForm,OrganizationForm,TeamForm,AgileTeamForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('You are logged in , Nice !')

def register(request):
    registered=False
    print("..................................................................")
    if request.method=='POST':
        print(request.method)
        user_form=  UserForm(data=request.POST)
        profile_form= UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            print(user+"user is valid................")
            profile=profile_form.save(commit=False)
            profile.user=user
            print(user+"profile.user.....................")
            if 'profile_pic' in request.FILES:
                profile.profile_pic= request.FILES['profile_pic']

            profile.save()
            print(profile+"profile details.................")
            registered=True
        else:
            print("Error details in user and profile............")
            print(user_form.errors , profile_form.errors)

    else:
        print("not post method(get method )............. ")
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basic_app/Registration.html',{
    'user_form':user_form,
    'profile_form':profile_form,
     'registered':registered
     }
     )

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('AACOUTN IS NOT ACTIVE!')

        else:
            print("some ont try to login failed")
            print('username :{} and password :{}'.format(username,password))
            return HttpResponse("invalid login details  suppiled")

    else:
        return render(request,'basic_app/login.html',{})


def org_base(request):
    return render(request,'org/org_base.html')

def orgname(request):
    if request.method == 'POST':
        orgName= OrganizationForm(data=request.POST)
        if orgName.is_valid:
            orgName.save()
    return render(request,'org/orgName.html',{'org_name':OrganizationForm})


def Team_dic(request):
    if request.method == 'POST':
        team= TeamForm(data=request.POST)
        if team.is_valid:
            team.save()
    return render(request,'org/team.html',{'team_me':TeamForm})


def agile(request):
    if request.method == 'POST':
        agile=AgileTeamForm(data = request.POST)
        if agile.is_valid:
            agile.save()
        else:
            print(agile.errors)
    else:
        print('NOT POST METHOD IN AGILE')
        agile = AgileTeamForm

    return render(request,'org/agile.html',{'agile':agile})


def emp(request):
    if request.method == 'POST':
        emp = EmployeeForm(data = request.POST)
        if emp.is_valid:
            emp.save()
        else:
            print(emp.errors)

    else:
        emp=EmployeeForm
    return render(request,'org/emp.html',{'emp':emp})
