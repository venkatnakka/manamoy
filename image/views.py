from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from rest_framework.response import Response
from .serializers import *
# Create your views here.


class Image_upload(ListCreateAPIView):
    serializer_class = ImageUploadSerializer
    queryset = Image.objects.all()

class ImageView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ImageUploadSerializer
    queryset = Image.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if (PageView.objects.count() <= 0):
            x = PageView.objects.create()
            x.save()
        else:
            x = PageView.objects.all()[0]
            x.hits = x.hits + 1
            x.save()
        print(x.hits)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def home(request):
    if (PageView.objects.count() <= 0):
        x = PageView.objects.create()
        x.save()
    else:
        x = PageView.objects.all()[0]
        x.hits = x.hits + 1
        x.save()
    print(x.hits)
    context = {'page':x.hits}
    return render(request,'home.html',context=context)