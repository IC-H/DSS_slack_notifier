# slack_to_line_notifier
슬랙을 보지 않는 멤버들을 위한 Line 노티파이어

## Requirements
Docker  
docker-composer

## Flow
1. Create **"local_settings.py"** file for Django settings under the same directory with **"settings.py"**.<br />
local_settings.py has to inlude SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASES.

2. Create **"env_val.env"** file for Line token under the same directory with **"docker-compose.yml"**.<br />
env_val.env has to include LINE_TOKEN.

3. run command for docker-compose.<br />
```
docker-compose up
```
