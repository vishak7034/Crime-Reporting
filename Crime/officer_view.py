from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Crime.models import Criminals, PoliceReg, UserReg, Fir,Complaint, evidence


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'officer/officer_index.html'
    login_url = '/'
    

class view_fir(TemplateView):
    template_name = 'officer/view_fir.html'

    def get_context_data(self, **kwargs):
        context = super(view_fir, self).get_context_data(**kwargs)
        p = Fir.objects.filter(status='fir_registered')

        context['p'] = p

        return context
class approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        f = Fir.objects.get(pk=id)
        f.status='FIR Approved'
        f.save()
        return render(request, 'officer/officer_index.html', {'message': "approved"})
    
class reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        f = Fir.objects.get(pk=id)
        f.status='reject'
        f.save()
        return render(request, 'officer/officer_index.html', {'message': "rejected"})



class fir_approve_list(TemplateView):
    template_name = 'officer/fir_approved_list.html'

    def get_context_data(self, **kwargs):
        context = super(fir_approve_list, self).get_context_data(**kwargs)
        p = Fir.objects.filter(status='FIR Approved')

        context['m'] = p
        return context


class evidence_details_view(TemplateView):
    template_name = 'officer/evidence_details.html'
    def get_context_data(self, **kwargs):
        context = super(evidence_details_view, self).get_context_data(**kwargs)
        try:
            id=self.request.GET['id']
            m = evidence.objects.get(police_id=self.request.user.id,ledger_id=id)
            print("qqqqqqqqqqqq",m)
            context['m'] = m
            return context
        except:
            pass

