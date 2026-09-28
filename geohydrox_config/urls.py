from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from watersheds.views import WatershedViewSet, HealthScoreViewSet
from assets.views import AssetViewSet
from field_reports.views import FieldReportViewSet
from imagery.views import SatelliteSceneViewSet

router = DefaultRouter()
router.register(r"watersheds", WatershedViewSet)
router.register(r"health-scores", HealthScoreViewSet)
router.register(r"assets", AssetViewSet)
router.register(r"field-reports", FieldReportViewSet)
router.register(r"satellite-scenes", SatelliteSceneViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/", include(router.urls)),
]