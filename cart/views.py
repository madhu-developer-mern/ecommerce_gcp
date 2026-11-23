from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class CartInfoView(APIView):
    """Informational endpoint confirming client-side cart handling."""
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "message": "Cart is managed client-side using React Context and localStorage for fast UX and stateless cloud deployment."
        })
