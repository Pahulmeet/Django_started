from django.views import generic
from .models import Blood_request
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm, RequestForm, HospitalForm, DonorForm, Login
from django.contrib.auth import authenticate, login


class IndexView(generic.ListView):
    template_name = 'blood/fmain.html'
    context_object_name = 'blood_request'

    def get_queryset(self):
        return Blood_request.objects.all()

#class DetailView(generic.DeleteView):
#    model = Blood_request
#    template_name = 'blood/request.html'


class UserFormView(View):
    form_class = UserForm
    template_name = 'blood/signd.html'
    #blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            # cleaned (normalized i.e. unifies , formatted)data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # return user credentials if correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blood:index')
        return render(request, self.template_name, {'form': form})




#   REQUEST BLOOD

def BloodRequest(request):
    print('!!!!!!!!!!!!!!!!!!!!!!')
    ch=1
    if (ch==2):
        print('nothing is fine')
    #if not request.user.is_authenticated():
    #    print('$$$$$$$$$$$$$$$$$$$$$$$$4')
    #    return render(request, 'blood/fmain.html')
    else:
        print('#############################')
        form = RequestForm(request.POST or None)

        if form.is_valid():
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&7')
            obj = Blood_request()
            obj.name = form.cleaned_data['name']
            obj.city = form.cleaned_data['city']
            obj.pin_code = form.cleaned_data['pin_code']
            obj.contact1 = form.cleaned_data['contact1']
            obj.contact2 = form.cleaned_data['contact2']
            obj.date = form.cleaned_data['date']
            obj.blood_group = form.cleaned_data['blood_group']
            obj.save()
            ch=0
            return redirect('blood:index')

        if ch==1:
            context = {"form" : form,}
            print('here!')
            return render(request, 'blood/request.html',context)


# Hospital Sign Up
def HospitalRegister(request):
    print('inside sign up hospital')
    ch = 1
    if (ch == 2):
        print('nothing is fine')
    #if not request.user.is_authenticated():
    #    print('$$$$$$$$$$$$$$$$$$$$$$$$4')
    #    return render(request, 'blood/fmain.html')
    else:
        print('\n Check1')
        form = HospitalForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            print('\nCheck2')
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            city = form.cleaned_data['city']
            email = form.cleaned_data['email']
            contact1 = form.cleaned_data['contact1']
            contact2 = form.cleaned_data['contact2']
            pin_code = form.cleaned_data['pin_code']
            state = form.cleaned_data['state']
            user.set_password(password)
            user.save()
            print('\ndeciding point')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    print('---------NOT IN HERE------------')
                    login(request, user)
                    #requests = Blood_request.objects.filter(user=request.user)
                    return redirect('blood:P_hospital')
        context = {
            "form": form,
        }
        return render(request, 'blood/signh.html', context)






# Donor Sign Up
def DonorRegister(request):
    print('inside sign up donor')
    ch = 1
    if (ch == 2):
        print('nothing is fine')
    #if not request.user.is_authenticated():
    #    print('$$$$$$$$$$$$$$$$$$$$$$$$4')
    #    return render(request, 'blood/fmain.html')
    else:
        print('\n Check1')
        form = DonorForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            print('\nCheck2')
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            city = form.cleaned_data['city']
            email = form.cleaned_data['email']
            contact1 = form.cleaned_data['contact1']
            contact2 = form.cleaned_data['contact2']
            pin_code = form.cleaned_data['pin_code']
            state = form.cleaned_data['state']
            blood_group = form.cleaned_data['blood_group']
            user.set_password(password)
            user.save()
            print('\ndeciding point')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    print('---------NOT IN HERE------------')
                    login(request, user)
                    #requests = Blood_request.objects.filter(user=request.user)
                    return redirect('blood:P_donor')
        context = {
            "form": form,
        }
        return render(request, 'blood/signd.html', context)



#Hospital profile page

def ProfileHospital(request):
    return render(request, 'blood/profile_hospital.html')

#Donor profile page

def ProfileDonor(request):
    return render(request, 'blood/profile_donor.html')

#LOGIN page

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'blood/profile_hospital.html')
            else:
                return render(request, 'blood/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'blood/login.html', {'error_message': 'Invalid login'})
    return render(request, 'blood/login.html')




#LOGOUT
def logout_user(request):
    logout(request)
    return redirect('blood:index')


'''
def Login(request):
    form = UserForm(request.GET or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'music:P_donor')
    context = {
        "form": form,
    }
    return render(request, 'blood/login.html', context)


    form = (request.POST or None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            print('---------NOT IN HERE------------')
            login(request, user)
            # requests = Blood_request.objects.filter(user=request.user)
            return redirect('blood:P_donor')
    else
        return redirect('blood:login')

'''
'''
            user = super(HospitalForm())
            user.username = form.cleaned_data('username')
            user.city = form.cleaned_data('city')
            user.pin_code = form.cleaned_data('pin_code')
            user.contact1 = form.cleaned_data('contact1')
            user.contact2 = form.cleaned_data('contcat2')
            user.email = form.cleaned_data('email')
            user.state = form.cleaned_data('state')

            if commit:
                user.save()
                return user

            return redirect('blood:index')
        else:
            form = UserCreationForm()

        args = {'form' : form,}
        print('now almost there')
        return render(request, 'blood/signh.html',args)

'''

'''
class HospitalFormView(View):
    form_class = UserForm
    template_name = 'blood/signh.html'
    # blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

        # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

                    # cleaned (normalized i.e. unifies , formatted)data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

                    # return user credentials if correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blood:index')
        return render(request, self.template_name, {'form': form})

        
        form = PostForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
'''



'''
class SignupDonor(CreateView):
    model = SignupDonor
    fields = ['username','email','password','repassword','city','pin_code','state','contact1','contact2','blood_group']
    template_name = 'blood/signd.html'

    
class BloodRequest(CreateView):
    model = Blood_request
    fields = ['name','city','pin_code','contact1','contact2','date','blood_group']
    template_name = 'blood/request.html'

    def form_valid(self, request, form):
        form.instance.name = self.request.name
        form.instance.city = self.request.city
        form.instance.pin_code = self.request.pin_code
        form.instance.contact1 = self.request.contact1
        form.instance.contact2 = self.request.contact2
        form.instance.date = self.request.date
        form.instance.blood_group = self.request.blood_group
        form.save()
        return super(BloodRequest, self).form_valid(form)
        
        
        
        
        
        
            if request.method == 'POST':
        print('****************')
        form = RequestForm(request.POST)

        
        if form.is_valid():
            print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
            blood_request = form.save(commit=False)
            blood_request.name = request.name
            blood_request.city = request.city
            blood_request.pin_code = request.pin_code
            blood_request.contact1 = request.contact1
            blood_request.contact1 = request.contact2
            blood_request.date = request.date
            blood_request.blood_group = request.blood_group
            blood_request.save()

            return render(request,'blood/fmain.html')
    '''