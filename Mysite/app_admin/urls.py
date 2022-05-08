from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('collection/', views.CollectionView.as_view(), name='collection'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('racingboots/', views.RacingBootsView.as_view(), name='racingboots'),
    path('shoes/', views.ShoesView.as_view(), name='shoes'),
]
