from django.urls import path
from user.views import sign_up,user_login,Log_out,Activate_user,admin_dashboard,assign_role,create_group,group_list
urlpatterns = [

    path("sign_up/",sign_up,name="sign_up"),
    path("login/",user_login,name="login"),
    path("logout/",Log_out,name="logout"),
    path("activate/<int:user_id>/<str:token>/", Activate_user, name="activate"),
    path("admin_dashboard/",admin_dashboard,name='admin_dashboard'),
    path("assign_role/<int:user_id>/",assign_role,name="assign_role"),
    path("create_group/",create_group,name="create_group"),
    path("group_list/",group_list,name="group_list")

]
