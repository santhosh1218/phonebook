from django.urls import path
from contacts import views
app_name='contacts'
urlpatterns=[
    path('create/',views.createcontact,name='create'),
    path('display/',views.display,name='display'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search/',views.Search,name='search'),
    path('signup/',views.usersignup,name='signup'),
    path('login/',views.Userlogin,name='login'),
    path('logout/',views.userlogout,name='logout')
]