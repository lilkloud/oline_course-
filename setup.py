from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ninekloud',
    version='0.1.0',
    description='An online courses platform built with Django',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/online-courses',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2.0,<5.0.0',
        'psycopg2-binary>=2.9.0',
        'python-dotenv>=0.19.0',
        'whitenoise>=6.0.0',
        'gunicorn>=20.0.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 4.2',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'ninekloud=manage:main',
        ],
    },
)
