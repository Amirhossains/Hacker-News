from django.db import models

# from users.models import AccountCustomUser


class AccountsInvitation(models.Model):
    # inviting_user = models.ForeignKey(to=AccountCustomUsers, on_delete=models.CASCADE)
    # users = models.ForeignKey(to=AccountCustomUsers)
    invite_code = models.IntegerField(verbose_name='invite code')
    invited_email_address = models.CharField(verbose_name='invited email address', max_length=32, blank=True)
    num_signups = models.IntegerField(verbose_name='num signups', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.invite_code}'


class AccountCustomUser(models.Model):
    # parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    used_invitation = models.ForeignKey(to=AccountsInvitation, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(verbose_name='user name', max_length=32)
    email = models.CharField(verbose_name='email', max_length=32)
    password = models.CharField(verbose_name='password', max_length=12)
    first_name = models.CharField(verbose_name='first name', max_length=20, blank=True, null=True)
    last_name = models.CharField(verbose_name='last name', max_length=20, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='is active', default=False)
    is_staff = models.BooleanField(verbose_name='is staff', default=False)
    is_superuser = models.BooleanField(verbose_name='is superuser', default=False)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)
    karma = models.IntegerField(verbose_name='karma', default=0, blank=True, null=True)
    about = models.TextField(verbose_name='about', blank=True)
    level = models.IntegerField(verbose_name='level')
    left = models.IntegerField(verbose_name='left', blank=True, null=True)
    right = models.IntegerField(verbose_name='right', blank=True, null=True)
    tree_id = models.IntegerField(verbose_name='tree id', blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    def __str__(self):
        return f'{self.username}  {self.is_staff}'


class NewsItem(models.Model):
    # parent = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    up_votes = models.IntegerField(verbose_name='up votes')
    down_votes = models.IntegerField(verbose_name='down votes')
    is_ask = models.BooleanField(verbose_name='is ask', default=False)
    is_show = models.BooleanField(verbose_name='is show', default=True)
    points = models.IntegerField(verbose_name='points', blank=True)
    num_comments = models.IntegerField(verbose_name='num comments', blank=True)
    left = models.IntegerField(verbose_name='left', blank=True, null=True)
    right = models.IntegerField(verbose_name='right', blank=True, null=True)
    tree_id = models.IntegerField(verbose_name='tree id', blank=True, null=True)
    level = models.IntegerField(verbose_name='level', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)
    indexes = [
        models.Index(fields=['points', 'created_at']),
        models.Index(fields=['id', 'created_at']),
        models.Index(fields=['created_at', 'id'])
    ]

    def __str__(self):
        return f'{self.user} {self.up_votes} {self.down_votes}'


class NewsVote(models.Model):
    item = models.ForeignKey(to=NewsItem, on_delete=models.CASCADE)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(verbose_name='vote')
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.item}  {self.user} {self.vote}'


class NewsStory(models.Model):
    item_ptr = models.OneToOneField(primary_key=True, to=NewsItem, on_delete=models.CASCADE)
    # duplicate_of = models.ForeignKey(to='self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='title', max_length=32)
    text = models.TextField(verbose_name='text', blank=True)
    url = models.CharField(verbose_name='url', max_length=50, blank=True, null=True)
    do_mail = models.CharField(verbose_name='do main', max_length=32, blank=True, null=True)
    indexes = [
        models.Index(fields=['do_mail', 'duplicate_of'])
    ]

    def __str__(self):
        return f'{self.item_ptr} {self.title}'


class NewsComment(models.Model):
    item_ptr = models.OneToOneField(primary_key=True, to=NewsItem, on_delete=models.CASCADE)
    to_story = models.ForeignKey(to=NewsStory, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='text')

    def __str__(self):
        return f'{self.item_ptr} {self.to_story} {self.text}'


class EmailDigestSubscription(models.Model):
    frequency = models.CharField(verbose_name='frequency', max_length=42)
    weekly_weekday = models.CharField(verbose_name='weekly weekday', max_length=32, blank=True, null=True)
    verified_email = models.CharField(verbose_name='verified email', max_length=32, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.frequency}'


