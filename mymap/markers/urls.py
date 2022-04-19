from django.urls import path
from markers import views
app_name = "markers"

urlpatterns = [
        path('map/',view=views.index, name='map'),
        ]
