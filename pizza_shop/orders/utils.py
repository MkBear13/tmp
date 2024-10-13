from django.core.mail import send_mail
from django.conf import settings

def send_order_ready_email(order):
    subject = 'Ваш заказ готов'
    message = f'Здравствуйте, {order.customer.username}! Ваш заказ #{order.id} готов к получению.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [order.customer.email]
    send_mail(subject, message, email_from, recipient_list)