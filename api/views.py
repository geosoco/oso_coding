from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.db.models import Prefetch
from rest_framework import filters, viewsets
from rest_framework.authentication import (
    SessionAuthentication, BasicAuthentication, TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
import api.serializers as api_serializers
import main.models as main_models
import coding.models as coding_models
import filters as api_filters


class DjangoUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = api_serializers.DjangoUserSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("id", )

    def get_queryset(self):
        current_user = self.request.query_params.get("current_user", None)
        if current_user is not None and current_user.lower() == "true":
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
    queryset = main_models.Tweet.objects.all().prefetch_related(
        "retweeted_status", "user", "mentions", "media_set",
        "in_reply_to_user", "in_reply_to_status", "hashtag_set",
        "url_set")
    serializer_class = api_serializers.TweetSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    page_size = 200
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = api_filters.TweetFilter
    #filter_fields = (
    #    "user", "in_reply_to_user", "in_reply_to_status_id",
    #    "created_ts", "retweeted_status",)




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
        current_user = self.request.query_params.get("current_user", None)
        if current_user is not None and current_user.lower() == "true":
            user = self.request.user
            return coding_models.TweetCodeInstance.objects.filter(
                created_by=user.id)
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
    filter_fields = (
        "code", "assignment", "user", "deleted_date", "deleted_by",
        "created_by",)

    def get_queryset(self):
        current_user = self.request.query_params.get("current_user", None)
        if current_user is not None and current_user.lower() == "true":
            user = self.request.user
            filtered = coding_models.UserCodeInstance.objects.filter(
                created_by=user.id, deleted_date=None)
            print filtered.count()
            return filtered
        else:
            return coding_models.UserCodeInstance.objects.filter(
                deleted_date=None)

    def create(self, request, *args, **kwargs):
        request.data["created_by"] = request.user.id
        return super(UserCodeInstanceViewSet, self).create(
            request, *args, **kwargs)

    def perform_destroy(self, instance):
        print "performing delete..."
        if instance is not None:
            instance.deleted_date = timezone.now()
            instance.deleted_by = self.request.user
            instance.save()

    def delete(self, request, pk, format=None):
        print "delete"
        instance = self.get_object(pk)
        if instance is not None:
            instance.deleted_date = timezone.now()
            instance.deleted_by = self.requeset.user
            instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)




class AssignmentViewSet(viewsets.ModelViewSet):
    """
    Viewset for assignment
    """
    serializer_class = api_serializers.AssignmentSerializer
    authentication_classes = (SessionAuthentication,
                              BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        current_user = self.request.query_params.get("current_user", None)
        if current_user is not None and current_user.lower() == "true":
            user = self.request.user
            qs = coding_models.Assignment.objects.filter(coder=user.id)
            qs = qs.prefetch_related("assigned_users")
        else:
            qs = coding_models.Assignment.objects.all().prefetch_related(
                "assigned_users")

        return qs


