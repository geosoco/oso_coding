# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class AccountType(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    set_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    accounts = models.ManyToManyField('User', db_table='user_account_types')

    class Meta:
        managed = False
        db_table = 'account_types'


class Hashtag(models.Model):
    text = models.CharField(max_length=200, blank=True, null=True)
    tweets = models.ManyToManyField('Tweet', db_table='tweet_hashtag')

    class Meta:
        managed = False
        db_table = 'hashtags'


class Media(models.Model):
    type = models.CharField(max_length=32, blank=True, null=True)
    media_id = models.BigIntegerField(blank=True, null=True)
    source_status_id = models.BigIntegerField(blank=True, null=True)
    expanded_url = models.CharField(max_length=1000, blank=True, null=True)
    display_url = models.CharField(max_length=300, blank=True, null=True)
    media_url = models.CharField(max_length=1000, blank=True, null=True)
    tweets = models.ManyToManyField('Tweet', db_table='tweet_media')

    class Meta:
        managed = False
        db_table = 'media'


class SubsetTag(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tweets = models.ManyToManyField('Tweet', db_table='tweet_subset_tags')
    users = models.ManyToManyField('User', db_table='user_subset_tags')

    class Meta:
        managed = False
        db_table = 'subset_tags'




class TweetMention(models.Model):
    tweet = models.ForeignKey('Tweet')
    user = models.ForeignKey('User')
    tweet_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tweet_mention'


class TweetSnapshot(models.Model):
    snapshot_tweet_id = models.BigIntegerField()
    snapshot_time = models.DateTimeField()
    retweet_source_id = models.BigIntegerField(blank=True, null=True)
    tweet_id = models.BigIntegerField()
    created_at = models.CharField(max_length=64, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    geo_coordinates_0 = models.CharField(max_length=40, blank=True, null=True)
    geo_coordinates_1 = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True, related_name="snapshot_user")
    user_screen_name = models.CharField(max_length=140, blank=True, null=True)
    user_followers_count = models.IntegerField(blank=True, null=True)
    user_friends_count = models.IntegerField(blank=True, null=True)
    user_statuses_count = models.IntegerField(blank=True, null=True)
    user_favourites_count = models.IntegerField(blank=True, null=True)
    user_geo_enabled = models.IntegerField(blank=True, null=True)
    user_time_zone = models.CharField(max_length=100, blank=True, null=True)
    user_description = models.CharField(max_length=512, blank=True, null=True)
    user_location = models.CharField(max_length=512, blank=True, null=True)
    user_created_at = models.CharField(max_length=64, blank=True, null=True)
    user_created_ts = models.DateTimeField(blank=True, null=True)
    user_lang = models.CharField(max_length=8, blank=True, null=True)
    user_listed_count = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=140, blank=True, null=True)
    user_url = models.CharField(max_length=512, blank=True, null=True)
    user_utc_offset = models.IntegerField(blank=True, null=True)
    user_verified = models.IntegerField(blank=True, null=True)
    user_profile_use_background_image = models.IntegerField(blank=True, null=True)
    user_default_profile_image = models.IntegerField(blank=True, null=True)
    user_profile_sidebar_fill_color = models.CharField(max_length=16, blank=True, null=True)
    user_profile_text_color = models.CharField(max_length=16, blank=True, null=True)
    user_profile_sidebar_border_color = models.CharField(max_length=16, blank=True, null=True)
    user_profile_background_color = models.CharField(max_length=16, blank=True, null=True)
    user_profile_link_color = models.CharField(max_length=16, blank=True, null=True)
    user_profile_image_url = models.CharField(max_length=256, blank=True, null=True)
    user_profile_banner_url = models.CharField(max_length=256, blank=True, null=True)
    user_profile_background_image_url = models.CharField(max_length=256, blank=True, null=True)
    user_profile_background_tile = models.IntegerField(blank=True, null=True)
    user_contributors_enabled = models.IntegerField(blank=True, null=True)
    user_default_profile = models.IntegerField(blank=True, null=True)
    user_is_translator = models.IntegerField(blank=True, null=True)    
    retweet_count = models.IntegerField(blank=True, null=True)
    favorite_count = models.IntegerField(blank=True, null=True)
    retweeted_status_id = models.BigIntegerField(blank=True, null=True)
    retweeted_status_user_screen_name = models.CharField(max_length=80, blank=True, null=True)
    retweeted_status_retweet_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user = models.ForeignKey('User', blank=True, null=True, related_name="snapshot_retweets")
    retweeted_status_user_time_zone = models.CharField(max_length=100, blank=True, null=True)
    retweeted_status_user_friends_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user_statuses_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user_followers_count = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    in_reply_to_screen_name = models.CharField(max_length=100, blank=True, null=True)
    in_reply_to_status_id = models.BigIntegerField(blank=True, null=True)
    in_reply_to_user = models.ForeignKey('User', blank=True, null=True, related_name="snapshot_replies")
    in_set = models.IntegerField(blank=True, null=True)
    local_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweet_snapshots'



