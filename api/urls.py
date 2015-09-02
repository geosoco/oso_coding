from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'sysusers', views.DjangoUserViewSet, base_name="sysusers")
router.register(r'sysgroups', views.DjangoGroupViewSet, base_name="sysgroups")
router.register(r'accounttype', views.AccountTypeViewSet)
router.register(r'hashtag', views.HashtagViewSet, base_name="hashtag")
router.register(r'media', views.MediaViewSet, base_name="media")
router.register(r'subsettag', views.SubsetTagViewSet, base_name="subsettag")
router.register(r'tweetmention', views.TweetMentionViewSet, base_name="tweetmention")
router.register(r'tweetsnapshot', views.TweetSnapshotViewSet, base_name="tweetsnapshot")
router.register(r'tweet', views.TweetViewSet, base_name="tweet")
router.register(r'url', views.UrlViewSet, base_name="url")
router.register(r'user', views.UserViewSet, base_name="user")
router.register(r'webpage', views.WebpageViewSet, base_name="webpage")
router.register(r'codescheme', views.CodeSchemeViewSet, base_name="codescheme")
router.register(r'code', views.CodeViewSet, base_name="code")
router.register(r'tweetcodeinstance', views.TweetCodeInstanceViewSet, base_name="tweetcodeinstance")
router.register(r'usercodeinstance', views.UserCodeInstanceViewSet, base_name="usercodeinstance")
router.register(r'assignment', views.AssignmentViewSet, base_name="assignment")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
]
