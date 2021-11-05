from .models import Image
from . import utils
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
import random


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    http_method_names = ['get']

    def list(self, request):
        if request.query_params.get('id', None) is not None:
            queryset = Image.objects.all()
            image = get_object_or_404(queryset, pk=request.query_params['id'])
            scale=1
            if request.query_params.get('scale', None) is not None:
                try:
                    scale = float(request.query_params['scale'])
                    if image.image.width*scale < 1 or image.image.width*scale > 20000 or \
                    image.image.height*scale < 1 or image.image.height*scale > 20000:
                        raise ValueError('') 
                except ValueError as e:
                    return Response({'details': "scale parametr is not float or scaled image is out of size borders"}, status=404)
                return Response({'image': "{}".format(request.build_absolute_uri(utils.scale_image(image, scale)))})
            return Response({'image': "{}".format(request.build_absolute_uri(image.image.url))})
        else:
            queryset = Image.objects.all()
            resp = []
            for item in queryset:
                resp.append({'id':item.id,
                            'image':request.build_absolute_uri(item.image.url)})
            return Response(resp)

    def retrieve(self, request, pk=None):
            queryset = Image.objects.all()
            image = get_object_or_404(queryset, pk=pk)
            serializer = ImageSerializer(image)
            return Response({'image': "{}".format(request.build_absolute_uri(image.image.url))})

class ImageUpload(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        print(request.data['image'])
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = Image(image=request.data['image'])
            id = None
            queryset = Image.objects.all()
            for exist_image in queryset:
                if utils.get_diff(image, exist_image) < 0.14:
                    if image.image.height > exist_image.image.height:
                        exist_image.image = image.image
                        exist_image.save()
                    id = exist_image.id
                    break
            else:
                print(image.image.name)
                image.image.name = str(random.randint(1000000, 99999999999))+'.jpg'
                image.save()
                id = image.id
            return Response({'id': id}, status=200)
        else:
            return Response(status=404)
       
