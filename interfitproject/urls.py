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
    path('resume_search/',resumeapp.views.resume_search, name='resume_search'),
    path('resume_list/<int:resumelist_id>/', resumeapp.views.resume_detail, name='resume_detail'),
    path('resume_list/<int:resumelist_id>/delete/', resumeapp.views.resume_delete, name='resume_delete'),
    path('resume_list/<int:resumelist_id>/update/', resumeapp.views.resume_update, name='resume_update'),
    path('resume_list/<int:resumelist_id>/edit/', resumeapp.views.resume_edit, name='resume_edit'),
    path('resume_input/resume_create/',resumeapp.views.resume_create, name="resume_create"),
    
    #positionapp
    path('position_input/',positionapp.views.position_input, name='position_input'),
    path('position_list/',positionapp.views.position_list, name='position_list'),
    path('position_search/',positionapp.views.position_search, name='position_search'),
    path('position_list/<int:recruitlist_id>/',positionapp.views.position_detail, name='position_detail'),
    path('position_list/<int:recruitlist_id>/delete/', positionapp.views.position_delete, name='position_delete'),
    path('position_list/<int:recruitlist_id>/update/', positionapp.views.position_update, name='position_update'),
    path('position_list/<int:recruitlist_id>/edit/', positionapp.views.position_edit, name='position_edit'),
    path('position_input/position_create/',positionapp.views.position_create, name='position_create'),

    #accountsapp
    path('accounts/' , include('accounts.urls')),
]
