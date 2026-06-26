# 🚀 AI Web Builder

An AI-powered website builder that generates modern business websites using **Google Gemini AI**, **Django**, and **Tailwind CSS**.

This project allows users to enter their business details and automatically generate website content such as hero sections, about sections, services, FAQs, testimonials, pricing plans, and SEO content. The long-term goal is to generate complete business websites that users can customize and publish.

---

# 📖 About the Project

Creating a professional business website takes time, design knowledge, and content writing skills.

The goal of this project is to simplify that process using Artificial Intelligence.

Users provide information about their business, and the application uses Google's Gemini AI model to generate website content automatically.

Instead of starting from a blank page, users receive a complete website structure that can be customized further.

---

# ✨ Features

## 📝 Business Information Form

Users can provide:

- Business Name
- Business Type
- Business Description
- Contact Information
- Address
- Social Media Links

---

## 🤖 AI Content Generation

Using Google Gemini AI, the application generates:

- Hero Title
- Hero Subtitle
- About Section
- Services
- FAQs
- Testimonials
- Pricing Plans
- SEO Title
- SEO Description

---

## 🎨 Website Templates

Currently implemented templates:

- Modern Business
- Portfolio
- Cafe / Restaurant

Each template is fully responsive and built using Tailwind CSS.

---

## ⚙ Backend

Built using Django.

Current implementation includes:

- Business Model
- Generated Website Model
- AI Service Layer
- JSON Response Parsing
- Database Storage
- Django Admin Integration

---

## 🧠 AI Integration

- Google Gemini API
- Prompt Engineering
- JSON-only Responses
- Automatic Parsing
- Dynamic Website Content Generation

---

# 🛠 Tech Stack

## Backend

- Python
- Django

## Frontend

- HTML
- Tailwind CSS
- JavaScript

## Database

- SQLite

## AI

- Google Gemini API

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
AI-Web-Builder/
│
├── AiwebBuilder/
├── generator/
├── templates/
├── static/
├── media/
├── requirements.txt
├── manage.py
└── README.md
```

---

# ✅ Completed

- Django Project Setup
- Business Information Form
- Database Models
- Google Gemini Integration
- AI Prompt Engineering
- JSON Parsing
- Website Content Generation
- Responsive Website Templates
- GitHub Repository
- Tailwind CSS UI

---

# 🚧 Work In Progress

Currently working on:

- Live Website Preview
- Template Switching
- Rich Text Editing
- Better Error Handling
- Loading Animations
- UI Improvements
- Validation Improvements

---

# 🌟 Future Features

Planned improvements:

- User Authentication
- User Dashboard
- Save Generated Websites
- Export HTML
- Download Website ZIP
- More Business Templates
- Theme Customization
- AI Image Generation
- One-click Website Publishing
- Custom Domains
- Analytics Dashboard
- Multi-language Support
- Payment Integration
- Subscription Plans

---

# 💡 Challenges Faced

During development I solved several real-world problems:

- Integrating Google Gemini AI with Django
- Handling JSON formatting returned by AI
- Managing API Rate Limits
- Designing reusable database models
- Building reusable website templates
- Connecting AI-generated content with frontend layouts

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ysvaidya/AI-Web-Builder.git
```

Move into the project

```bash
cd AI-Web-Builder
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
DEBUG=True
```

Run migrations

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 📸 Screenshots

Screenshots will be added soon.

---

# 📚 What I Learned

This project helped me gain practical experience in:

- Django Project Architecture
- AI API Integration
- Prompt Engineering
- Database Design
- Tailwind CSS
- JSON Handling
- Git & GitHub Workflow
- Backend Development Best Practices

---

# 🤝 Contributing

This is currently a personal learning project.

Suggestions and feedback are always welcome.

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Yash Vaidya**

Python Developer | Django Developer | AI Enthusiast

GitHub: https://github.com/ysvaidya
