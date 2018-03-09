from django.shortcuts import render , get_object_or_404
from . forms import UserForm,UserProfileInfoForm,MessageForm
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.views.generic import ListView,CreateView,TemplateView,DetailView
from messageApp.models import UserProfileInfo,Message
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def register(request):

    if request.method == 'POST':

        userform = UserForm(data = request.POST)
        userprofileform = UserProfileInfoForm(request.POST,request.FILES)

        if(userform.is_valid() and userprofileform.is_valid()):

            # Delaing with userfrom
            user_created = userform.save()

            # Here delaing with other info about user
            userprofileinfo = userprofileform.save(commit=False)
            userprofileinfo.user = user_created

            if (request.FILES.get('profile_pic',False)):
                userprofileinfo.profile_pic = request.FILES['profile_pic']

            userprofileinfo.save()

            print(userform.cleaned_data)
            print(userprofileform.cleaned_data)

            return HttpResponseRedirect(reverse('index'));

        else:

            print(userform.errors)
            print(userprofileform.errors)
            return render(request,'messageApp/register.html',{'userform':userform,'userprofileform':userprofileform})

    userform = UserForm()
    userprofileform = UserProfileInfoForm();

    return render(request,'messageApp/register.html',{'userform':userform,'userprofileform':userprofileform})


class UserList(LoginRequiredMixin,ListView):
    login_url = 'login/'
    model = UserProfileInfo


class CreateMessage(LoginRequiredMixin,CreateView):
    login_url = 'login/'
    model = Message
    form_class = MessageForm

    def form_valid(self, form):
        form.instance.sent_by = self.request.user
        return super().form_valid(form)

class MessageDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login/'
    model = Message
    

class Index(ListView):
    template_name = 'index.html'
    context_object_name = 'message_list'
    login_url = 'login/'

    def get_queryset(self):
        try:
            queryset = Message.objects.filter(sent_to = self.request.user)
        except:
            queryset = []
        return queryset

class SentItems(LoginRequiredMixin,ListView):
    template_name = 'messageApp/sent_items.html';
    context_object_name = 'message_list'
    login_url = 'login/'

    def get_queryset(self):
        try:
            queryset = Message.objects.filter(sent_by = self.request.user)
        except:
            queryset = []
        return queryset

def listMessages(request,pk):
    friend = get_object_or_404(User,pk=pk)
    # print(request.user.username)
    # print(friend.username)
    try:
        messages = Message.objects.filter(sent_by=friend,sent_to=request.user)
        # messages = list(messages)
    except:
        messages = []

    # print(messages)
    return render(request,'messageApp/messageDetail.html',{'messages':messages})
