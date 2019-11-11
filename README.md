# slack_to_line_notifier
슬랙을 보지 않는 멤버들을 위한 Line 노티파이어

## Requirements
Docker  
docker-composer

## Flow
Create **"local_settings.py"** file for Django settings under the same directory with **"settings.py"**.<br />
local_settings.py has to inlude SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES.

```
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TEST_SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Create **"env_val.env"** file for Line token under the same directory with **"docker-compose.yml"**.<br />
env_val.env has to include LINE_TOKEN.
```
LINE_TOKEN=TEST_TOKEN
```

Run command for docker-compose.<br />
```
docker-compose up
```

Adding Slack's outcoming-hook URL to URL bellow.
```
http://${your_site_domain_or_ip_address}:8000/api/slack_to_line/
```
