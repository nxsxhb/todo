from . import views
from django.urls import path
from todo import settings
from django.conf.urls.static import static

app_name = 'todo-app'
urlpatterns = [
    path('', views.home, name='home'),
    path("delete/<int:id>",views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvhome/',views.TodoListView.as_view(),name='cbvhome'),   
    path('cbvdetails/<int:pk>',views.TodoDetailView.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>',views.TodoUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>',views.TodoDeleteView.as_view(),name='cbvdelete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)