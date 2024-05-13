from django.urls import path
from . import views, continent_views
urlpatterns = [
    path('ajout/<int:id>/', views.ajout),
    path('traitement/<int:id>/', views.traitement),
    path('index/', views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
    path("delete/<int:id>/", views.delete),

    path('ajoutcontinent/', continent_views.ajout),
    path('traitementcontinent/', continent_views.traitement),
    path('', continent_views.index),
    path("affichecontinent/<int:id>/", continent_views.affiche),
    path("updatecontinent/<int:id>/", continent_views.update),
    path("updatetraitementcontinent/<int:id>/", continent_views.updatetraitement),
    path("deletecontinent/<int:id>/", continent_views.delete),


]