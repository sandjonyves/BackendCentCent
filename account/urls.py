from django.urls import path,include
from .views import *
from rest_framework import routers

route =routers.SimpleRouter()

route.register('register',UserRegister,basename='user')


route.register('etudiant',EtudiantUser,basename='etudiant')
route.register('marchand',MarchandUser,basename='marchand')
route.register('admin',AdminRegister,basename='admin')
# route.register('otheretudiant',OtheretudiantView,basename = 'other-etudiant')
# route.register('marchand-register',MarchantREgister,basename='marchant')
# route.register('admin-register',AdminREgister,basename='admin')

urlpatterns =[
    # path('register',etudiantRegister.as_view(),name = 'register'),
    
    path('',include(route.urls)),
    # path('user/etudiant/',etudiantUser.as_view(),name='user'),
    
    # path('etudiant',etudiantUser.as_view(),name='etudiant'  ),

    path('login',UserLogin.as_view(),name='login'),
    path('logout/<id>',Logout.as_view(),name='logout'),
]