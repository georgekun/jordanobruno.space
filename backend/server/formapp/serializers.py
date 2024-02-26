from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ['sender_ip','created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'META'):
            sender_ip = request.META.get('REMOTE_ADDR')
            self.__check_matches(sender_ip)
            validated_data['sender_ip'] = sender_ip
        return super().create(validated_data)


    def __check_matches(self, sender_ip):
        application_exists = Application.objects.filter(
                sender_ip=sender_ip
        ).first()

        if application_exists:
            raise ValueError("Вы уже отправляли заявку! Ожидайте ответа.")
