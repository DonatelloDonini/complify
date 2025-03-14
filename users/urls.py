
from . import views
from django.contrib.auth import views as auth_view
from django.urls import path, include
#from .views import TodosListView

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path('basetables/', views.base_tables, name="base_tables"),
    path('files/', views.files, name="files"),
    path('certification/', views.certification, name="certification"),
    path('todos_dett/', views.todos_dett, name="todos_dett"),
    path('todos_list/', views.todos_list, name="todos_list"),
    path('standarditems_list/', views.standarditems_list, name="standarditems_list"),
    path('requirements_list/', views.requirements_list, name="requirements_list"),
    path('enterprises_dett/', views.enterprises_dett, name="enterprises_dett"),
    path('actions_dett/', views.actions_dett, name="actions_dett"),
    path('actions_list/', views.actions_list, name="actions_list"),
    path('about/', views.about, name="about"),    
    path('orgcharts_dett/', views.orgcharts_dett, name="orgcharts_dett"),
    path('orgchartsitems_dett/', views.orgchartsitems_dett, name="orgchartsitems_dett"),
    path('termsandconditions/', views.termsandconditions, name="termsandconditions"),
    path('enterprises_people_dett/', views.enterprises_people_dett, name="enterprises_people_dett"),
    path('enterprises_locations_dett/', views.enterprises_locations_dett, name="enterprises_locations_dett"),   
    path('assets_dett/', views.assets_dett, name="assets_dett"),   
    path('enterprises_enterprises_dett/', views.enterprises_enterprises_dett, name="enterprises_enterprises_dett"), 
    path('download/', views.download_file, name='download_file'),
    path('requests_dett/', views.requests_dett, name='requests_dett'),
    path('actionsitemsstandards_dett/', views.actionsitemsstandards_dett, name='actionsitemsstandards_dett'),
    path('actionsassets_dett/', views.actionsassets_dett, name='actionsassets_dett'),
    path('enterprisesstandardsitems_dett/', views.enterprisesstandardsitems_dett, name='enterprisesstandardsitems_dett'),
    path('enterprisestandards_dett/', views.enterprisestandards_dett, name='enterprisestandards_dett'),
    path('roles_dett/', views.roles_dett, name='roles_dett'),
    path('tofaenterprisesitemsstandards_dett/', views.tofaenterprisesitemsstandards_dett, name='tofaenterprisesitemsstandards_dett'),
    #path('todos-filter/', TodosListView.as_view(), name='todos-list-filter'),
]
