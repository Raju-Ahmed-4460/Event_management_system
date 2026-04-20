from django.urls import path
from user.views import sign_up,user_login,Log_out,Activate_user
urlpatterns = [

    path("sign_up/",sign_up,name="sign_up"),
    path("login/",user_login,name="login"),
    path("logout/",Log_out,name="logout"),
    path("activate/<int:user_id>/<str:token>/", Activate_user, name="activate"),

]
