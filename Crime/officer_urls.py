from django.urls import path

from django.contrib.auth import views as auth_views

from Crime.officer_view import IndexView,view_fir,approve,reject,fir_approve_list,evidence_details_view


urlpatterns = [

    path('',IndexView.as_view()),
    path('view_fir',view_fir.as_view()),
    path('approve',approve.as_view()),
    path('reject',reject.as_view()),
    path('fir_approve_list',fir_approve_list.as_view()),
    path('evidence_details_view',evidence_details_view.as_view()),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),
]
def urls():
      return urlpatterns,'police','police'