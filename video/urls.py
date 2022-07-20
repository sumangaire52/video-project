from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from django.urls import path, include
from .views import  VideoViewset, CostingView

router = DefaultRouter()
router.register(r'videos', VideoViewset, basename="videos")

urlpatterns = [ 
    path('', include(router.urls)),
    path('calculate_cost/', CostingView.as_view()),
    path('docs/', include_docs_urls(title = "Video API")),
    path('schema/', get_schema_view(title = "Video Schema")),
]