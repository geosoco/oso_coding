# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('set_id', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'account_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'hashtags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=32, null=True, blank=True)),
                ('media_id', models.BigIntegerField(null=True, blank=True)),
                ('source_status_id', models.BigIntegerField(null=True, blank=True)),
                ('expanded_url', models.CharField(max_length=1000, null=True, blank=True)),
                ('display_url', models.CharField(max_length=300, null=True, blank=True)),
                ('media_url', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'db_table': 'media',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubsetTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'subset_tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('created_at', models.CharField(max_length=64, null=True, blank=True)),
                ('created_ts', models.DateTimeField(null=True, blank=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('text', models.CharField(max_length=500, null=True, blank=True)),
                ('geo_coordinates_0', models.CharField(max_length=40, null=True, blank=True)),
                ('geo_coordinates_1', models.CharField(max_length=40, null=True, blank=True)),
                ('user_screen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('user_followers_count', models.IntegerField(null=True, blank=True)),
                ('user_friends_count', models.IntegerField(null=True, blank=True)),
                ('user_statuses_count', models.IntegerField(null=True, blank=True)),
                ('user_favourites_count', models.IntegerField(null=True, blank=True)),
                ('user_geo_enabled', models.IntegerField(null=True, blank=True)),
                ('user_time_zone', models.CharField(max_length=100, null=True, blank=True)),
                ('retweet_count', models.IntegerField(null=True, blank=True)),
                ('favorite_count', models.IntegerField(null=True, blank=True)),
                ('retweeted', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_screen_name', models.CharField(max_length=80, null=True, blank=True)),
                ('retweeted_status_retweet_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_time_zone', models.CharField(max_length=100, null=True, blank=True)),
                ('retweeted_status_user_friends_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_statuses_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_followers_count', models.IntegerField(null=True, blank=True)),
                ('source', models.CharField(max_length=500, null=True, blank=True)),
                ('in_reply_to_screen_name', models.CharField(max_length=100, null=True, blank=True)),
                ('local_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tweets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TweetMention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_index', models.IntegerField()),
            ],
            options={
                'db_table': 'tweet_mention',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TweetSnapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('snapshot_tweet_id', models.BigIntegerField()),
                ('snapshot_time', models.DateTimeField()),
                ('retweet_source_id', models.BigIntegerField(null=True, blank=True)),
                ('tweet_id', models.BigIntegerField()),
                ('created_at', models.CharField(max_length=64, null=True, blank=True)),
                ('created_ts', models.DateTimeField(null=True, blank=True)),
                ('lang', models.CharField(max_length=20, null=True, blank=True)),
                ('text', models.CharField(max_length=500, null=True, blank=True)),
                ('geo_coordinates_0', models.CharField(max_length=40, null=True, blank=True)),
                ('geo_coordinates_1', models.CharField(max_length=40, null=True, blank=True)),
                ('user_screen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('user_followers_count', models.IntegerField(null=True, blank=True)),
                ('user_friends_count', models.IntegerField(null=True, blank=True)),
                ('user_statuses_count', models.IntegerField(null=True, blank=True)),
                ('user_favourites_count', models.IntegerField(null=True, blank=True)),
                ('user_geo_enabled', models.IntegerField(null=True, blank=True)),
                ('user_time_zone', models.CharField(max_length=100, null=True, blank=True)),
                ('user_description', models.CharField(max_length=512, null=True, blank=True)),
                ('user_location', models.CharField(max_length=512, null=True, blank=True)),
                ('user_created_at', models.CharField(max_length=64, null=True, blank=True)),
                ('user_created_ts', models.DateTimeField(null=True, blank=True)),
                ('user_lang', models.CharField(max_length=8, null=True, blank=True)),
                ('user_listed_count', models.IntegerField(null=True, blank=True)),
                ('user_name', models.CharField(max_length=140, null=True, blank=True)),
                ('user_url', models.CharField(max_length=512, null=True, blank=True)),
                ('user_utc_offset', models.IntegerField(null=True, blank=True)),
                ('user_verified', models.IntegerField(null=True, blank=True)),
                ('user_profile_use_background_image', models.IntegerField(null=True, blank=True)),
                ('user_default_profile_image', models.IntegerField(null=True, blank=True)),
                ('user_profile_sidebar_fill_color', models.CharField(max_length=16, null=True, blank=True)),
                ('user_profile_text_color', models.CharField(max_length=16, null=True, blank=True)),
                ('user_profile_sidebar_border_color', models.CharField(max_length=16, null=True, blank=True)),
                ('user_profile_background_color', models.CharField(max_length=16, null=True, blank=True)),
                ('user_profile_link_color', models.CharField(max_length=16, null=True, blank=True)),
                ('user_profile_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('user_profile_banner_url', models.CharField(max_length=256, null=True, blank=True)),
                ('user_profile_background_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('user_profile_background_tile', models.IntegerField(null=True, blank=True)),
                ('user_contributors_enabled', models.IntegerField(null=True, blank=True)),
                ('user_default_profile', models.IntegerField(null=True, blank=True)),
                ('user_is_translator', models.IntegerField(null=True, blank=True)),
                ('retweet_count', models.IntegerField(null=True, blank=True)),
                ('favorite_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_id', models.BigIntegerField(null=True, blank=True)),
                ('retweeted_status_user_screen_name', models.CharField(max_length=80, null=True, blank=True)),
                ('retweeted_status_retweet_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_time_zone', models.CharField(max_length=100, null=True, blank=True)),
                ('retweeted_status_user_friends_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_statuses_count', models.IntegerField(null=True, blank=True)),
                ('retweeted_status_user_followers_count', models.IntegerField(null=True, blank=True)),
                ('source', models.CharField(max_length=500, null=True, blank=True)),
                ('in_reply_to_screen_name', models.CharField(max_length=100, null=True, blank=True)),
                ('in_reply_to_status_id', models.BigIntegerField(null=True, blank=True)),
                ('in_set', models.IntegerField(null=True, blank=True)),
                ('local_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tweet_snapshots',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000, null=True, blank=True)),
                ('expanded_url', models.CharField(max_length=2000, null=True, blank=True)),
                ('display_url', models.CharField(max_length=300, null=True, blank=True)),
            ],
            options={
                'db_table': 'urls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('screen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('description', models.CharField(max_length=512, null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('friends_count', models.IntegerField(null=True, blank=True)),
                ('statuses_count', models.IntegerField(null=True, blank=True)),
                ('favourites_count', models.IntegerField(null=True, blank=True)),
                ('location', models.CharField(max_length=512, null=True, blank=True)),
                ('created_at', models.CharField(max_length=64, null=True, blank=True)),
                ('created_ts', models.DateTimeField(null=True, blank=True)),
                ('geo_enabled', models.IntegerField(null=True, blank=True)),
                ('lang', models.CharField(max_length=8, null=True, blank=True)),
                ('listed_count', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=140, null=True, blank=True)),
                ('time_zone', models.CharField(max_length=64, null=True, blank=True)),
                ('url', models.CharField(max_length=512, null=True, blank=True)),
                ('utc_offset', models.IntegerField(null=True, blank=True)),
                ('verified', models.IntegerField(null=True, blank=True)),
                ('profile_use_background_image', models.IntegerField(null=True, blank=True)),
                ('default_profile_image', models.IntegerField(null=True, blank=True)),
                ('profile_sidebar_fill_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_text_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_sidebar_border_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_background_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_link_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_banner_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_background_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_background_tile', models.IntegerField(null=True, blank=True)),
                ('contributors_enabled', models.IntegerField(null=True, blank=True)),
                ('default_profile', models.IntegerField(null=True, blank=True)),
                ('is_translator', models.IntegerField(null=True, blank=True)),
                ('source_snapshot_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000, null=True, blank=True)),
                ('title', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'db_table': 'webpages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TweetStats',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='main.Tweet')),
                ('replies_count', models.IntegerField(null=True, blank=True)),
                ('retweet_count', models.IntegerField(null=True, blank=True)),
                ('retweets_in_set', models.IntegerField(null=True, blank=True)),
                ('favorites_count', models.IntegerField(null=True, blank=True)),
                ('duplicate_count', models.IntegerField(null=True, blank=True)),
                ('snapshot_count', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tweets_stats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserCurrent',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='main.User')),
                ('screen_name', models.CharField(max_length=140, null=True, blank=True)),
                ('description', models.CharField(max_length=512, null=True, blank=True)),
                ('followers_count', models.IntegerField(null=True, blank=True)),
                ('friends_count', models.IntegerField(null=True, blank=True)),
                ('statuses_count', models.IntegerField(null=True, blank=True)),
                ('favourites_count', models.IntegerField(null=True, blank=True)),
                ('location', models.CharField(max_length=512, null=True, blank=True)),
                ('created_at', models.CharField(max_length=64, null=True, blank=True)),
                ('created_ts', models.DateTimeField(null=True, blank=True)),
                ('geo_enabled', models.IntegerField(null=True, blank=True)),
                ('lang', models.CharField(max_length=8, null=True, blank=True)),
                ('listed_count', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=140, null=True, blank=True)),
                ('time_zone', models.CharField(max_length=64, null=True, blank=True)),
                ('url', models.CharField(max_length=512, null=True, blank=True)),
                ('utc_offset', models.IntegerField(null=True, blank=True)),
                ('verified', models.IntegerField(null=True, blank=True)),
                ('profile_use_background_image', models.IntegerField(null=True, blank=True)),
                ('default_profile_image', models.IntegerField(null=True, blank=True)),
                ('profile_sidebar_fill_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_text_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_sidebar_border_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_background_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_background_image_url_https', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_link_color', models.CharField(max_length=16, null=True, blank=True)),
                ('profile_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_banner_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_background_image_url', models.CharField(max_length=256, null=True, blank=True)),
                ('profile_background_tile', models.IntegerField(null=True, blank=True)),
                ('contributors_enabled', models.IntegerField(null=True, blank=True)),
                ('default_profile', models.IntegerField(null=True, blank=True)),
                ('is_translator', models.IntegerField(null=True, blank=True)),
                ('request_date', models.DateTimeField(null=True, blank=True)),
                ('deletion_noticed_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'users_current',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.OneToOneField(primary_key=True, db_column='id', serialize=False, to='main.User')),
                ('statuses_count_in_set', models.IntegerField(null=True, blank=True)),
                ('snapshot_count_in_set', models.IntegerField(null=True, blank=True)),
                ('first_tweet_date', models.DateTimeField(null=True, blank=True)),
                ('last_tweet_date', models.DateTimeField(null=True, blank=True)),
                ('first_snapshot_date', models.DateTimeField(null=True, blank=True)),
                ('last_snapshot_date', models.DateTimeField(null=True, blank=True)),
                ('followers_count_min', models.IntegerField(null=True, blank=True)),
                ('followers_count_max', models.IntegerField(null=True, blank=True)),
                ('followers_count_delta', models.IntegerField(null=True, blank=True)),
                ('friends_count_min', models.IntegerField(null=True, blank=True)),
                ('friends_count_max', models.IntegerField(null=True, blank=True)),
                ('friends_count_delta', models.IntegerField(null=True, blank=True)),
                ('statuses_count_min', models.IntegerField(null=True, blank=True)),
                ('statuses_count_max', models.IntegerField(null=True, blank=True)),
                ('statuses_count_delta', models.IntegerField(null=True, blank=True)),
                ('favourites_count_min', models.IntegerField(null=True, blank=True)),
                ('favourites_count_max', models.IntegerField(null=True, blank=True)),
                ('favourites_count_delta', models.IntegerField(null=True, blank=True)),
                ('listed_count_min', models.IntegerField(null=True, blank=True)),
                ('listed_count_max', models.IntegerField(null=True, blank=True)),
                ('listed_count_delta', models.IntegerField(null=True, blank=True)),
                ('screen_name_change_count', models.IntegerField(null=True, blank=True)),
                ('name_change_count', models.IntegerField(null=True, blank=True)),
                ('location_change_count', models.IntegerField(null=True, blank=True)),
                ('geo_enabled_change_count', models.IntegerField(null=True, blank=True)),
                ('description_change_count', models.IntegerField(null=True, blank=True)),
                ('profile_change_count', models.IntegerField(null=True, blank=True)),
                ('url_change_count', models.IntegerField(null=True, blank=True)),
                ('timeline_total_retweets', models.IntegerField(null=True, blank=True)),
                ('timeline_total_replied', models.IntegerField(null=True, blank=True)),
                ('timeline_total_favorited', models.IntegerField(null=True, blank=True)),
                ('tweet_retweet_count', models.IntegerField(null=True, blank=True)),
                ('tweet_replies_count', models.IntegerField(null=True, blank=True)),
                ('tweet_with_mentions_count', models.IntegerField(null=True, blank=True)),
                ('tweet_with_urls_count', models.IntegerField(null=True, blank=True)),
                ('tweet_with_media_count', models.IntegerField(null=True, blank=True)),
                ('percent_tweets_retweets', models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)),
                ('percent_tweets_replies', models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)),
                ('percent_tweets_copies', models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)),
                ('percent_tweets_originals', models.DecimalField(null=True, max_digits=16, decimal_places=4, blank=True)),
            ],
            options={
                'db_table': 'users_stats',
                'managed': False,
            },
        ),
    ]