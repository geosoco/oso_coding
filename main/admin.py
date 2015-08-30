from django.contrib import admin
from base.admin import CreatedByBaseAdmin, FullAuditBaseAdmin
import models

#
#
#
class AccountTypeAdmin(FullAuditBaseAdmin):
    """
    AccountType Admin
    """

    list_display = ('id', 'name', 'set_id', 'description')
    readonly_fields = ('id', 'name', 'set_id', 'description')



class HashtagAdmin(FullAuditBaseAdmin):
    """
    Hashtag Admin
    """

    list_display = ('id', 'text')
    readonly_fields = ('id', 'text')



class MediaAdmin(FullAuditBaseAdmin):
    """
    Media Admin
    """

    list_display = ('id', 'type', 'expanded_url', 'media_url')
    readonly_fields = ('id', 'type', 'expanded_url', 'media_url')



class SubsetTagAdmin(FullAuditBaseAdmin):
    """
    SubsetTag Admin
    """

    list_display = ('id', 'name', 'description')
    readonly_fields = ('id', 'name', 'description')



class TweetMentionAdmin(FullAuditBaseAdmin):
    """
    TweetMention Admin
    """

    list_display = ('id', 'tweet_id', 'user_id')
    readonly_fields = ('id', 'tweet_id', 'user_id')



class TweetSnapshotAdmin(FullAuditBaseAdmin):
    """
    TweetSnapshot Admin
    """

    list_display = ('id', 'tweet_id', 'user_screen_name', 'text')
    readonly_fields = ('id', 'tweet_id', 'user_screen_name', 'text')



class TweetAdmin(FullAuditBaseAdmin):
    """
    Tweet Admin
    """

    list_display = ('id', 'user_screen_name', 'text', 'retweeted_status_id')
    readonly_fields = ('id', 'user_screen_name', 'text', 'retweeted_status_id')



class TweetStatsAdmin(FullAuditBaseAdmin):
    """
    TweetStats Admin
    """

    list_display = ('id', 'replies_count', 'retweet_count')
    readonly_fields = ('id', 'replies_count', 'retweet_count')



class UrlAdmin(FullAuditBaseAdmin):
    """
    Url Admin
    """

    list_display = ('id', 'expanded_url', 'display_url')
    readonly_fields = ('id', 'expanded_url', 'display_url')



class UserAdmin(FullAuditBaseAdmin):
    """
    User Admin
    """

    list_display = ('id', 'screen_name', 'name')
    readonly_fields = ('id', 'screen_name', 'name')



class UserCurrentAdmin(FullAuditBaseAdmin):
    """
    UserCurrent Admin
    """

    list_display = ('id', 'screen_name', 'name')
    readonly_fields = ('id', 'screen_name', 'name')



class UserStatsAdmin(FullAuditBaseAdmin):
    """
    UserStats Admin
    """

    list_display = ('id', )
    readonly_fields = ('id', )



class WebpageAdmin(FullAuditBaseAdmin):
    """
    Webpage Admin
    """

    list_display = ('id', 'url', 'title')
    readonly_fields = ('id', 'url', 'title')




# register admin
admin.site.register(models.AccountType, AccountTypeAdmin)
admin.site.register(models.Hashtag, HashtagAdmin)
admin.site.register(models.Media, MediaAdmin)
admin.site.register(models.SubsetTag, SubsetTagAdmin)
admin.site.register(models.TweetMention, TweetMentionAdmin)
admin.site.register(models.TweetSnapshot, TweetSnapshotAdmin)
admin.site.register(models.Tweet, TweetAdmin)
admin.site.register(models.TweetStats, TweetStatsAdmin)
admin.site.register(models.Url, UrlAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserCurrent, UserCurrentAdmin)
admin.site.register(models.UserStats, UserStatsAdmin)
admin.site.register(models.Webpage, WebpageAdmin)
