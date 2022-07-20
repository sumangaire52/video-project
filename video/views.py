from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer, CostingSerializer

class VideoViewset(viewsets.ModelViewSet):

    serializer_class = VideoSerializer

    def get_queryset(self):
        start_size =  self.request.query_params.get('start_size') # expects the size in MB
        end_size = self.request.query_params.get('end_size') # expects the size in MB
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        queryset = Video.objects.all()
        if start_size and end_size:
            queryset = (video for video in Video.objects.all() if float(start_size) <= video.size <= float(end_size) )
        
        if start_date and end_date:
            queryset = Video.objects.filter(created_date__range = [start_date, end_date])

        return queryset

class CostingView(APIView):
    
    def post(self, request):
        serializer = CostingSerializer(data = request.POST)
        if serializer.is_valid():
            if serializer.data['size'] <= 500:
                total_cost = 5
            else:
                total_cost = 12.5

            if serializer.data['duration'] <= 378:
                total_cost += 12.5    
            else:
                total_cost += 20

            return Response({'Total Cost' : total_cost})

        else:
            return Response(serializer.errors)