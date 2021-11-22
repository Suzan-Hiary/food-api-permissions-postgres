from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .seralizers import FoodSerializer
from .models import Food
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class Foodviewset(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Food.objects.all()
    serializer_class= FoodSerializer

class FoodDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    
    queryset = Food.objects.all()
    serializer_class= FoodSerializer