# from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter

from apps.business_app.views.brand import BrandViewSet
from apps.business_app.views.car import CarViewSet
from apps.business_app.views.driver import DriverViewSet
from apps.business_app.views.gallery_picture import GalleryPictureViewSet
from apps.business_app.views.model import ModelViewSet


router = ExtendedSimpleRouter()
router.register(
    "brands",
    BrandViewSet,
    basename="brands",
)

router.register(
    "models",
    ModelViewSet,
    basename="models",
)
router.register(
    "gallery-picture",
    GalleryPictureViewSet,
    basename="gallery-picture",
)
router.register(
    "drivers",
    DriverViewSet,
    basename="drivers",
)
router.register(
    "cars",
    CarViewSet,
    basename="cars",
)
urlpatterns = [
    # path("markers/delete/<int:marker_id>/", delete_marker, name="delete_marker"),
]

urlpatterns += router.urls
