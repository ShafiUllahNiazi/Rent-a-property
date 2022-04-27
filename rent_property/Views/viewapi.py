from django.http import HttpResponseRedirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rent_property.Serializers.AppartmentSerializer import ApartmentSerializer
from rent_property.Serializers.ContactUsSerializer import ContactUsSerializer
from rent_property.Serializers.ApartmentImagesSerializer import ApartmentImagesSerializer
from rent_property.models import Apartment, ContactUs,ApartmentImages
from django.db.models.functions import Lower


class Home_page_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/index.html'

    def get(self, request):
        try:
            info_set = Apartment.objects.all()
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
        try:
            contact = ContactUs.objects.first()
            if(contact):
                serializer = ContactUsSerializer(contact,)
                print ("aaaaaaaaaaaa")
                print (serializer.data)
            else:
                serializer = None
            return Response({'data': serializer.data}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)


class add_property_data(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        return Response({'profiles': 'abc'})


class show_contact(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/show_contact.html'

    def get(self, request):
        query_set = ContactUs.objects.first()
        if not query_set:

            return Response({}, status=200)

        serializer = ContactUsSerializer(query_set)

        return Response({'data': serializer.data})


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


class show_apartments1(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/sellproperty.html'

    def get(self, request,pk):
        try:
            data=request.POST
            
            print (data)
            info_set = Apartment.objects.filter(property_status=pk)
            serializer = ApartmentSerializer(info_set, many=True)

            return Response({'data': serializer.data}, status=200)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)


class city_apartment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/city_apartment.html'

    def get(self, request, pk):
        try:
            pk = pk.lower()

            Apartment.objects.update(city=Lower('city'))
            info_set = Apartment.objects.all().filter(city=pk)

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
        # return HttpResponseRedirect(redirect_to='/app/show_apartments')

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
        return HttpResponseRedirect(redirect_to='/app/show_apartments')
        # return Response({"detail": "Deleted Apartment Successfully!"}, status=200)



class details_apartment(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/speciefic.html'

    def get(self, request, pk):
        contact = ContactUs.objects.first()
        if(contact):
            conserializer = ContactUsSerializer(contact)
            
        else:
            conserializer = None
            
        imagelist = ApartmentImages.objects.filter(apartment_id=pk)

        if(imagelist):
            imgserializer = ApartmentImagesSerializer(imagelist,many=True)
            
            
            
        else:
            imgserializer = None
        
        try:
            apartment_info = Apartment.objects.get(id=pk)
        except Exception as e:
            return Response({"detail": str(e)}, status=422)

        serializer = ApartmentSerializer(apartment_info)
        if conserializer is not None:
            print(imgserializer.data)

            return Response({'data': serializer.data,'condata':conserializer.data,'imgdata':imgserializer.data}, status=200)
        else:
            return Response({'data': serializer.data,'condata':{"No contact Data Found"},'imgdata':imgserializer.data}, status=200)


