from django.conf.urls import url
from .views import tweet_detail_view, tweet_list_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'tweetapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', tweet_list_view , name = 'list'),
    url(r'^1/$', tweet_detail_view , name = 'detail'),
]
