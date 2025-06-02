from rest_framework.views import APIView
from rest_framework.response import Response
from products.serializers import ProductSerializer
from products.models import Product

class ProductView(APIView):

    def get(self, request):
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.body
        serializer = ProductSerializer(data=data)
        return Response(serializer.data)