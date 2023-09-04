from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from .serializers import *


def find(model, pk):
    try:
        r = model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise Http404
    return r


class AccountCustomUserListView(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        accounts = AccountCustomUser.objects.all()
        serializer = AccountCustomUserListSerializer(accounts, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountCustomUserDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response


class AccountCustomUserDetailView(APIView):

    def get(self, request, pk):
        account = find(AccountCustomUser, pk)
        serializer = AccountCustomUserDetailSerializer(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        account = find(AccountCustomUser, pk)
        serializer = AccountCustomUserDetailSerializer(instance=account, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = find(AccountCustomUser, pk)
        account.delete()
        return Response(data={'detail': 'The user deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class AccountsInvitationListView(APIView):

    def get(self, request):
        invitations = AccountsInvitation.objects.all()
        serializer = AccountsInvitationListSerializer(invitations, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountsInvitationDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsInvitationDetailView(APIView):

    def get(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        serializer = AccountsInvitationDetailSerializer(invitation)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        serializer = AccountsInvitationDetailSerializer(instance=invitation, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        invitation = find(AccountsInvitation, pk)
        invitation.delete()
        return Response(data={'detail': 'The invitation deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class NewsItemListView(APIView):

    def get(self, request):
        newsItems = NewsItem.objects.all()
        serializer = NewsItemListSerializer(newsItems, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsItemDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsItemDetailView(APIView):

    def get(self, request, pk):
        newsItem = find(NewsItem, pk)
        serializer = NewsItemDetailSerializer(newsItem)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsItem = find(NewsItem, pk)
        serializer = NewsItemDetailSerializer(newsItem, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsItem = find(NewsItem, pk)
        newsItem.delete()
        return Response(data={'detail': 'The news item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsStoryListView(APIView):

    def get(self, request):
        newsStories = NewsStory.objects.all()
        serializer = NewsStoryListSerializer(newsStories, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsStoryDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsStoryDetailView(APIView):

    def get(self, request, pk):
        newsStory = find(NewsStory, pk)
        serializer = NewsStoryDetailSerializer(newsStory)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsStory = find(NewsStory, pk)
        serializer = NewsStoryDetailSerializer(instance=newsStory, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsStory = find(NewsStory, pk)
        newsStory.delete()
        return Response(data={'detail': 'The news story deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsVoteListView(APIView):

    def get(self, request):
        newsVote = NewsVote.objects.all()
        serializer = NewsVoteListSerializer(newsVote, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsVoteDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsVoteDetailView(APIView):

    def get(self, request, pk):
        newsVote = find(NewsVote, pk)
        serializer = NewsVoteDetailSerializer(newsVote)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsVote = find(NewsVote, pk)
        serializer = NewsVoteDetailSerializer(instance=newsVote, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        newsVote = find(NewsVote, pk)
        newsVote.delete()
        return Response(data={'detail': 'The news vote deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class NewsCommentListView(APIView):

    def get(self, request):
        newsComments = NewsComment.objects.all()
        serializer = NewsCommentListSerializer(newsComments, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsCommentDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsCommentDetailView(APIView):

    def get(self, request, pk):
        newsComment = find(NewsComment, pk)
        serializer = NewsCommentDetailSerializer(newsComment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        newsComment = find(NewsComment, pk)
        serializer = NewsCommentDetailSerializer(instance=newsComment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request, pk):
        newsComment = find(NewsComment, pk)
        newsComment.delete()
        return Response(data={'detail': 'The news comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class EmailDigestSubscriptionListView(APIView):

    def get(self, request):
        emailDigestSubscriptions = EmailDigestSubscription.objects.all()
        serializer = EmailDigestSubscriptionListSerializer(emailDigestSubscriptions, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestSubscriptionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        serializer = EmailDigestSubscriptionDetailSerializer(emailDigestSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        serializer = EmailDigestSubscriptionDetailSerializer(instance=emailDigestSubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestSubscription = find(EmailDigestSubscription, pk)
        emailDigestSubscription.delete()
        return Response(data={'detail': 'The email digest subscription deleted successfully.'})


class EmailDigestEmailDigestListView(APIView):

    def get(self, request):
        emailDigestEmailDigest = EmailDigestEmailDigest.objects.all()
        serializer = EmailDigestEmailDigestSerializer(emailDigestEmailDigest, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestEmailDigestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestEmailDigestDetailView(APIView):

    def get(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        serializer = EmailDigestEmailDigestSerializer(emailDigestEmailDigest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        serializer = EmailDigestEmailDigestSerializer(instance=emailDigestEmailDigest, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestEmailDigest = find(EmailDigestEmailDigest, pk)
        emailDigestEmailDigest.delete()
        return Response(data={'detail': 'The digest email deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class EmailDigestUnsubscriptionListView(APIView):

    def get(self, request):
        emailDigestUnSubscription = EmailDigestUnsubscription.objects.all()
        serializer = EmailDigestUnsubscriptionSerializer(emailDigestUnSubscription, many=True,
                                                         context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestUnsubscriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestUnsubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        serializer = EmailDigestUnsubscriptionSerializer(emailDigestUnsubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        serializer = EmailDigestUnsubscriptionSerializer(instance=emailDigestUnsubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestUnsubscription = find(EmailDigestUnsubscription, pk)
        emailDigestUnsubscription.delete()
        return Response(data={'detail': 'The email digest unSubscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class EmailDigestEmailDigestStoriesListView(APIView):

    def get(self, request):
        emailDigestEmailDigestStories = EmailDigestEmailDigestStories.objects.all()
        serializer = EmailDigestEmailDigestStoriesSerializer(emailDigestEmailDigestStories, many=True,
                                                             context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestEmailDigestStoriesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestEmailDigestStoriesDetailView(APIView):

    def get(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        serializer = EmailDigestEmailDigestStoriesSerializer(emailDigestEmailDigestStories)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        serializer = EmailDigestEmailDigestStoriesSerializer(instance=emailDigestEmailDigestStories, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestEmailDigestStories = find(EmailDigestEmailDigestStories, pk)
        emailDigestEmailDigestStories.delete()
        return Response(data={'detail': 'The email digest Story deleted successfully.'})


class EmailDigestUserSubscriptionListView(APIView):

    def get(self, request):
        emailDigestUserSubscription = EmailDigestUserSubscription.objects.all()
        serializer = EmailDigestUserSubscriptionSerializer(emailDigestUserSubscription, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestUserSubscriptionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestUserSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        serializer = EmailDigestUserSubscriptionSerializer(emailDigestUserSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        serializer = EmailDigestUserSubscriptionSerializer(instance=emailDigestUserSubscription, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestUserSubscription = find(EmailDigestUserSubscription, pk)
        emailDigestUserSubscription.delete()
        return Response(data={'detail': ' The email digest user subscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class EmailDigestAnonymousSubscriptionListView(APIView):

    def get(self, request):
        emailDigestAnonymousSubscription = EmailDigestAnonymousSubscription.objects.all()
        serializer = EmailDigestAnonymousSubscriptionListSerializer(emailDigestAnonymousSubscription, many=True,
                                                                    context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailDigestAnonymousSubscriptionDetailView(APIView):

    def get(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(emailDigestAnonymousSubscription)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        serializer = EmailDigestAnonymousSubscriptionDetailSerializer(instance=emailDigestAnonymousSubscription,
                                                                      data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emailDigestAnonymousSubscription = find(EmailDigestAnonymousSubscription, pk)
        emailDigestAnonymousSubscription.delete()
        return Response(data={'detail': 'The email digest anonymous subscription deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class AccountsEmailVerificationListView(APIView):

    def get(self, request):
        accountsEmailVerification = AccountsEmailVerification.objects.all()
        serializer = AccountsEmailVerificationListSerializer(accountsEmailVerification, many=True,
                                                             context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountsEmailVerificationDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsEmailVerificationDetailView(APIView):

    def get(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        serializer = AccountsEmailVerificationDetailSerializer(accountsEmailVerification)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        serializer = AccountsEmailVerificationDetailSerializer(instance=accountsEmailVerification, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        accountsEmailVerification = find(AccountsEmailVerification, pk)
        accountsEmailVerification.delete()
        return Response(data={'detail': 'The account Email verification deleted successfully.'},
                        status=status.HTTP_205_RESET_CONTENT)


class AccountPasswordResetRequestListView(APIView):

    def get(self, request):
        accountPasswordResetRequest = AccountPasswordResetRequest.objects.all()
        serializer = AccountPasswordResetRequestSerializer(accountPasswordResetRequest, many=True,
                                                           context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AccountPasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountPasswordResetRequestDetailView(APIView):

    def get(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        serializer = AccountPasswordResetRequestSerializer(accountPasswordResetRequest)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        serializer = AccountPasswordResetRequestSerializer(instance=accountPasswordResetRequest, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        accountPasswordResetRequest = find(AccountPasswordResetRequest, pk)
        accountPasswordResetRequest.delete()
        return Response(data={'detail': 'The account password rest request deleted successfully.'},
                        status=status.HTTP_205_RESET_CONTENT)


class DjangoContentTypeListView(APIView):

    def get(self, request):
        djangoContentType = DjangoContentType.objects.all()
        serializer = DjangoContentTypeSerializer(djangoContentType, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DjangoContentTypeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DjangoContentTypeDetailView(APIView):

    def get(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        serializer = DjangoContentTypeSerializer(djangoContentType)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        serializer = DjangoContentTypeSerializer(instance=djangoContentType, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        djangoContentType = find(DjangoContentType, pk)
        djangoContentType.delete()
        return Response(data={'detail': 'The django content type deleted successfully.'},
                        status=status.HTTP_204_NO_CONTENT)


class AuthPermissionListView(APIView):

    def get(self, request):
        authPermission = AuthPermission.objects.all()
        serializer = AuthPermissionListSerializer(authPermission, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthPermissionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthPermissionDetailView(APIView):

    def get(self, request, pk):
        authPermission = find(AuthPermission, pk)
        serializer = AuthPermissionDetailSerializer(authPermission)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        authPermission = find(AuthPermission, pk)
        serializer = AuthPermissionDetailSerializer(instance=authPermission, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        authPermission = find(AuthPermission, pk)
        authPermission.delete()
        return Response(data={'detail': 'The auth permission deleted successfully.'})


class AuthGroupListView(APIView):

    def get(self, request):
        authGroup = AuthGroup.objects.all()
        serializer = AuthGroupSerializer(authGroup, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthGroupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthGroupDetailView(APIView):

    def get(self, request, pk):
        authGroup = find(AuthGroup, pk)
        serializer = AuthGroupSerializer(authGroup)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        authGroup = find(AuthGroup, pk)
        serializer = AuthGroupSerializer(instance=authGroup, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        authGroup = find(AuthGroup, pk)
        authGroup.delete()
        return Response(data={'detail': 'the auth group deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class DjangoAdminLogListView(APIView):

    def get(self, request):
        djangoAdminLog = DjangoAdminLog.objects.all()
        serializer = DjangoAdminLogListSerializer(djangoAdminLog, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DjangoAdminLogDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DjangoAdminLogDetailView(APIView):

    def get(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        serializer = DjangoAdminLogDetailSerializer(djangoAdminLog)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        serializer = DjangoAdminLogDetailSerializer(instance=djangoAdminLog, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        djangoAdminLog = find(DjangoAdminLog, pk)
        djangoAdminLog.delete()
        return Response(data={'detail': 'The django admin log deleted successfully.'})
