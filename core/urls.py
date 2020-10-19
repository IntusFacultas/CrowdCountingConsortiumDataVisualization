from django.urls import path
from core.views import MainView, DataPointsApiView, ViewConfig
app_name = "core"
urlpatterns = [
    path("api/data-points", DataPointsApiView.as_view(), name="data-points"),
    path("api/config", ViewConfig.as_view(), name="config"),
    path("", MainView.as_view(), name="main")
]
