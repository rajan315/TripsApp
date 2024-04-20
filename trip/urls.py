
from django.urls import path
from .views import HomeView,trips_list,TripCreateView,TripDetailView,NoteDetailView,NoteListView,NoteCreateView,NoteDeleteView,NoteUpdateView,TripDeleteView,TripUpdateView

urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("dashboard/",trips_list,name="trip-list"),
    path("dashboard/note/",NoteListView.as_view(),name="note-list"),
    path("dashboard/trip/create/",TripCreateView.as_view(),name="trip-create"),
    path("dashboard/note/create",NoteCreateView.as_view(),name="note-create"),
    path("dashboard/trip/<int:pk>/",TripDetailView.as_view(),name="trip-detail"),
    path("dashboard/note/<int:pk>/",NoteDetailView.as_view(),name="note-detail"),
    path("dashboard/trip/<int:pk>/delete",TripDeleteView.as_view(),name="trip-delete"),
    path("dashboard/trip/<int:pk>/update",TripUpdateView.as_view(),name="trip-update"),
    path("dashboard/note/<int:pk>/delete",NoteDeleteView.as_view(),name="note-delete"),
    path("dashboard/note/<int:pk>/update",NoteUpdateView.as_view(),name="note-update"),
]

# note delete does not require template
#  note update uses the same template as note create