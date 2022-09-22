
from django.contrib import admin
from django.urls import path, include

app_name = 'quiz'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('', include('quiz.urls', namespace='quiz')),
]
