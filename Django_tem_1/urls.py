"""Django_tem_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App1 import views
from django.contrib.auth import views as vs
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profupdt/', views.profupdt, name='profupdt'),
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', vs.LoginView.as_view(template_name='html/login.htm'), name='login'),
    path('logout/',vs.LogoutView.as_view(template_name="html/logout.htm"),name="lgo"),
    path('addimg/', views.addimg, name='addimg'),
    path('delimg/<int:m>', views.delimg, name='delimg'),
    path('showimg/<int:m>', views.showimg, name='showimg'),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('capedit/<int:m>', views.capedit, name="capedit"),
    path('showprofile/<int:m>', views.showprofile, name='showprofile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)