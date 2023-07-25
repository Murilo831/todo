from django.urls import path

from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    # Mark as done
    path('mark_as_done/<int:pk>', views.mark_as_done, name='mark_as_done'),
    
    # Mark as Undone
    path('mark_as_undone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
    
    # Edit/Delete Feature
    path('deleteTask/<int:pk>', views.deleteTask, name='deleteTask'),
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    
]
