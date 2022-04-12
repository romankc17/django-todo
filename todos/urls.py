from django.urls import path
from todos import views, views_api, auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('save', views.save, name='save'),
    path('edit/todos/<int:id>', views.edit, name='edit'),
    path('delete/todos/<int:id>', views.delete, name='delete'),

    # API Route for Ajax
    path('api/todos/<int:id>', views_api.TodoItemView.as_view(), name='api_todo_item'),
    path('api/todos', views_api.TodoListView.as_view(), name='api_todo_list'),

    # Auth Routes
    path('login', auth_views.login, name='login'),
    path('authenticate', auth_views.authenticate, name='authenticate'),
    path('logout', auth_views.logout, name='logout'),
    path('signup', auth_views.signup, name='signup'),
    path('signup/submit', auth_views.signup_submit, name='signup-submit'),
]
