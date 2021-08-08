from django.urls import path
from .import views


urlpatterns = [

    path('',views.departfun,name='departfun'),
    path('<slug:d_slug>/',views.departfun,name="departfun"),
    path('<slug:d_slug>/<slug:doc_slug>/', views.doctfunc, name="doctfunc"),

    # path('<slug:d_slug>/<slug:doc_slug>/',views.doctfunc,name="doctfunc")

]