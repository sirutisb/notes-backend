from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NoteListCreateView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
]