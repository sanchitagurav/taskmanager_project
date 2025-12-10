from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Temporary home view
def home(request):
    return HttpResponse("Welcome to Task Manager API!")

urlpatterns = [
    path('', home),             # / → home page
    path('admin/', admin.site.urls),  # /admin/ → admin site
    path('api/', include('api.urls')),  # /api/ → API app urls
]
