from rest_framework import serializers

from .models import *


class AccountCustomUserListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountCustomUser
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser', 'url']


class AccountCustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCustomUser
        fields = ['id', 'used_invitation', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'last_login', 'karma', 'about', 'level', 'left', 'right', 'tree_id',
                  'date_joined']


class AccountsInvitationListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsInvitation
        fields = ['id', 'invite_code', 'invited_email_address', 'url']


class AccountsInvitationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsInvitation
        fields = ['id', 'invite_code', 'invited_email_address', 'num_signups']


class NewsItemListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'user', 'up_votes', 'down_votes', 'url']


class NewsItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id', 'user', 'up_votes', 'down_votes', 'is_ask', 'is_show', 'points', 'num_comments', 'left',
                  'right', 'tree_id', 'level', ]


class NewsVoteListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsVote
        fields = ['id', 'item', 'user', 'url']


class NewsVoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsVote
        fields = ['id', 'item', 'user', 'vote']


class NewsStoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ['item_ptr', 'title', 'text', 'url']


class NewsStoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsStory
        fields = ['item_ptr', 'title', 'text', 'url', 'do_mail']


class NewsCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ['item_ptr', 'to_story']


class NewsCommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = ['item_ptr', 'to_story', 'text']


class EmailDigestSubscriptionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailDigestSubscription
        fields = ['id', 'frequency', 'weekly_weekday', 'url']


class EmailDigestSubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestSubscription
        fields = ['id', 'frequency', 'weekly_weekday', 'verified_email', 'is_active']


class EmailDigestEmailDigestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestEmailDigest
        fields = ['id', 'frequency', 'weekly_weekday']


class EmailDigestUnsubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestUnsubscription
        fields = ['id', 'from_digest', 'subscription']


class EmailDigestEmailDigestStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestEmailDigestStories
        fields = ['id', 'email_digest', 'story']


class EmailDigestUserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestUserSubscription
        fields = ['subscription', 'user']


class EmailDigestAnonymousSubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestAnonymousSubscription
        fields = ['subscription_ptr', 'logged_in_user', 'verified']


class EmailDigestAnonymousSubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailDigestAnonymousSubscription
        fields = ['subscription_ptr', 'logged_in_user', 'verified', 'verified_at', 'verified_code', 'email']


class AccountsEmailVerificationListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountsEmailVerification
        fields = ['id', 'user', 'verified', 'url']


class AccountsEmailVerificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsEmailVerification
        fields = ['id', 'user', 'verified', 'verified_at', 'verification_code', 'email']


class AccountPasswordResetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPasswordResetRequest
        fields = ['id', 'user', 'verified_code']


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = ['id', 'app_label', 'model']


class AuthPermissionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthPermission
        fields = ['id', 'custom_user', 'content_type', 'url']


class AuthPermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = ['id', 'custom_user', 'content_type', 'name', 'codename']


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = ['id', 'name', 'permission', 'custom_user']


class DjangoAdminLogListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = ['id', 'user', 'content_type', 'object_repr', 'url']


class DjangoAdminLogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = ['id', 'user', 'content_type', 'object_repr', 'change_message', 'object_id', 'action_flag',
                  'action_time']
