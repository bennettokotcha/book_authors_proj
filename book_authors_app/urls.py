from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add-book', views.add_book),
    path('book/<int:number>', views.book_details),
    path('results/<int:number>', views.results),
    path('authors', views.authors),
    path('add-author', views.add_author),
    path('author/<int:number>', views.author_details),
    path('author-results/<int:number>', views.author_results),
    # path('add-this-author', views.add_this_author),
]
