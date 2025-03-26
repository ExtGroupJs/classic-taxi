from rest_framework import routers


router = routers.DefaultRouter()
# router.register(r"users", UserViewSet, basename="users")
# router.register(r"countries", CountryViewSet, basename="countries")

urlpatterns = []

urlpatterns += router.urls
