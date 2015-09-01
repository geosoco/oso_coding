from django.contrib.auth.models import User, Group
import main.models as main_models
import coding.models as coding_models
from rest_framework import viewsets
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
import api.serializers as api_serializers
import django_filters
from django.utils import timezone


class DjangoUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = api_serializers.DjangoUserSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current' and request.user:
            kwargs['pk'] = request.user.pk

        return super(DjangoUserViewSet, self).dispatch(request, *args, **kwargs)

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




class HashtagViewSet(viewsets.ModelViewSet):
    """
    Viewset for Hashtag
    """
    queryset = main_models.Hashtag.objects.all()
    serializer_class = api_serializers.HashtagSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class MediaViewSet(viewsets.ModelViewSet):
    """
    Viewset for Media
    """
    queryset = main_models.Media.objects.all()
    serializer_class = api_serializers.MediaSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class SubsetTagViewSet(viewsets.ModelViewSet):
    """
    Viewset for SubsetTag
    """
    queryset = main_models.SubsetTag.objects.all()
    serializer_class = api_serializers.SubsetTagSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class TweetMentionViewSet(viewsets.ModelViewSet):
    """
    Viewset for TweetMention
    """
    queryset = main_models.TweetMention.objects.all()
    serializer_class = api_serializers.TweetMentionSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class TweetSnapshotViewSet(viewsets.ModelViewSet):
    """
    Viewset for TweetSnapshot
    """
    queryset = main_models.TweetSnapshot.objects.all()
    serializer_class = api_serializers.TweetSnapshotSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class TweetViewSet(viewsets.ModelViewSet):
    """
    Viewset for Tweet
    """
    queryset = main_models.Tweet.objects.all()
    serializer_class = api_serializers.TweetSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class UrlViewSet(viewsets.ModelViewSet):
    """
    Viewset for Url
    """
    queryset = main_models.Url.objects.all()
    serializer_class = api_serializers.UrlSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset for User
    """
    queryset = main_models.User.objects.all()
    serializer_class = api_serializers.UserSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)




class WebpageViewSet(viewsets.ModelViewSet):
    """
    Viewset for Webpage
    """
    queryset = main_models.Webpage.objects.all()
    serializer_class = api_serializers.WebpageSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class CodeSchemeViewSet(viewsets.ModelViewSet):
    """
    Viewset for code scheme
    """
    queryset = coding_models.CodeScheme.objects.all()
    serializer_class = api_serializers.CodeSchemeSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class CodeViewSet(viewsets.ModelViewSet):
    """
    Viewset for code
    """
    queryset = coding_models.Code.objects.all()
    serializer_class = api_serializers.CodeSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class TweetCodeInstanceViewSet(viewsets.ModelViewSet):
    """
    Viewset for Tweet code instance
    """
    queryset = coding_models.TweetCodeInstance.objects.all()
    serializer_class = api_serializers.TweetCodeInstanceSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserCodeInstanceViewSet(viewsets.ModelViewSet):
    """
    Viewset for User code instance
    """
    queryset = coding_models.UserCodeInstance.objects.all()
    serializer_class = api_serializers.UserCodeInstanceSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class AssignmentViewSet(viewsets.ModelViewSet):
    """
    Viewset for assignment
    """
    queryset = coding_models.Assignment.objects.all()
    serializer_class = api_serializers.AssignmentSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
