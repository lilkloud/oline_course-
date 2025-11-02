# 9kloud — Online Learning Platform

A modern, responsive online learning platform built with Django and Bootstrap 5. Features a clean, dark-themed interface with course management, user authentication, and interactive learning experiences.

## 🌟 Features

### Core Features
- **User Authentication**: Secure signup, login, and password reset functionality
- **Course Management**: Browse, search, and enroll in courses
- **Interactive Learning**: Track progress through course modules and lessons
- **Instructor Profiles**: Detailed instructor information and course listings
- **Responsive Design**: Fully responsive layout that works on all devices
- **Dark Mode**: Built-in dark theme for comfortable learning

### Technical Features
- **Django 4.2+**: Robust backend framework
- **Bootstrap 5**: Modern, responsive frontend framework
- **Vite.js**: Fast frontend asset building
- **SCSS**: Advanced CSS with variables and mixins
- **SQLite/PostgreSQL**: Flexible database options
- **Django Admin**: Powerful built-in admin interface

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+ (for frontend assets)
- PostgreSQL (for production, SQLite for development)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/lilkloud/online_course-.git
   cd online_course-
   ```

2. **Set up Python virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///db.sqlite3
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Set up frontend dependencies**
   ```bash
   npm install
   npm run dev  # For development with hot-reload
   # or
   npm run build  # For production build
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Homepage: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
   - API: http://127.0.0.1:8000/api/

## 📦 Production Deployment

### Environment Variables
Create a `.env.prod` file with your production settings:
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=.yourdomain.com
DATABASE_URL=postgres://user:password@localhost:5432/dbname
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=your-smtp-host
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@example.com
```

### Deployment Steps
1. **Set up a production database** (PostgreSQL recommended)
2. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```
3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```
4. **Set up a production web server** (Gunicorn + Nginx recommended)
   ```bash
   # Install Gunicorn
   pip install gunicorn
   
   # Run Gunicorn
   gunicorn ninekloud.wsgi:application --bind 0.0.0.0:8000
   ```

## 🛠 Project Structure

```
├── core/                  # Core application
├── courses/              # Courses app
│   ├── migrations/       # Database migrations
│   ├── templates/        # App-specific templates
│   ├── admin.py          # Admin configuration
│   ├── models.py         # Database models
│   └── views.py          # View functions
├── static/               # Static files (CSS, JS, images)
│   ├── css/              # Compiled CSS
│   ├── js/               # JavaScript files
│   └── img/              # Image assets
├── templates/            # Global templates
├── .env.example          # Example environment variables
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── vite.config.js        # Vite configuration
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap 5](https://getbootstrap.com/) - Frontend framework
- [Vite.js](https://vitejs.dev/) - Frontend build tool
- [Font Awesome](https://fontawesome.com/) - Icons

## License
MIT
