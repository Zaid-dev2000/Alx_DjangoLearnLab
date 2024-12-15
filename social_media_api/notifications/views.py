# notifications/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from django.shortcuts import get_object_or_404
from rest_framework import status

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get unread notifications for the current user
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        notification_data = [{
            'actor': notification.actor.username,
            'verb': notification.verb,
            'target': str(notification.target),
            'timestamp': notification.timestamp,
        } for notification in notifications]

        return Response(notification_data, status=status.HTTP_200_OK)

class MarkNotificationReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return Response({'detail': 'Notification marked as read'}, status=status.HTTP_200_OK)
