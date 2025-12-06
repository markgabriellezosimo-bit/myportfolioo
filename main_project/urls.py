from django.contrib import admin
from django.urls import path
from my_app.views import portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio, name='portfolio'),
]

