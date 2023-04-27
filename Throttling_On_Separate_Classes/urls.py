from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuapi/', views.StudentList.as_view()),
    # path('stucreate/', views.StudentCreate.as_view()),
    # path('stuapi/<int:pk>', views.StudentRetrieve.as_view()),
    # path('updatestuapi/<int:pk>', views.StudentUpdate.as_view()),
    # path('destorystuapi/<int:pk>', views.StudentDestroy.as_view()),
]
