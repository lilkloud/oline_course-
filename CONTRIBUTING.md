# Contributing to 9kloud Online Courses

Thank you for your interest in contributing to 9kloud Online Courses! We welcome contributions from the community to help improve this project.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How to Contribute

### Reporting Bugs
1. Check if the bug has already been reported in the [issue tracker](https://github.com/yourusername/online-courses/issues).
2. If not, create a new issue with a clear title and description.
3. Include steps to reproduce the bug, expected behavior, and actual behavior.

### Suggesting Enhancements
1. Check if the enhancement has already been suggested.
2. Create a new issue with a clear title and description of the enhancement.
3. Explain why this enhancement would be useful.

### Pull Requests
1. Fork the repository and create a new branch for your feature or bugfix.
2. Make your changes and ensure tests pass.
3. Submit a pull request with a clear description of the changes.

## Development Setup

### Prerequisites
- Python 3.8+
- PostgreSQL
- Node.js and npm (for frontend assets)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-courses.git
   cd online-courses
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing

Run the test suite:
```bash
pytest
```

## Code Style

We use Black for code formatting and flake8 for linting. Run these before committing:

```bash
black .
flake8
```

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
