
from rent_property.models import ContactUs
from rent_property.Serializers.ContactUsSerializer import ContactUsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ContactUsView(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=422)


class ContactUsDetailedView(APIView):
    def get(self, request, pk):
        try:
            appartment_info = ContactUs.objects.get(id=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = ContactUsSerializer(appartment_info)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            contact_info = ContactUs.objects.filter(id=pk).first()
        except Exception as e:
            print(e)
            return Response({"detail": "Id not found in data!"}, status=422)

        request_data = request.data

        serializer = ContactUsSerializer(contact_info, data=request_data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=422)

    def delete(self, request, pk):
        if pk is not None:
            try:
                apartment_info = ContactUs.objects.get(id=pk)
                apartment_info.delete()
            except Exception as e:
                return Response({"detail": str(e)}, status=422)
        else:
            return Response({"detail": "Contact ID not found in request"}, status=422)

        return Response({"detail": "Deleted Job Successfully!"}, status=200)
