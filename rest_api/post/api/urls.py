from django.urls import path

from post.api.views import (
    post_list_api,
    post_detailed_api,
    post_delete_api,
    post_update_api
)

urlpatterns = [
    path('all/', post_list_api, name="post-list-api"),
    path('<int:pk>/', post_detailed_api, name="post-detailed-api"),
    path('<int:pk>/delete/', post_delete_api, name="post-delete-api"),
    path('<int:pk>/update/', post_update_api, name="post-update-api"),
]