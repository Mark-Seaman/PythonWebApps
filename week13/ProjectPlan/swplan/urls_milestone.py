
from django.urls import path

from .views_milestone import MilestoneDeleteView, MilestoneDetailView, MilestoneListView, MilestoneCreateView, MilestoneUpdateView


urlpatterns = [

    # Milestone
    path('',                       MilestoneListView.as_view(),    name='milestone_list'),
    path('<int:pk>',               MilestoneDetailView.as_view(),  name='milestone_detail'),
    path('<int:project>/add',      MilestoneCreateView.as_view(),  name='milestone_add'),
    path('<int:pk>/',              MilestoneUpdateView.as_view(),  name='milestone_edit'),
    path('<int:pk>/delete',        MilestoneDeleteView.as_view(),  name='milestone_delete'),

    # # Book
    # path('book/',                       BookListView.as_view(),    name='book_list'),
    # path('book/<int:pk>',               BookDetailView.as_view(),  name='book_detail'),
    # path('book/add',                    BookCreateView.as_view(),  name='book_add'),
    # path('book/<int:pk>/',              BookUpdateView.as_view(),  name='book_edit'),
    # path('book/<int:pk>/delete',        BookDeleteView.as_view(),  name='book_delete'),

    # # Chapter
    # path('chapter/',                    ChapterListView.as_view(),    name='chapter_list'),
    # path('chapter/<int:pk>',            ChapterDetailView.as_view(),  name='chapter_detail'),
    # path('chapter/add',                 ChapterCreateView.as_view(),  name='chapter_add'),
    # path('chapter/<int:pk>/',           ChapterUpdateView.as_view(),  name='chapter_edit'),
    # path('chapter/<int:pk>/delete',     ChapterDeleteView.as_view(),  name='chapter_delete'),

    # # Note
    # path('note/',                       NoteListView.as_view(),    name='note_list'),
    # path('note/<int:pk>',               NoteDetailView.as_view(),  name='note_detail'),
    # path('note/add',                    NoteCreateView.as_view(),  name='note_add'),
    # path('note/<int:pk>/',              NoteUpdateView.as_view(),  name='note_edit'),
    # path('note/<int:pk>/delete',        NoteDeleteView.as_view(),  name='note_delete'),

]
