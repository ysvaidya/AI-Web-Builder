from django.db import models


class Business(models.Model):

    BUSINESS_TYPES = [
        ("GYM", "Gym"),
        ("RESTAURANT", "Restaurant"),
        ("CAFE", "Cafe"),
        ("SALON", "Salon"),
        ("AGENCY", "Agency"),
        ("PORTFOLIO", "Portfolio"),
        ("LAWYER", "Lawyer"),
        ("DOCTOR", "Doctor"),
        ("REAL_ESTATE", "Real Estate"),
    ]

    business_name = models.CharField(max_length=255)

    business_type = models.CharField(
        max_length=20,
        choices=BUSINESS_TYPES
    )

    description = models.TextField()

    location = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    primary_color = models.CharField(
        max_length=7,
        default="#000000"
    )

    secondary_color = models.CharField(
        max_length=7,
        default="#FFFFFF"
    )

    target_audience = models.CharField(
        max_length=255,
        blank=True
    )

    include_testimonials = models.BooleanField(
        default=True
    )

    include_pricing = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.business_name
    


class GeneratedWebsite(models.Model):

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name="generated_websites"
    )

    hero_title = models.CharField(
        max_length=255
    )

    hero_subtitle = models.TextField()

    about_text = models.TextField()

    services = models.JSONField(
        default=list
    )

    faqs = models.JSONField(
        default=list,
        blank=True
    )

    testimonials = models.JSONField(
        default=list,
        blank=True
    )

    pricing_plans = models.JSONField(
        default=list,
        blank=True
    )

    seo_title = models.CharField(
        max_length=255,
        blank=True
    )

    seo_description = models.TextField(
        blank=True
    )

    selected_template = models.CharField(
        max_length=100
    )

    generated_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.business.business_name} Website"