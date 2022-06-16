from django.urls import include, path


urlpatterns = [

    # Blog
    path('', BlogListView.as_view()),
    path('blog/', include('blog.urls_blog')),
    path('article/', include('blog.urls_article')),

]
