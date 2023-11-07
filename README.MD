1. Install dependencies
```
pip install -r requirements.txt
```
2. Activate Redis
```
docker run -p 6379:6379 redis
```
3. Create posts with custom command
default 10 posts:
```
python manage.py create_info
```
or 
```
python manage.py create_info --number=<int: number of posts>
```
4. Run Django web-server
```
python manage.py runserver
```