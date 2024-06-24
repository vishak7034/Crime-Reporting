
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Crime.models import Criminals, Feedback, UserReg, PoliceReg, Complaint, add_evidence, missing


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'user/user_index.html'
    login_url = '/'

class ViewCriminals(LoginRequiredMixin,TemplateView):
    template_name = 'user/view_criminals.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewCriminals,self).get_context_data(**kwargs)
        cri = Criminals.objects.all()
        context['cri'] = cri
        return context

class AddFeedback(LoginRequiredMixin,TemplateView):
    template_name = 'user/feedback.html'
    login_url = '/'

    def post(self, request, *args, **kwargs):
        f = request.POST['feed']

        ps = UserReg.objects.get(login_id=self.request.user.id)

        s = Feedback()
        s.feedback = f
        s.user = ps
        s.save()

        messages = "Added Successfully"
        return render(request,'user/feedback.html',{'message':messages})

class SelectStation(LoginRequiredMixin,TemplateView):
    template_name = 'user/select_sation.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SelectStation, self).get_context_data(**kwargs)
        staff = PoliceReg.objects.filter(login__last_name='1', login__is_staff='0')
        context['staff'] = staff
        return context

class Complaint_reg(LoginRequiredMixin,TemplateView):
    template_name = 'user/complaint.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(Complaint_reg, self).get_context_data(**kwargs)
        st = self.request.GET['st']
        ps = UserReg.objects.get(login_id=self.request.user.id)

        context['st'] = st
        context['ps'] = ps
        return context

    def post(self, request, *args, **kwargs):
        st = request.POST['st']
        timee = request.POST['timee']
        date = request.POST['date']
        complaint = request.POST['complaint']
        location=request.POST['location']

        ps = UserReg.objects.get(login_id=self.request.user.id)
        pl = PoliceReg.objects.get(pk=st)

        com =Complaint()
        com.police = pl
        com.user = ps
        com.complaint = complaint
        com.location=location
        com.timee = timee
        com.c_date = date
        com.status = 'pending'
        com.status1='not_register'
        com.save()

        messages = "Registered Successfully"
        return render(request,'user/user_index.html',{'message':messages})


class View_complaint(LoginRequiredMixin,TemplateView):
    template_name = 'user/view_fir.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(View_complaint, self).get_context_data(**kwargs)
        m = Complaint.objects.filter(user__login=self.request.user.id)

        context['m'] = m
        return context
    
    
class add_evidence_view(LoginRequiredMixin,TemplateView):
    template_name = 'user/add_evidence.html'
    login_url = '/'
        
  
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
   

        id = self.request.GET['id']
        trip = Complaint.objects.get(id=id)
       
        context['veh']= trip
  
        return context
  
    def post(self, request, *args, **kwargs):
        id2 = request.POST['id2']
        id = request.POST['id']
        id3 = request.POST['id3']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        video = request.FILES['video']
        vid = FileSystemStorage()
        vids = vid.save(video.name, video)
        desc=request.POST['desc']

        com =add_evidence()
        com.image = filesss
        com.video = vids
        com.desc=desc
        com.complaint_id=id
        com.user_id=id2
        com.station_id=id3
        com.save()

        messages = "Evidence Added Successfully"
        return render(request,'user/user_index.html',{'message':messages})
    

class missing_view(LoginRequiredMixin,TemplateView):
    template_name = 'user/missing_complaint.html'
    login_url = '/'
        
    def get_context_data(self, **kwargs):
        context = super(missing_view, self).get_context_data(**kwargs)
        staff = PoliceReg.objects.filter(login__last_name='1', login__is_staff='0')
        context['staff'] = staff
        return context
  
    def post(self, request, *args, **kwargs):
        user= UserReg.objects.get(login_id=self.request.user.id)
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)
        date=request.POST['date']
        desc=request.POST['desc']
        station_name = request.POST['station_name']

        com =missing()
        com.image = filesss
        com.desc=desc
        com.date=date
        com.station_name=station_name
        com.user_id=user.id
        com.station_id=station_name
        com.save()

        messages = "Complaint Added Successfully"
        return render(request,'user/user_index.html',{'message':messages})


class View_Evidence(LoginRequiredMixin, TemplateView):
    template_name = 'user/view_evidence.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(View_Evidence, self).get_context_data(**kwargs)
        m = Complaint.objects.filter(user__login=self.request.user.id)

        context['m'] = m
        return context

class Evidence(LoginRequiredMixin, TemplateView):
    template_name = 'user/evidence.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(Evidence, self).get_context_data(**kwargs)
        m = add_evidence.objects.filter(complaint_id=id)

        context['m'] = m
        return context