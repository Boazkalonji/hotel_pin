from django.urls import path
from .views import *

app_name = 'utilisateurs'

urlpatterns = [
    path('login', login_users , name='login_users'),
    path('singup', sing_up , name='sing_up'),
    path('update_user', update_user , name='update_user'),
    path('reservation', reservation , name='reservation'),
]