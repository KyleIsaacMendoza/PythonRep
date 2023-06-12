
from django.urls import path # import when creating new url

from . import views # import when creating new url

urlpatterns = [ # urlpattern not urlspatterns
    path("", views.index, name="index")
]