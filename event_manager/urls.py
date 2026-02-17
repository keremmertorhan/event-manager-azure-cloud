from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from events.views import event_list, add_event, event_detail, delete_event, edit_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_list, name='home'),
    path('add/', add_event, name='add_event'),
    path('<int:pk>/', event_detail, name='event_detail'),
    path('<int:pk>/edit/', edit_event, name='edit_event'),
    path('<int:pk>/delete/', delete_event, name='delete_event'),
    
    # Kullanıcı İşlemleri (Register, Login, Logout)
    path('register/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)