class Tweet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.CharField(max_length=64, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    geo_coordinates_0 = models.CharField(max_length=40, blank=True, null=True)
    geo_coordinates_1 = models.CharField(max_length=40, blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True)
    user_screen_name = models.CharField(max_length=140, blank=True, null=True)
    user_followers_count = models.IntegerField(blank=True, null=True)
    user_friends_count = models.IntegerField(blank=True, null=True)
    user_statuses_count = models.IntegerField(blank=True, null=True)
    user_favourites_count = models.IntegerField(blank=True, null=True)
    user_geo_enabled = models.IntegerField(blank=True, null=True)
    user_time_zone = models.CharField(max_length=100, blank=True, null=True)
    retweet_count = models.IntegerField(blank=True, null=True)
    favorite_count = models.IntegerField(blank=True, null=True)
    retweeted = models.IntegerField(blank=True, null=True)
    retweeted_status = models.ForeignKey('self', blank=True, null=True, related_name="retweets")
    retweeted_status_user_screen_name = models.CharField(max_length=80, blank=True, null=True)
    retweeted_status_retweet_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user = models.ForeignKey('User', blank=True, null=True, related_name="retweets")
    retweeted_status_user_time_zone = models.CharField(max_length=100, blank=True, null=True)
    retweeted_status_user_friends_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user_statuses_count = models.IntegerField(blank=True, null=True)
    retweeted_status_user_followers_count = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=500, blank=True, null=True)
    in_reply_to_screen_name = models.CharField(max_length=100, blank=True, null=True)
    in_reply_to_status = models.ForeignKey('self', blank=True, null=True, related_name="replies")
    in_reply_to_user = models.ForeignKey('User', blank=True, null=True, related_name="replies")
    local_time = models.DateTimeField(blank=True, null=True)
    retweet_source = models.ForeignKey('self', blank=True, null=True, related_name="source_retweet")
    mentions = models.ManyToManyField('User', through=TweetMention, related_name="user_mentions")
    source_snapshot = models.ForeignKey(TweetSnapshot, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweets'

class TweetStats(models.Model):
    id = models.OneToOneField(Tweet, db_column='id', primary_key=True)
    replies_count = models.IntegerField(blank=True, null=True)
    retweet_count = models.IntegerField(blank=True, null=True)
    retweets_in_set = models.IntegerField(blank=True, null=True)
    favorites_count = models.IntegerField(blank=True, null=True)
    duplicate_count = models.IntegerField(blank=True, null=True)
    duplicate_of_tweet = models.ForeignKey(Tweet, db_column='duplicate_of_tweet', blank=True, null=True, related_name="duplicates")
    snapshot_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tweets_stats'        


class Url(models.Model):
    url = models.CharField(max_length=1000, blank=True, null=True)
    expanded_url = models.CharField(max_length=2000, blank=True, null=True)
    display_url = models.CharField(max_length=300, blank=True, null=True)
    tweets = models.ManyToManyField(Tweet, db_table="tweet_url")

    class Meta:
        managed = False
        db_table = 'urls'



class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    screen_name = models.CharField(max_length=140, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    statuses_count = models.IntegerField(blank=True, null=True)
    favourites_count = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.CharField(max_length=64, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    geo_enabled = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=8, blank=True, null=True)
    listed_count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=140, blank=True, null=True)
    time_zone = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    profile_use_background_image = models.IntegerField(blank=True, null=True)
    default_profile_image = models.IntegerField(blank=True, null=True)
    profile_sidebar_fill_color = models.CharField(max_length=16, blank=True, null=True)
    profile_text_color = models.CharField(max_length=16, blank=True, null=True)
    profile_sidebar_border_color = models.CharField(max_length=16, blank=True, null=True)
    profile_background_color = models.CharField(max_length=16, blank=True, null=True)
    profile_link_color = models.CharField(max_length=16, blank=True, null=True)
    profile_image_url = models.CharField(max_length=256, blank=True, null=True)
    profile_banner_url = models.CharField(max_length=256, blank=True, null=True)
    profile_background_image_url = models.CharField(max_length=256, blank=True, null=True)
    profile_background_tile = models.IntegerField(blank=True, null=True)
    contributors_enabled = models.IntegerField(blank=True, null=True)
    default_profile = models.IntegerField(blank=True, null=True)
    is_translator = models.IntegerField(blank=True, null=True)
    source_snapshot_id = models.IntegerField(blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'users'


class UserCurrent(models.Model):
    id = models.OneToOneField(User, db_column='id', primary_key=True)
    screen_name = models.CharField(max_length=140, blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    statuses_count = models.IntegerField(blank=True, null=True)
    favourites_count = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.CharField(max_length=64, blank=True, null=True)
    created_ts = models.DateTimeField(blank=True, null=True)
    geo_enabled = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=8, blank=True, null=True)
    listed_count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=140, blank=True, null=True)
    time_zone = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    utc_offset = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    profile_use_background_image = models.IntegerField(blank=True, null=True)
    default_profile_image = models.IntegerField(blank=True, null=True)
    profile_sidebar_fill_color = models.CharField(max_length=16, blank=True, null=True)
    profile_text_color = models.CharField(max_length=16, blank=True, null=True)
    profile_sidebar_border_color = models.CharField(max_length=16, blank=True, null=True)
    profile_background_color = models.CharField(max_length=16, blank=True, null=True)
    profile_background_image_url_https = models.CharField(max_length=16, blank=True, null=True)
    profile_link_color = models.CharField(max_length=16, blank=True, null=True)
    profile_image_url = models.CharField(max_length=256, blank=True, null=True)
    profile_banner_url = models.CharField(max_length=256, blank=True, null=True)
    profile_background_image_url = models.CharField(max_length=256, blank=True, null=True)
    profile_background_tile = models.IntegerField(blank=True, null=True)
    contributors_enabled = models.IntegerField(blank=True, null=True)
    default_profile = models.IntegerField(blank=True, null=True)
    is_translator = models.IntegerField(blank=True, null=True)
    request_date = models.DateTimeField(blank=True, null=True)
    deletion_noticed_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_current'


class UserStats(models.Model):
    id = models.OneToOneField(User, db_column='id', primary_key=True)
    statuses_count_in_set = models.IntegerField(blank=True, null=True)
    snapshot_count_in_set = models.IntegerField(blank=True, null=True)
    first_tweet_date = models.DateTimeField(blank=True, null=True)
    last_tweet_date = models.DateTimeField(blank=True, null=True)
    first_snapshot_date = models.DateTimeField(blank=True, null=True)
    last_snapshot_date = models.DateTimeField(blank=True, null=True)
    followers_count_min = models.IntegerField(blank=True, null=True)
    followers_count_max = models.IntegerField(blank=True, null=True)
    followers_count_delta = models.IntegerField(blank=True, null=True)
    friends_count_min = models.IntegerField(blank=True, null=True)
    friends_count_max = models.IntegerField(blank=True, null=True)
    friends_count_delta = models.IntegerField(blank=True, null=True)
    statuses_count_min = models.IntegerField(blank=True, null=True)
    statuses_count_max = models.IntegerField(blank=True, null=True)
    statuses_count_delta = models.IntegerField(blank=True, null=True)
    favourites_count_min = models.IntegerField(blank=True, null=True)
    favourites_count_max = models.IntegerField(blank=True, null=True)
    favourites_count_delta = models.IntegerField(blank=True, null=True)
    listed_count_min = models.IntegerField(blank=True, null=True)
    listed_count_max = models.IntegerField(blank=True, null=True)
    listed_count_delta = models.IntegerField(blank=True, null=True)
    screen_name_change_count = models.IntegerField(blank=True, null=True)
    name_change_count = models.IntegerField(blank=True, null=True)
    location_change_count = models.IntegerField(blank=True, null=True)
    geo_enabled_change_count = models.IntegerField(blank=True, null=True)
    description_change_count = models.IntegerField(blank=True, null=True)
    profile_change_count = models.IntegerField(blank=True, null=True)
    url_change_count = models.IntegerField(blank=True, null=True)
    timeline_total_retweets = models.IntegerField(blank=True, null=True)
    timeline_total_replied = models.IntegerField(blank=True, null=True)
    timeline_total_favorited = models.IntegerField(blank=True, null=True)
    tweet_retweet_count = models.IntegerField(blank=True, null=True)
    tweet_replies_count = models.IntegerField(blank=True, null=True)
    tweet_with_mentions_count = models.IntegerField(blank=True, null=True)
    tweet_with_urls_count = models.IntegerField(blank=True, null=True)
    tweet_with_media_count = models.IntegerField(blank=True, null=True)
    percent_tweets_retweets = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)
    percent_tweets_replies = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)
    percent_tweets_copies = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)
    percent_tweets_originals = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'users_stats'


class Webpage(models.Model):
    url = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    tweets = models.ManyToManyField(Tweet, db_table="tweet_webpage")

    class Meta:
        managed = False
        db_table = 'webpages'
