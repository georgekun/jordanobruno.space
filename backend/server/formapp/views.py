from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Application
from .serializers import ApplicationSerializer


class ApplicationView(generics.CreateAPIView):
    """ Ендпоинт для получения новых заявок """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
     
    def create(self, request, *args, **kwargs):
        try:   
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"msg":"Контактые данные получены, ожидайте ответа!"},
                            status=status.HTTP_201_CREATED,
                            headers=headers)
            
        except ValueError as e:
            return Response({"msg":str(e)}, status.HTTP_400_BAD_REQUEST)
        

