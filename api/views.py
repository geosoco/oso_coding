from django.contrib.auth.models import User, Group
import main.models as main_models
import coding.models as coding_models
from rest_framework import viewsets
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
import api.serializers as api_serializers
from rest_framework import filters
import django_filters
from django.utils import timezone


class DjangoUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = api_serializers.DjangoUserSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    #filter_backends = (filters.DjangoFilterBackend,)
    #filter_fields = ("id", )

    def get_queryset(self):
        if self.request.query_params.get("pk", None) == "current":
            user = self.request.user
            return User.objects.filter(pk=user.id)
        else:
            return User.objects.all()


class DjangoGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = api_serializers.DjangoGroupSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)



class AccountTypeViewSet(viewsets.ModelViewSet):
    """
    Viewset for AccountType
    """
    queryset = main_models.AccountType.objects.all()
    serializer_class = api_serializers.AccountTypeSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class HashtagViewSet(viewsets.ModelViewSet):
    """
    Viewset for Hashtag
    """
    queryset = main_models.Hashtag.objects.all()
    serializer_class = api_serializers.HashtagSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class MediaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Media
    """
    queryset = main_models.Media.objects.all()
    serializer_class = api_serializers.MediaSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class SubsetTagViewSet(viewsets.ModelViewSet):
    """
    Viewset for SubsetTag
    """
    queryset = main_models.SubsetTag.objects.all()
    serializer_class = api_serializers.SubsetTagSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class TweetMentionViewSet(viewsets.ModelViewSet):
    """
    Viewset for TweetMention
    """
    queryset = main_models.TweetMention.objects.all()
    serializer_class = api_serializers.TweetMentionSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class TweetSnapshotViewSet(viewsets.ModelViewSet):
    """
    Viewset for TweetSnapshot
    """
    queryset = main_models.TweetSnapshot.objects.all()
    serializer_class = api_serializers.TweetSnapshotSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class TweetViewSet(viewsets.ModelViewSet):
    """
    Viewset for Tweet
    """
    queryset = main_models.Tweet.objects.all()
    serializer_class = api_serializers.TweetSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        "user", "in_reply_to_user", "in_reply_to_status_id",
        "created_ts")




class UrlViewSet(viewsets.ModelViewSet):
    """
    Viewset for Url
    """
    queryset = main_models.Url.objects.all()
    serializer_class = api_serializers.UrlSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for User
    """
    queryset = main_models.User.objects.all()
    serializer_class = api_serializers.UserSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)




class WebpageViewSet(viewsets.ModelViewSet):
    """
    Viewset for Webpage
    """
    queryset = main_models.Webpage.objects.all()
    serializer_class = api_serializers.WebpageSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)


class CodeSchemeViewSet(viewsets.ModelViewSet):
    """
    Viewset for code scheme
    """
    queryset = coding_models.CodeScheme.objects.all()
    serializer_class = api_serializers.CodeSchemeSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)


class CodeViewSet(viewsets.ModelViewSet):
    """
    Viewset for code
    """
    queryset = coding_models.Code.objects.all()
    serializer_class = api_serializers.CodeSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)


class TweetCodeInstanceViewSet(viewsets.ModelViewSet):
    """
    Viewset for Tweet code instance
    """
    serializer_class = api_serializers.TweetCodeInstanceSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        pk = self.request.query_params.get("created_by", None)
        if pk == "current":
            user = self.request.user
            return coding_models.TweetCodeInstance.objects.filter(created_by=user.id)
        else:
            return coding_models.TweetCodeInstance.objects.all()


class UserCodeInstanceViewSet(viewsets.ModelViewSet):
    """
    Viewset for User code instance
    """
    serializer_class = api_serializers.UserCodeInstanceSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        pk = self.request.query_params.get("created_by", None)
        if pk == "current":
            user = self.request.user
            return coding_models.UserCodeInstance.objects.filter(created_by=user.id)
        else:
            return coding_models.UserCodeInstance.objects.all()



class AssignmentViewSet(viewsets.ModelViewSet):
    """
    Viewset for assignment
    """
    #queryset = coding_models.Assignment.objects.all()
    serializer_class = api_serializers.AssignmentSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        pk = self.request.query_params.get("coder", None)
        if pk == "current":
            user = self.request.user
            return coding_models.Assignment.objects.filter(coder=user.id)
        else:
            return coding_models.Assignment.objects.all()
