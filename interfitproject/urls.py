from django.contrib import admin
from django.urls import path, include
import resumeapp.views
import positionapp.views

urlpatterns = [
    path('admin/', admin.site.urls),

    #resumeapp
    path('',resumeapp.views.resume_index, name='resume_index'),
    path('resume_input/',resumeapp.views.resume_input, name='resume_input'),
    path('resume_list/',resumeapp.views.resume_list, name='resume_list'),
    path('resume_list/<int:resumelist_id>/', resumeapp.views.resume_detail, name='resume_detail'),
    path('resume_input/resume_create/',resumeapp.views.resume_create, name="resume_create"),
    
    #positionapp
    path('position_input/',positionapp.views.position_input, name='position_input'),
    path('position_input/position_create/',positionapp.views.position_create, name='position_create'),

    #accountsapp
    path('accounts/' , include('accounts.urls')),
]
