from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

class AddPropertyView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = '../templates/add_property.html'

    def get(self, request):
        # queryset = Profile.objects.all()
        return Response({'profiles': "there"})




