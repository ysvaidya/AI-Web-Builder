from .ai_generator import generate_website_content_ai

def generate_website_content(business):

    website_data = generate_website_content_ai(
        business,
    )

    return website_data