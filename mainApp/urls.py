from django.urls import path
from . import views



urlpatterns = [
    path("",views.indexPage,name="homepage"),
    path('about/',views.about,name='about')   ,
    path('team/',views.team,name='team'),
    path('insights/',views.insightList,name='insightList'),
    path('insight-detail/<int:pk>/',views.insightDetail,name="insightDetail"),
    path('solution-detail/<int:pk>/',views.solutionDetail,name='solutionDetail'),
    path('solutions/',views.solutionList,name='solutions'),
    path('contact/',views.contact,name='contact')
]