class EmailDigestEmailDigest(models.Model):
    frequency = models.CharField(verbose_name='frequency', max_length=32)
    weekly_weekday = models.CharField(verbose_name='weekly weekday', max_length=32, blank=True)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.frequency} {self.weekly_weekday}'


class EmailDigestUnsubscription(models.Model):
    from_digest = models.ForeignKey(to=EmailDigestEmailDigest, on_delete=models.CASCADE, blank=True, null=True)
    subscription = models.ForeignKey(to=EmailDigestSubscription, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.from_digest} {self.subscription}'


class EmailDigestEmailDigestStories(models.Model):
    email_digest = models.ForeignKey(to=EmailDigestEmailDigest, on_delete=models.CASCADE)
    story = models.ForeignKey(to=NewsStory, on_delete=models.CASCADE)
    # Indexes = [
    #     models.Index(['story', 'email_digest'])
    # ]

    def __str__(self):
        return f'{self.email_digest}  {self.story}'


class EmailDigestUserSubscription(models.Model):
    subscription = models.OneToOneField(to=EmailDigestSubscription, primary_key=True, on_delete=models.CASCADE)
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscription}  {self.user}'


class EmailDigestAnonymousSubscription(models.Model):
    subscription_ptr = models.OneToOneField(to=EmailDigestSubscription, on_delete=models.CASCADE, primary_key=True)
    logged_in_user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(verbose_name='verified', default=False)
    verified_at = models.DateTimeField(verbose_name='verified at', blank=True, null=True)
    verified_code = models.CharField(verbose_name='verified code', max_length=21)
    email = models.CharField(verbose_name='email', max_length=32, blank=True)

    def __str__(self):
        return {self.verified}


class AccountsEmailVerification(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified = models.BooleanField(verbose_name='verified', default=False)
    verified_at = models.DateTimeField(verbose_name='verified at', blank=True, null=True)
    verification_code = models.CharField(verbose_name='verification code', max_length=32)
    email = models.CharField(verbose_name='email', max_length=32)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.user}  {self.verified}'


class AccountPasswordResetRequest(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    verified_code = models.CharField(verbose_name='verified code', max_length=32)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='changed at', auto_now=True)

    def __str__(self):
        return f'{self.user}  {self.verified_code}'


class DjangoContentType(models.Model):
    app_label = models.CharField(verbose_name='app label', max_length=32)
    model = models.CharField(verbose_name='model', max_length=32)
    # indexes = [
    #     models.Index(['model', 'app_label'])
    # ]

    def __str__(self):
        return f'{self.app_label}  {self.model}'


class AuthPermission(models.Model):
    custom_user = models.ManyToManyField(to=AccountCustomUser)
    content_type = models.ForeignKey(to=DjangoContentType, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='name', max_length=32)
    codename = models.CharField(verbose_name='code name', max_length=32)
    # indexes = [
    #     models.Index([content_type, name])
    # ]

    def __str__(self):
        return f'{self.content_type}  {self.name}'


class AuthGroup(models.Model):
    name = models.CharField(verbose_name='name', max_length=32)
    permission = models.ManyToManyField(to=AuthPermission)
    custom_user = models.ManyToManyField(to=AccountCustomUser)

    def __str__(self):
        return self.name


class DjangoAdminLog(models.Model):
    user = models.ForeignKey(to=AccountCustomUser, on_delete=models.CASCADE)
    content_type = models.ForeignKey(to=DjangoContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_repr = models.CharField(verbose_name='object repr', max_length=32)
    change_message = models.TextField(verbose_name='change message')
    object_id = models.TextField(verbose_name='object id', blank=True, null=True)
    action_flag = models.SmallIntegerField(verbose_name='action flag')
    action_time = models.DateTimeField(verbose_name='action time', blank=True, null=True)

    def __str__(self):
        return f'{self.user}  {self.object_repr}'
