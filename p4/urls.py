from django.contrib import admin
from django.urls import include, path
from draw import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('draw/', views.index, name = 'index'),
    path('custom/', views.custom, name = 'custom'),
    path('ingredientSelect/', views.ingredientSelect, name='ingredientSelect'),
    path('processSelect/', views.processSelect, name='processSelect'),
    path('finalDetails/', views.finalDetails, name='finalDetails'),
    path('submissionConfirmation/', views.submissionConfirmation, name='submissionConfirmation'),
]
