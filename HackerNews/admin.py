from django.contrib import admin

from .models import *

admin.site.register(AccountsInvitation)
admin.site.register(AccountCustomUser)
admin.site.register(NewsItem)
admin.site.register(NewsVote)
admin.site.register(NewsStory)
admin.site.register(NewsComment)
admin.site.register(EmailDigestSubscription)
admin.site.register(EmailDigestEmailDigest)
admin.site.register(EmailDigestUnsubscription)
admin.site.register(EmailDigestEmailDigestStories)
admin.site.register(EmailDigestUserSubscription)
admin.site.register(EmailDigestAnonymousSubscription)
admin.site.register(AccountsEmailVerification)
admin.site.register(AccountPasswordResetRequest)
admin.site.register(DjangoContentType)
admin.site.register(AuthPermission)
admin.site.register(AuthGroup)
admin.site.register(DjangoAdminLog)
