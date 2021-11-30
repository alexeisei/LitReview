from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from litReview_site import views


urlpatterns = [
    path('', views.index, name="home"),
    path('home/', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout_user, name="logout"),
    path('flux/', views.flux, name="flux"),
    path('follow/', views.follow_users, name="follow"),
    path('unfollow/<int:id_follow>/', views.unfollow_user, name="unfollow"),
    path('new-ticket/', views.create_ticket, name="new-ticket"),
    path('new-critic/', views.create_critics, name="new-critic"),
    path('answer-critic/<int:ticket_id>/', views.answer_to_critic, name="answer-critic"),
    path('show-critics/', views.show_own_critics, name="show-critics"),
    path('edit-critics/<int:review_id>/', views.edit_own_critics, name="edit-critics"),
    path('edit-ticket/<int:ticket_id>/', views.edit_own_ticket, name="edit-ticket"),
    path('delticket/<int:ticket_id>/', views.del_ticket, name="delticket"),
    path('delreview/<int:review_id>/', views.del_review, name="delreview"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
