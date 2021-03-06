from django.core.mail import send_mail
from rest_framework import permissions


def send_activation_email(user):
    subject = 'Site registering'
    body = f'Activate code: http://localhost:8000/account/activate/{user.activation_code}/'
    from_email = 'shop@mail.com'
    recipients = [user.email]
    send_mail(subject=subject, message=body, from_email=from_email, recipient_list=recipients, fail_silently=False)


class IsOwnerAccount(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.username == request.user.username or bool(request.user and request.user.is_superuser)
