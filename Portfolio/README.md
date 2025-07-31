# Django Portfolio Website

A clean, professional portfolio website built with Django, showcasing my skills, projects, and contact information.

## 🚀 Features

- **Responsive Design**: Works seamlessly across desktop, tablet, and mobile devices
- **Multi-page Navigation**: About, Projects, and Contact pages
- **Clean UI**: Modern, minimalist design with smooth animations
- **Interactive Contact**: Clickable contact cards for email, GitHub, and LinkedIn
- **Static File Management**: Organized CSS and static assets

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (development)
- **Styling**: Custom CSS with responsive design

## 📁 Project Structure

```
Portfolio/
├── Portfolio/                  # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL routing
│   ├── views.py               # View functions
│   └── wsgi.py
├── static/                    # Static files
│   └── styles.css            # Main stylesheet
├── templates/                 # HTML templates
│   ├── about.html            # About page
│   ├── contact.html          # Contact page
│   └── projects.html         # Projects page
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── README.md                 # This file
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Navigate to the project directory**
   ```bash
   cd Portfolio
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Visit the website**
   Open your browser and go to `http://127.0.0.1:8000/`

## 📄 Pages Overview

### 🏠 About Page (`/`)
- Personal introduction and background
- Skills showcase with technology stack
- Philosophy and approach to development
- Professional journey highlights

### 💼 Projects Page (`/projects/`)
- Showcase of completed and ongoing projects
- Project descriptions and technologies used
- Links to live demos and source code

### 📧 Contact Page (`/contact/`)
- Interactive contact cards
- Direct links to email, GitHub, and LinkedIn
- Professional networking information

## 🎨 Design Features

- **Modern Typography**: Clean, readable fonts
- **Smooth Animations**: Hover effects and transitions
- **Color Scheme**: Professional blue and white palette
- **Mobile-First**: Responsive design approach
- **Accessibility**: Semantic HTML and proper contrast ratios

## 🚀 Deployment

### Development
The project is configured for development with Django's built-in server.

### Production Considerations
For production deployment, consider:
- Setting `DEBUG = False` in settings.py
- Configuring a production database (PostgreSQL recommended)
- Setting up static file serving with a web server (Nginx/Apache)
- Adding environment variables for sensitive settings
- Implementing SSL certificates

## 🤝 Contributing

This is a personal portfolio project, but feel free to:
- Report bugs or issues
- Suggest improvements
- Fork the project for your own use

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 About the Developer

**Vaibhav Maurya**
- 📧 Email: mauryavaibhav2007@gmail.com
- 💼 GitHub: [Vaibhav07-M](https://github.com/Vaibhav07-M)
- 🔗 LinkedIn: [vaibhav-mavex](https://www.linkedin.com/in/vaibhav-mavex/)

---

