from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import authentication.views
import blog.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', authentication.views.LoginPage.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('flux/', blog.views.flux, name='flux'),
    path('my_posts/', blog.views.user_posts, name='my-posts'),
    path('LITReview/<int:ticket_id>/<int:review_id>/edit_review', blog.views.EditReview.as_view(), name='edit_review'),
    path('LITReview/<int:ticket_id>/edit_ticket', blog.views.EditTicket.as_view(), name='edit_ticket'),
    path('LITReview/post', blog.views.view_post, name='view_post'),
    path('LITReview/follow_users', blog.views.FollowUsers.as_view(), name='follow-users'),
    path('LITReview/create_ticket', blog.views.CreateTicket.as_view(), name='create_ticket'),
    path('LITReview/create_review', blog.views.CreateReview.as_view(), name='create_review'),
    path('LITReview/<int:ticket_id>/create_ticket_review',
         blog.views.CreateTicketReview.as_view(),
         name='create_ticket_review'),
    path('LITReview/subscriptions', blog.views.subscriptions, name='subscriptions'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

