from.import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path('', views.home, name='home'),

    path('register/', views.register, name="signup_worker"),
    path('register_owner/', views.register_owner, name="signup"),
    path('accounts/profile/', views.account_settings, name="account_settings"),
    path("single_booked/<int:id>", views.booked_single, name="single_booked"),
    path("single_worker_booked/<int:id>", views.worker_single, name="single_worker_booked"),
    path("worker_action/", views.worker_action, name="worker_action"),
    path("accept_worked/", views.accept_work, name="accept_worked"),
    path("single_worker_booked/worker_profile/<int:id>", views.worker_profile, name="worker_profile"),
    path("worker_profile/<int:id>", views.my_profile, name="my_profile"),
    path("find_job",views.search,name="search_result"),
    path('post_jobs/', views.job_post, name='post_jobs'),
    path('your_booked/', views.get_work, name="booked"),
    path('owner', views.owner, name="owner"),
    path('<str:room>/', views.room, name='room'),
    path('room/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),



    ]