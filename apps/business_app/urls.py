# from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter


router = ExtendedSimpleRouter()
# router.register(
# "allowed-extensions",
# AllowedExtensionsViewSet,
# basename="allowed-extensions",
# )
urlpatterns = [
    # path("markers/delete/<int:marker_id>/", delete_marker, name="delete_marker"),
]

urlpatterns += router.urls
