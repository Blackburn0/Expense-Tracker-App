from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),

    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password-change-one"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name="password-change"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password-reset-complete"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password-reset-done"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name="password-reset"),

    path('books/', get_all_book, name="books"),
    path('book/detail/<int:pk>/', book_details, name="book-detail"),
    path('book/add/', add_book, name="add-book"),
    path('book/update/<int:pk>/', update_book, name="update-book"),
    path('book/delete/<int:pk>/', delete_book, name="delete-book"),
    path('upload/', upload_file, name="upload-file"),
]
