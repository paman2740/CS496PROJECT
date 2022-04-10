from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import WitnessSignUpForm, OfficerSignUpForm, LineUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.http import HttpResponseRedirect
from .models import Photo, Officer, Case, LineUp
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, '../templates/register.html')

class witness_register(CreateView):
    model = User
    form_class = WitnessSignUpForm
    template_name = '../templates/witness_register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('gallery')

class officer_register(CreateView):
    model = User
    form_class = OfficerSignUpForm
    template_name = '../templates/officer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('gallery')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            officer = authenticate(username=username, password=password)

            if officer is not None :
                login(request,officer)
                return redirect('gallery')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('gallery')


@login_required(login_url='login')
def gallery(request):
    photos = Photo.objects.all()
    #user = request.user
    #venues = LineUp.objects.filter(user=user)

    context = {'photos': photos}

    return render(request, 'photos/gallery.html', context)

@login_required(login_url='login')
def lineUp(request):
    
    lines = LineUp.objects.all()

    context = {'lines': lines}
    return render(request, 'photos/lineUp.html', context)

@login_required(login_url='login')
def addLineup(request, pk):
    Users=User.objects.all()
    Cases=Case.objects.all()
    ref = Photo.objects.get(id=pk)

    submitted = False
    if request.method == "POST":
        form = LineUpForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.photo = ref
            venue.save()
            #form.save()
            submitted = True
            return  redirect('gallery')   
    else:
        form = LineUpForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'photos/addLineup.html', 
             {'Cases': Cases,
             'Users': Users,
             'form':form, 
             'submitted':submitted})


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photos/photo.html', {'photo': photo}, )



@login_required(login_url='login')
def witnessList(request):
    photos =Witness.objects.all()
    return render(request, 'photos/witness_list.html', 
        {'photos': photos })

@login_required(login_url='login')
def addPhoto(request):

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        for image in images:
            photo = Photo.objects.create(
                description=data['description'],
                image=image,
                Height=data['height'],
                HairColor=data['haircolor'],
                HairType=data['hairtype'],
                EyeColor=data['eyecolor'],
                Glasses=data['glasses'],
                Scar=data['scar'],
            )

        return redirect('gallery')

    return render(request, 'photos/add.html')

@login_required(login_url='login')
def addCase(request):

    if request.method == 'POST':
        data = request.POST

        case = Case.objects.create(
                    name=data['name'],
                )

        return redirect('gallery')
    return render(request, 'photos/addCase.html')

def search_photo(request):
    if request.method == "POST":
        scars = request.POST['scars']
        glasses = request.POST['glasses']
        haircolor =request.POST['haircolor']
        hairtype =request.POST['hairtype']
        eyecolor =request.POST['eyecolor']
        venues = Photo.objects.filter(Scar__contains=scars).filter(Glasses__contains=glasses).filter(EyeColor__contains=eyecolor).filter(HairType__contains=hairtype).filter(HairColor__contains=haircolor)
    
        return render(request, 
        'photos/filter.html', 
        {
        'venues':venues})
    else:
        return render(request, 
        'photos/filter.html', 
        {})
def witness_view(request):
    user = request.user
    venues = LineUp.objects.filter(user=user)

    context = { 'venues': venues }

    return render(request, 'photos/witness_view.html', context)
