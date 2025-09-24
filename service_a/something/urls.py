from django.urls import path


from something.views import SomethingListCreateAPIView


urlpatterns = [
    path("something/", SomethingListCreateAPIView.as_view(), name="something-list-create"),
]
