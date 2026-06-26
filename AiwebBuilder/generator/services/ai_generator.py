import os
import json
import google.generativeai as genai

genai.configure(
    api_key = os.getenv("GEMINI_API_KEY")
)

# def test_gemini():

#     model = genai.GenerativeModel(
#         "gemini-2.5-flash"
#     )

#     response = model.generate_content(
#         "Say hello from Gemini."
#     )

#     return response.text

def generate_website_content_ai(business):


    prompt  = f"""
        You are an expert website copywriter.

        Please Generate professional website content for:

        Business Name: {business.business_name}
        Business Type: {business.business_type}
        Description: {business.description}
        Location: {business.location}
        Target Audience: {business.target_audience}

        Return ONLY valid JSON.

        Format:

        {{
            "hero_title": "",
            "hero_subtitle": "",
            "about_text": "",
            "services": [],
            "faqs": [],
            "testimonials": [],
            "pricing_plans": [],
            "seo_title": "",
            "seo_description": ""
        }}

        Return ONLY a valid JSON object.

        Rules:
        1. Return JSON only.
        2. No markdown.
        3. No explanations.
        4. No text before JSON.
        5. No text after JSON.
        6. Output must be valid JSON.

        Requirements:
        - Hero title should be persuasive and engaging.
        - Hero subtitle should clearly explain the business value.
        - About section should be 2-3 paragraphs.
        - Generate 6-8 realistic services.
        - Generate 5 realistic FAQs.
        - Generate 3 customer testimonials.
        - Generate 3 pricing plans.
        - SEO title should be optimized.
        - SEO description should be 150-160 characters.
    """
    
    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )
    try:

        response = model.generate_content(
            prompt
        )

    except Exception as e:

        print("Gemini API Error:")
        print(e)

        return {
            "hero_title": business.business_name,
            "hero_subtitle": "AI generation temporarily unavailable",
            "about_text": business.description,
            "services": [],
            "faqs": [],
            "testimonials": [],
            "pricing_plans": [],
            "seo_title": business.business_name,
            "seo_description": business.description
        }

    response_text = response.text.strip()

    response_text = (
        response_text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )


    try:

        data = json.loads(
            response_text
            )
    
    except json.JSONDecodeError as e:
        
        print("Json Error:")
        print(e)
        
        print("Gemini Response:")
        print(response_text)

        return{
            "hero_title": business.business_name,
            "hero_subtitle": "Website generation failed",
            "about_text": business.description,
            "services": [],
            "faqs": [],
            "testimonials": [],
            "pricing_plans": [],
            "seo_title": business.business_name,
            "seo_description": business.description
        }


    return data
    