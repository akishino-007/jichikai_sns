from django.urls import path,include

from .import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('j_sns/', views.ListJSnsView.as_view(), name='list-jsns'),
    path('j_sns/kairan', views.ListJSnskairanView.as_view(), name='list-jsns-kairan'),
    path('j_sns/keijiban', views.ListJSnskeijibanView.as_view(), name='list-jsns-keijiban'),
    path('j_sns/osirase', views.ListJSnsosiraseView.as_view(), name='list-jsns-osirase'),
    path('j_sns/<int:pk>/detail/', views.DetailJSnsView.as_view(), name='detail-jsns'),
    path('j_sns/create/', views.CreateJSnsView.as_view(), name='create-jsns'),
    path('j_sns/<int:pk>/delete/', views.DeleteJSnsView.as_view(), name='delete-jsns'),
    path('j_sns/<int:pk>/update/', views.UpdateJSnsView.as_view(), name='update-jsns'),
    path('j_sns/<int:j_sns_id>/review/', views.CreateReviewView.as_view(), name='review'),  
    path('accounts/', include('allauth.urls')),
]