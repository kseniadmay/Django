from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('women/', views.index),  # http://127.0.0.1:8000/ + women/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/ + about/
    path('cats/', views.categories),  # http://127.0.0.1:8000/ + cats/
    path('cats/<int:cat_id>/', views.categories, name='cats=id'),  # http://127.0.0.1:8000/ + cats/2
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # http://127.0.0.1:8000/ + cats/dhm68ud
    path('archive/<year4:year>/', views.archive, name='archive')  # http://127.0.0.1:8000/ + archive/1994
]
