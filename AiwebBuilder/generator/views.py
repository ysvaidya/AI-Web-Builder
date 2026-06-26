from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)

from django.http import HttpResponse

from .forms import BusinessForm
from .models import (
    Business, 
    GeneratedWebsite
)

from django.http import JsonResponse

from .services.ai_generator import (
    # test_gemini,
    generate_website_content_ai
)
from .services.website_generator import(
    generate_website_content
)

import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_business(request):

    if request.method == "POST":

        form = BusinessForm(request.POST)

        if form.is_valid():

            business = form.save()

            return redirect(
                "business_details",
                business_id = business.id
            )
    else:
        form = BusinessForm()

    return render (
        request,
        "generator/create-business.html",
        {"form":form}

    )


def business_details(request, business_id):

    business =get_object_or_404(
        Business,
        id = business_id
    )

    return render(
        request,
        "generator/business_detail.html",
        {"business": business}
    )



def generate_website(request, business_id):

    business = get_object_or_404(
        Business,
        id=business_id
    )

    existing_website = GeneratedWebsite.objects.filter(
        business = business
    ).first()

    if existing_website:
        return redirect(
            "website_preview",
            website_id = existing_website.id
        )

    website_data = generate_website_content(
        business
    )

    generated_website = GeneratedWebsite.objects.create(
        business=business,

        hero_title=website_data["hero_title"],

        hero_subtitle=website_data["hero_subtitle"],

        about_text=website_data["about_text"],

        services=website_data["services"],

        faqs=website_data["faqs"],

        testimonials=website_data["testimonials"],

        pricing_plans=website_data["pricing_plans"],

        seo_title=website_data["seo_title"],

        seo_description=website_data["seo_description"],

        selected_template=business.business_type
    )

    return redirect(
        "website_preview",
        website_id = generated_website.id
    )
    


def website_preview(request, website_id):

    website = get_object_or_404(
        GeneratedWebsite,
        id = website_id
    )

    return render(
        request,
        "generator/website_preview.html",
        {
            "website": website
        }
    )


def test_ai(request):

    business = Business.objects.first()

    data = generate_website_content_ai(
        business
    )

    return JsonResponse(data)
