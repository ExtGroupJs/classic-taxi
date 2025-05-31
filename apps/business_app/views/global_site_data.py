from apps.business_app.models.global_site_data import GlobalSiteData
from rest_framework.decorators import action


from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from rest_framework.viewsets import GenericViewSet


class GlobalSiteDataViewSet(GenericViewSet):
    queryset = GlobalSiteData.objects.all()
    permission_classes = [AllowAny]

    def get_object(self):
        return GlobalSiteData.get_solo()

    @action(
        methods=["get"],
        detail=False,
        url_name="get-visitors-counter",
        url_path="get-visitors-counter",
    )
    def get_visitors_counter(
        self,
        request,
    ):
        instance = self.get_object()
        return Response({"visitors_counter": instance.visitors_counter})

    @action(
        methods=["post"],
        detail=False,
        url_name="update-visitors-counter",
        url_path="update-visitors-counter",
    )
    def update_visitors_counter(
        self,
        request,
    ):
        instance = self.get_object()
        instance.visitors_counter += 1
        instance.save()
        return Response({"visitors_counter": instance.visitors_counter})
