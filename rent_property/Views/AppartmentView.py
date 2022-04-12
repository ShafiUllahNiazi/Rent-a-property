
from rent_property.models import Apartment
from rent_property.Serializers.AppartmentSerializer import ApartmentSerializer
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rent_a_property.pagination import StandardResultSetPagination


class ApartmentListView(ListAPIView):
    serializer_class = ApartmentSerializer
    pagination_class = StandardResultSetPagination

    def get_queryset(self):
        try:
            queryset = Apartment.objects.all()

        except Exception as e:
            print(e)
            return Response({"detail": "record not found!"}, status=422)

        return queryset


class ApartmentView(APIView):
    def post(self, request):
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=422)


class ApartmrntDetailedView(APIView):
    def get(self, request, pk):
        try:
            apartment_info = Apartment.objects.get(id=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = ApartmentSerializer(apartment_info)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            apartment_info = Apartment.objects.filter(id=pk).first()
        except Exception as e:
            return Response({"detail": "Id not found in data!"}, status=422)

        request_data = request.data
        serializer = ApartmentSerializer(apartment_info, data=request_data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=422)

    def delete(self, request, pk):
        if pk is not None:
            try:
                apartment_info = Apartment.objects.get(id=pk)
                apartment_info.delete()
            except Exception as e:
                return Response({"detail": str(e)}, status=422)
        else:
            return Response({"detail": "Apartment ID not found in request"}, status=422)

        return Response({"detail": "Deleted Job Successfully!"}, status=200)
