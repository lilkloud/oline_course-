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

- **[Django](https://www.djangoproject.com/) 4.2+**: Robust backend framework
- **[Bootstrap 5](https://getbootstrap.com/)**: Modern, responsive frontend framework
- **[Vite.js](https://vitejs.dev/)**: Fast frontend asset building
- **SCSS**: Advanced CSS with variables and mixins
- **PostgreSQL**: Production-ready database
- **Docker**: Containerized development and production environments
- **Nginx**: High-performance web server
- **Gunicorn**: Production-grade WSGI server

## 🚀 Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

### Local Development with Docker

1. **Clone the repository**

   ```bash
   git clone https://github.com/lilkloud/online_course-.git
   cd online_course-
   ```

2. **Set up environment variables**

   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file with your configuration:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   DB_NAME=online_courses
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=db
   DB_PORT=5432
   ```

3. **Build and start the containers**

   ```bash
   docker-compose up --build
   ```

4. **Run database migrations**

   In a new terminal:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application**

   - Website: [http://localhost:8000](http://localhost:8000)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 🏗 Project Structure

```
online_course-/
├── .github/            # GitHub workflows and templates
├── courses/            # Main Django app
├── media/              # User-uploaded files
├── ninekloud/          # Project settings
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── .env.example        # Example environment variables
├── .gitignore          # Git ignore file
├── docker-compose.yml  # Docker Compose configuration
├── Dockerfile          # Docker configuration
├── manage.py           # Django management script
├── nginx/              # Nginx configuration
│   └── nginx.conf
└── requirements.txt    # Python dependencies
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
