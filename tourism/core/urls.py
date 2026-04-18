from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/<int:pk>/', views.destination_detail, name='destination_detail'),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # TRAVEL PLAN
    path('create-plan/', views.create_plan, name='create_plan'),
    path('plan/<int:pk>/', views.plan_summary, name='plan_summary'),
    path('my-plans/', views.my_plans, name='my_plans'),

    # REVIEW
    path('review/<int:pk>/', views.add_review, name='add_review'),
    path('top-destinations/', views.top_destinations, name='top_destinations'),
]