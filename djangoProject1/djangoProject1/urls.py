from django.contrib import admin
from django.urls import path
from gs1 import views
#from api import views
from gs2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('info/<int:pk>', views.student_detail),
    #path('info/', views.student_list),
    path('student_create/', views.student_create),
]
