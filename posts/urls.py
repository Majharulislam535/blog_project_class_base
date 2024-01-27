from django.urls import path
from .import views

urlpatterns = [
    # path('add_post/',views.add_post,name='add_post'),
    path('add_post/',views.AddPost_view.as_view(),name='add_post'),
    # path('edit_post/<int:id>/',views.edit_post,name='edit_post'),
    path('edit_post/<int:id>/',views.Edit_Post_View.as_view(),name='edit_post'),
    # path('delete_post/<int:id>/',views.delete_post,name='delete_post'),
    path('delete_post/<int:id>/',views.DeletePostView.as_view(),name='delete_post'),
    path('details_post/<int:id>/',views.DetailsView.as_view(),name='details_post'),
]