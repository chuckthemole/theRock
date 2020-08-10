from django.urls import path, include
from rock.views import comment
app_name = 'rock'

urlpatterns = [
    # Comment
    path('comment/<int:review_id>/publish', comment.publish_comment, name='publish_comment'),
    path('comment/<int:review_id>/create', comment.create_comment, name='create_comment'),
    path('comment/<int:comment_id/show', comment.show_comment, name='show_comment'),
    path('comment/<int:comment_id>/edit', comment.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/update', comment.update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete', comment.delete_comment, name='delete_comment'),
]
