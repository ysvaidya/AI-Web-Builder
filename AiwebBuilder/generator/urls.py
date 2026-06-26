from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path(
        "create-business/", 
        views.create_business, 
        name = "create-business"
    ),

    path(
        "business/<int:business_id>/",
        views.business_details,
        name = "business_details"
    ),

    path(
        "generate-website/<int:business_id>/",
        views.generate_website,
        name="generate_website"
    ),

    path(
        "website/<int:website_id>/",
        views.website_preview,
        name = "website_preview"
    ),

    path(
        "test-ai/",
        views.test_ai,
        name="test_ai"
    ),


] 