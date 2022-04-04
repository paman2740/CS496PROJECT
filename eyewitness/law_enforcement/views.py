from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .models import Photo, Customer, Case
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, '../templates/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('gallery')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

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
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
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
    
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.all()

    context = {'photos': photos}
    return render(request, 'photos/gallery.html', context)



@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo}, )

@login_required(login_url='login')
def addLineup(request, pk):
    Cases=Case.objects.all()
    
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        photo_num=data['photo_num']
        post = Case.objects.get(id=data['case'])
        post.photo_1.add(photo)

    
    return render(request, 'photos/addLineup.html', 
             {'Cases': Cases},)


@login_required(login_url='login')
def witnessList(request):
    photos =Customer.objects.all()
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
