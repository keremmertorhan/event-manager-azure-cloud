import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-fallback-key-123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# CSRF Ayarları - Azure domainleri için gerekli
CSRF_TRUSTED_ORIGINS = [
    'https://kerem-event-manager-dzfpegdwbqdsbzea.polandcentral-01.azurewebsites.net',
    'https://*.azurewebsites.net'
]

# Application definition
INSTALLED_APPS = [
    'events',
    'users',
    'storages',  # Azure Storage için gerekli
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'event_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'event_manager.wsgi.application'

# Database - Azure PostgreSQL bağlantısı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# --------------------------------------------------------
# AZURE STORAGE AYARLARI (Garanti Bağlantı Yapısı)
# --------------------------------------------------------

# 1. Depolama Sınıfı Seçimi
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'

# 2. Azure Hesap Bilgileri
AZURE_ACCOUNT_NAME = 'keremstorage01'
AZURE_CONTAINER = 'media'

# 3. Kimlik Doğrulama (Hata payını sıfırlamak için doğrudan Key kullanıyoruz)
AZURE_ACCOUNT_KEY = 'QZu/U9synZ0v4mfz0r6QugHjjD+mpu4BdOOox6yKqzqMfMpAQ5hJ77jFDe3t/bdgiW8LBOfyXtHk+AStG8GXSg=='

# 4. Dosya ve Klasör Ayarları
AZURE_LOCATION = ''            # Dosyaları doğrudan media kutusuna atar
AZURE_OVERWRITE_FILES = True    # Aynı isimli dosya gelirse üstüne yazar
AZURE_CONNECTION_TIMEOUT = 30   # Bağlantı kopmalarını engellemek için süre artırıldı

# 5. Erişim Linki
MEDIA_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/'

# --------------------------------------------------------

# Static files (CSS, JavaScript)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login/Logout Yönlendirmeleri
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
