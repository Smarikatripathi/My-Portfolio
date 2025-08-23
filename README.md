# Professional CV Website

A modern, responsive, and interactive personal CV/portfolio website built with Django, HTML, CSS, and JavaScript. This website showcases your professional information, projects, skills, and provides a contact form that sends emails directly to your inbox.

## 🚀 Features

### Core Features
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Dynamic Content**: All content is managed through Django admin panel
- **Email Integration**: Contact form sends emails directly to your inbox
- **Theme Switcher**: Toggle between light and dark themes
- **SEO Optimized**: Meta tags, structured data, and semantic HTML

### Sections
- **Home**: Hero section with profile picture, introduction, and download resume option
- **About**: Detailed background, personality traits, and skills visualization
- **Education**: Timeline format showing academic background
- **Projects**: Dynamic project showcase with images and links
- **Skills**: Interactive progress bars and charts using JavaScript
- **Certifications**: Professional certifications and achievements
- **Testimonials**: Client and colleague testimonials
- **Contact**: Contact form with email integration

### Interactive Features
- **Smooth Scrolling**: Animated page transitions
- **Progress Bars**: Animated skill proficiency indicators
- **Hover Effects**: Interactive card and button animations
- **AJAX Contact Form**: Real-time form submission without page reload
- **Back to Top Button**: Smooth scroll to top functionality
- **Mobile Menu**: Responsive navigation for mobile devices

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.4.0
- **Animations**: AOS (Animate On Scroll)
- **Charts**: Chart.js
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Email**: Django Email Backend (SMTP)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd CV
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy the example environment file
cp env.example .env

# Edit .env file with your settings
# Use a text editor to modify the .env file
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your website!

## ⚙️ Configuration

### Email Setup
1. Edit the `.env` file with your email credentials
2. For Gmail, you'll need to:
   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password in `EMAIL_HOST_PASSWORD`

### Adding Content
1. Access the admin panel at `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Add your personal information, projects, skills, etc.

### Customization
- **Colors**: Modify CSS variables in `static/css/style.css`
- **Content**: Update through Django admin panel
- **Styling**: Edit templates in `templates/portfolio/`
- **Functionality**: Modify views in `portfolio/views.py`

## 📁 Project Structure

```
CV/
├── cv_website/          # Django project settings
│   ├── __init__.py
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   ├── wsgi.py          # WSGI configuration
│   └── asgi.py          # ASGI configuration
├── portfolio/           # Main app
│   ├── __init__.py
│   ├── admin.py         # Admin interface configuration
│   ├── apps.py          # App configuration
│   ├── forms.py         # Django forms
│   ├── models.py        # Database models
│   ├── urls.py          # App URL patterns
│   └── views.py         # View functions
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── portfolio/       # App-specific templates
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       └── contact.html
├── static/              # Static files
│   ├── css/
│   │   └── style.css    # Custom styles
│   └── js/
│       └── main.js      # Custom JavaScript
├── media/               # User-uploaded files
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── env.example          # Environment variables example
└── README.md           # This file
```

## 🎨 Customization Guide

### Adding New Sections
1. Create a new model in `portfolio/models.py`
2. Add admin configuration in `portfolio/admin.py`
3. Create a view in `portfolio/views.py`
4. Add URL pattern in `portfolio/urls.py`
5. Create template in `templates/portfolio/`
6. Update navigation in `templates/base.html`

### Styling Modifications
- **Colors**: Update CSS variables in `:root` selector
- **Fonts**: Change Google Fonts import in `base.html`
- **Layout**: Modify Bootstrap classes in templates
- **Animations**: Adjust AOS attributes in templates

### Adding JavaScript Features
- **New Functions**: Add to `static/js/main.js`
- **Event Listeners**: Use `DOMContentLoaded` event
- **AJAX Calls**: Follow the contact form pattern

## 📧 Email Configuration

### Gmail Setup
1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Generate an App Password
4. Use the App Password in your `.env` file

### Other Email Providers
Update the email settings in `.env`:
```env
EMAIL_HOST=your-smtp-server.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@domain.com
EMAIL_HOST_PASSWORD=your-password
```

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. Set `DEBUG=False` in `.env`
2. Configure your production database
3. Set up static file serving
4. Configure your web server (Nginx, Apache)
5. Use a production WSGI server (Gunicorn)

### Environment Variables for Production
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the Django documentation
2. Review the error logs
3. Create an issue in the repository
4. Contact the maintainer

## 🎯 Roadmap

- [ ] Blog functionality
- [ ] Portfolio gallery
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Social media integration
- [ ] Newsletter subscription
- [ ] Advanced SEO features

---

**Happy Coding! 🎉** 