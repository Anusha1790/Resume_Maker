from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.input_form, name="input_form"),
    path('<int:id>/', views.check, name="check"),

]
