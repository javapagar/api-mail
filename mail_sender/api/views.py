from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.mail import send_mail

import json

class EmailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(Self, request):
        request_json = json.loads(request.body.decode('utf-8'))
        #TODO: serialize
        fields = ['name','to_email','subject','message']
        for field in fields:
            if not field in request_json.keys():
                return Response({"error": f"Param '{field}' not found"}, 
                                status=status.HTTP_400_BAD_REQUEST) 

        try:
            name = request_json['name']
            to_email = request_json['to_email']
            from_email = request_json['from_email']
            subject = request_json['subject']
            message = f"""From {from_email} of {name}:\n\n{request_json['message']}"""
            send_mail(subject=subject, 
                      message=message, 
                      from_email=None, 
                      recipient_list=[to_email])
            return Response({'message': "Mail sended"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"error sending email:{e}"}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
