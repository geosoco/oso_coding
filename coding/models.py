from django.db import models
from django.contrib.auth.models import User
import base.models as base_models
import main.models as main_models

from main.models import Tweet as mainTweet, User as mainUser


class CodeScheme(base_models.FullAuditModel):
    """Container for a group of codes."""
    name = models.CharField(max_length=64)
    description = models.TextField()
    mutually_exclusive = models.BooleanField(default=False)

    def __str__(self):
        return "%s (%d)" % (self.name, self.id)

    def __unicode__(self):
        return u"%s (%d)" % (self.name, self.id)


class Code(base_models.FullAuditModel):
    """Code class."""
    scheme = models.ForeignKey(CodeScheme)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    css_class = models.CharField(max_length=64, null=True, blank=True)
    key = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return "%s (%d)" % (self.name, self.scheme_id)

    def __unicode__(self):
        return u"%s (%d)" % (self.name, self.scheme_id)


class Assignment(base_models.FullAuditModel):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    coder = models.ForeignKey(User)
    assigned_users = models.ManyToManyField(mainUser)
    assigned_tweets = models.ManyToManyField(mainTweet, blank=True, null=True)

    def __str__(self):
        return "%s (%s - %s)" % (
            self.id,
            self.name, 
            self.coder.id)

    def __unicode__(self):
        return u"%s (%s - %s)" % (self.id, self.name, self.coder.id)


class TweetCodeInstance(base_models.FullAuditModel):
    code = models.ForeignKey(Code)
    tweet = models.ForeignKey(mainTweet)
    assignment = models.ForeignKey(Assignment, null=True, blank=True)

    def __str__(self):
        return "%s - %d - %s" % (
            self.assignment.id, self.tweet.id, self.code.name)

    def __unicode__(self):
        return u"%s - %d - %s" % (
            self.assignment.id, self.tweet.id, self.code.name)


class UserCodeInstance(base_models.FullAuditModel):

    code = models.ForeignKey(Code)
    user = models.ForeignKey(mainUser)
    assignment = models.ForeignKey(Assignment, null=True, blank=True)

    def __str__(self):
        return "%s - %d - %s" % (
            self.assignment.id, self.user.id, self.code.name)

    def __unicode__(self):
        return u"%s - %d - %s" % (
            self.assignment.id, self.user.id, self.code.name)
