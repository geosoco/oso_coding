from django.contrib.auth.models import User, Group
import main.models as main_models
import coding.models as coding_models
from rest_framework import serializers


class DjangoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class DjangoUserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
        read_only_fields = ('username',)


class DjangoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.AccountType
        fields = ('id', 'name', 'set_id', 'description')


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.Hashtag
        fields = ('id', 'text')


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.Media
        fields = (
            'id', 'type', 'media_id', 'source_status_id',
            'expanded_url', 'display_url', 'media_url')


class SubsetTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.SubsetTag
        fields = ('id', 'name', 'description')


class TweetMentionSerializer(serializers.ModelSerializer):
    tweet = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = main_models.TweetMention
        fields = ('id', 'tweet', 'user')


class TweetSnapshotSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    retweeted_status_user = serializers.PrimaryKeyRelatedField(read_only=True)
    in_reply_to_user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = main_models.TweetSnapshot
        fields = (
            'id', 'snapshot_tweet_id', 'snapshot_time', 'retweet_source_id',
            'tweet_id', 'created_at', 'created_ts', 'lang', 'text',
            'geo_coordinates_0', 'geo_coordinates_1', 'user',
            'user_screen_name', 'user_followers_count', 'user_friends_count',
            'user_statuses_count', 'user_favourites_count',
            'user_geo_enabled', 'user_time_zone', 'user_description',
            'user_location', 'user_created_at', 'user_created_ts',
            'user_lang', 'user_listed_count', 'user_name', 'user_url',
            'user_utc_offset', 'user_verified', 'retweet_count',
            'favorite_count', 'retweeted_status_id',
            'retweeted_status_user_screen_name',
            'retweeted_status_retweet_count', 'retweeted_status_user',
            'retweeted_status_user_time_zone',
            'retweeted_status_user_friends_count',
            'retweeted_status_user_statuses_count',
            'retweeted_status_user_followers_count',
            'source', 'in_reply_to_screen_name', 'in_reply_to_status_id',
            'in_reply_to_user', 'in_set', 'local_time',
            'user_profile_use_background_image', 'user_default_profile_image',
            'user_profile_sidebar_fill_color', 'user_profile_text_color',
            'user_profile_sidebar_border_color',
            'user_profile_background_color', 'user_profile_link_color',
            'user_profile_image_url', 'user_profile_banner_url',
            'user_profile_background_image_url',
            'user_profile_background_tile', 'user_contributors_enabled',
            'user_default_profile', 'user_is_translator')


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    retweeted_status = serializers.PrimaryKeyRelatedField(read_only=True)
    retweeted_status_user = serializers.PrimaryKeyRelatedField(read_only=True)
    in_reply_to_status = serializers.PrimaryKeyRelatedField(read_only=True)
    in_reply_to_user = serializers.PrimaryKeyRelatedField(read_only=True)
    retweet_source = serializers.PrimaryKeyRelatedField(read_only=True)
    mentions = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    source_snapshot = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = main_models.Tweet
        fields = (
            'id', 'created_at', 'created_ts', 'lang', 'text',
            'geo_coordinates_0', 'geo_coordinates_1', 'user',
            'user_screen_name', 'user_followers_count',
            'user_friends_count', 'user_statuses_count',
            'user_favourites_count', 'user_geo_enabled',
            'user_time_zone', 'retweet_count', 'favorite_count',
            'retweeted', 'retweeted_status',
            'retweeted_status_user_screen_name',
            'retweeted_status_retweet_count', 'retweeted_status_user',
            'retweeted_status_user_time_zone',
            'retweeted_status_user_friends_count',
            'retweeted_status_user_statuses_count',
            'retweeted_status_user_followers_count', 'source',
            'in_reply_to_screen_name', 'in_reply_to_status',
            'in_reply_to_user', 'local_time', 'retweet_source', 'mentions',
            'source_snapshot')


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.Url
        fields = ('id', 'url', 'expanded_url', 'display_url')


class UserSerializer(serializers.ModelSerializer):
    source_snapshot_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = main_models.User
        fields = (
            'id', 'screen_name', 'description', 'followers_count',
            'friends_count', 'statuses_count', 'favourites_count',
            'location', 'created_at', 'created_ts', 'geo_enabled',
            'lang', 'listed_count', 'name', 'time_zone', 'url',
            'utc_offset', 'verified', 'profile_use_background_image',
            'default_profile_image', 'profile_sidebar_fill_color',
            'profile_text_color', 'profile_sidebar_border_color',
            'profile_background_color', 'profile_link_color',
            'profile_image_url', 'profile_banner_url',
            'profile_background_image_url', 'profile_background_tile',
            'contributors_enabled', 'default_profile', 'is_translator',
            'source_snapshot_id')


class UserSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = main_models.User
        fields = ('id', 'screen_name')


class WebpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = main_models.Webpage
        fields = ('id', 'url', 'title')

class CodeSerializer(serializers.ModelSerializer):
    scheme = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.CodeScheme.objects.all())

    class Meta:
        model = coding_models.Code
        fields = (
            'created_by', 'created_date', 'deleted_by', 'deleted_date',
            'scheme', 'name', 'description', 'css_class', 'key'
            )

class CodeSchemeSerializer(serializers.ModelSerializer):
    code_set = CodeSerializer(many=True, read_only=True)

    class Meta:
        model = coding_models.CodeScheme
        fields = (
            'created_by', 'created_date', 'deleted_by', 'deleted_date',
            'name', 'description', 'mutually_exclusive', 'code_set'
            )
        #read_only_fields = ('codes')


class TweetCodeInstanceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.Code.objects.all(), many=False,
        style={'base_template': 'input.html'})
    tweet = serializers.PrimaryKeyRelatedField(
        queryset=main_models.Tweet.objects.all(), many=False,
        style={'base_template': 'input.html'})
    assignment = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.Assignment.objects.all(), many=False,
        style={'base_template': 'input.html'})

    class Meta:
        model = coding_models.TweetCodeInstance
        fields = (
            'created_by', 'created_date', 'deleted_by', 'deleted_date',
            'code', 'tweet', 'assignment'
            )


class UserCodeInstanceSerializer(serializers.ModelSerializer):
    code = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.Code.objects.all(), many=False,
        style={'base_template': 'input.html'})
    user = serializers.PrimaryKeyRelatedField(
        queryset=main_models.User.objects.all(), many=False,
        style={'base_template': 'input.html'})
    assignment = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.Assignment.objects.all(), many=False,
        style={'base_template': 'input.html'})

    class Meta:
        model = coding_models.UserCodeInstance
        fields = (
            'created_by', 'created_date', 'deleted_by', 'deleted_date',
            'code', 'user', 'assignment'
            )

class AssignmentSerializer(serializers.ModelSerializer):
    coder = serializers.PrimaryKeyRelatedField(
        queryset=coding_models.Code.objects.all(), many=False)
    assigned_users = UserSimpleSerializer(
        many=True,
        style={'base_template': 'input.html'})
    assigned_tweets = TweetSerializer(
        many=True,
        style={'base_template': 'input.html'})

    class Meta:
        model = coding_models.Assignment
        fields = (
            'created_by', 'created_date', 'deleted_by', 'deleted_date',
            'id', 'name', 'description',
            'coder', 'assigned_users', 'assigned_tweets'
            )
