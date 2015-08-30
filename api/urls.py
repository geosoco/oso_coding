from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'sysusers', views.DjangoUserViewSet, base_name="sysusers")
router.register(r'sysgroups', views.DjangoGroupViewSet, base_name="sysgroups")
router.register(r'accounttype', views.AccountTypeViewSet)
router.register(r'hashtag', views.HashtagViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'subsettag', views.SubsetTagViewSet)
router.register(r'tweetmention', views.TweetMentionViewSet)
router.register(r'tweetsnapshot', views.TweetSnapshotViewSet)
router.register(r'tweet', views.TweetViewSet)
router.register(r'url', views.UrlViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'webpage', views.WebpageViewSet)
router.register(r'codescheme', views.CodeSchemeViewSet)
router.register(r'code', views.CodeViewSet)
router.register(r'tweetcodeinstance', views.TweetCodeInstanceViewSet)
router.register(r'usercodeinstance', views.UserCodeInstanceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
