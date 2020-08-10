from django.urls import path, include
from rock.views import review
app_name = 'rock'

urlpatterns = [
    # Review
    path('review/<int:destination_id>/publish', review.publish_review, name='publish_review'),
    path('review/<int:destination_id>/create', review.create_review, name='create_review'),
    path('review/<int:review_id>/show', review.show_review, name='show_review'),
    path('review/<int:review_id>/edit', review.edit_review, name='edit_review'),
    path('review/<int:review_id>/update', review.update_review, name='update_review'),
    path('review/<int:review_id>/delete', review.delete_review, name='delete_review'),

]
