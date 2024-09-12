from django.urls import path,re_path
from .views import homePage,login,signup,dashboard, logout,displayNote, deleteNote,custom_404_view

urlpatterns = [
    path('', homePage, name='homepage'),
    path('login/', login, name='login'),
    path('sign_up/', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('note/', displayNote, name='newnote'),
    path('note/<int:note_id>/',displayNote, name='modifynote'),
    path('note/delete/<int:note_id>/', deleteNote, name='deletenote'),
]
