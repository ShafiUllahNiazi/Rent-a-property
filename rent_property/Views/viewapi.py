
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class Home_page_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/index.html'

    def get(self, request):
        
        return Response({'profiles': 'abc'})
    
class add_property (APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        
        return Response({'profiles': 'abc'})
    
class contact (APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/contact.html'

    def get(self, request):
        
        return Response({'profiles': 'abc'})
class add_property_data (APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        
        return Response({'profiles': 'abc'})