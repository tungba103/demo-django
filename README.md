# 1. Tạo file requirements.txt
# 2. Tạo venv

pip install -r requirements.txt
pip uninstall -y -r requirements.txt

# 3. Set up a new project with a single application
django-admin startproject core .  # Note the trailing '.' character
cd core
django-admin startapp users
cd ..

python manage.py migrate

python manage.py createsuperuser --username admin --email admin@example.com

Tạo 1 serializers.py

Chỉnh sửa views.py

# 4. Set up django-rest-swagger

# 5. Set up api authentication

# Set up database postgres