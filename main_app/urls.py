from django.urls import path

from main_app import views, admin_views, Donor_views, Receiver_views

urlpatterns = [
   path("dashboard",views.dashboard,name="dashboard"),
   path("Login",views.Login,name="Login"),
   path("DonerRegister",views.DonerR,name="DonerRegister"),
   path("ReceiverRegister",views.ReceiverR,name="ReceiverRegister"),
   path("",views.Land,name="Land"),
   path("login_view",views.login_view,name="login_view"),
#admin
   path("admin_view",admin_views.admin_view,name="admin_view") ,
   path("Donor_view",Donor_views.Donor_view,name="Donor_view") ,
   path("Receiver_view",Receiver_views.Receiver_view,name="Receiver_view"),
   path("delete/<int:id>",admin_views.remove,name="delete"),
   path("update/<int:id>",admin_views.update,name="update"),
   path("table_view",admin_views.table_view,name="table_view"),
path("table2_view",admin_views.table2_view,name="table2_view"),
path("delete2/<int:id>",admin_views.remove2,name="delete2"),
   path("update2/<int:id>", admin_views.update2, name="update2"),



    path("Receiver_req",Receiver_views.Receiver_req,name="Receiver_req"),
   path("req_table",Receiver_views.req_table,name="req_table"),
   path("req_admin",admin_views.req_admin,name="req_admin"),
   path("rmv_req/<int:id>",Receiver_views.rmv_req,name="rmv_req"),
   path("req_donor",Donor_views.req_donor,name="req_donor"),
   path("Donate/<int:id>",Donor_views.Donate,name="Donate"),
   path("Donor_accept",admin_views.Donor_accept,name="Donor_accept"),
   path("accept/<int:id>",admin_views.accept,name="accept"),
   path("reject/<int:id>",admin_views.reject,name="reject"),
   path("accept_view",admin_views.accept_view,name="accept_view"),
   path("feedbk",admin_views.feedbk,name="feedbk"),
   path("replay",Receiver_views.replay,name="replay"),
   path("replay_view",admin_views.replay_view,name="replay_view"),
   path("replay_feedback/<int:id>",admin_views.replay_feedback,name="replay_feedback"),
   path("profile_donor",Donor_views.profile_donor,name="profile_donor"),
   path("profile_receiver",Receiver_views.profile_receiver,name="profile_receiver"),
   path("donor_update/<int:id>",Donor_views.donor_update,name="donor_update"),
   path("receiver_update/<int:id>",Receiver_views.receiver_update,name="receiver_update"),
   path("logou",admin_views.logou,name="logou"),
   path("logou",Receiver_views.logou,name="logou"),
path("logou",Donor_views.logou,name="logou")






]


