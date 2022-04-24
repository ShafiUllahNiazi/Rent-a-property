from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rent_property.Serializers.AppartmentSerializer import ApartmentSerializer
from rent_property.models import Apartment


class Home_page_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/index.html'

    def get(self, request):
        try:
            info_set = Apartment.objects.all()[:6]
            serializer = ApartmentSerializer(info_set, many=True)

            return Response({'data': serializer.data}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)


class add_property(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        return Response({'profiles': 'abc'})


class contact(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/contact.html'

    def get(self, request):
        return Response({'profiles': 'abc'})


class add_property_data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        return Response({'profiles': 'abc'})


class show_apartments(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/show_apartments.html'

    def get(self, request):
        try:
            info_set = Apartment.objects.all()
            serializer = ApartmentSerializer(info_set, many=True)

            return Response({'data': serializer.data}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

class edit_apartment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/edit_apartment.html'

    def get(self, request, pk):
        try:
            apartment_info = Apartment.objects.get(id=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = ApartmentSerializer(apartment_info)
        return Response({'data': serializer.data}, status=200)


class del_apartment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/show_apartments.html'

    def get(self, request, pk):
        if pk is not None:
            try:
                apartment_info = Apartment.objects.get(id=pk)
                apartment_info.delete()
            except Exception as e:
                return Response({"detail": str(e)}, status=422)
        else:
            return Response({"detail": "Apartment ID not found in request"}, status=422)

        return Response({"detail": "Deleted Apartment Successfully!"}, status=200)



class details_apartment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/speciefic.html'

    def get(self, request, pk):
        try:
            apartment_info = Apartment.objects.get(id=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = ApartmentSerializer(apartment_info)
        return Response({'data': serializer.data}, status=200)