from django.urls import path

from Crime.user_views import IndexView, ViewCriminals, AddFeedback, SelectStation,View_complaint, \
    Complaint_reg,add_evidence_view,missing_view,View_Evidence,Evidence
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('',IndexView.as_view()),
    path('ViewCriminals',ViewCriminals.as_view()),
    path('AddFeedback',AddFeedback.as_view()),
    path('SelectStation',SelectStation.as_view()),
    path('FIR_reg',Complaint_reg.as_view()),
    path('ViewFIR',View_complaint.as_view()),
    path('add_evidence',add_evidence_view.as_view()),
    path('missing',missing_view.as_view()),
    path('View_Evidence',View_Evidence.as_view()),
    path('Evidence',Evidence.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),


]
def urls():
      return urlpatterns,'user','user'