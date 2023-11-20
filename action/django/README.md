# Django

## 1. 简介

地址 : https://www.djangoproject.com/

Django 是一个开放源代码的 Web 应用框架，由 Python 编写。

Django 是一个基于 Python 的高级 Web 开发框架，由 Django 社区开发并维护。

## Django 版本

Django 4.2.x 版本

## 2. 安装

```bash
pip install django

pip install django==4.2.x

pip install django==4.2.6

pip install --upgrade django==4.2.7
```

## 3. 项目结构

```bash
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mysite.settings.py
···
```

## 4. 创建Django项目

```bash
django-admin startproject mysite
```

## 5. 启动项目

```bash
python manage.py runserver
```

## 6. 项目配置

```python
# mysite/settings.py

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

## 7. 查看工具功能
```

Django提供了一系列的工具来帮助我们查看项目的功能。

```bash
# 查看工具功能
python manage.py help

# 创建应用
python manage.py startapp index
```

## 8. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

## 9. 创建模型

```bash
python manage.py makemigrations mysite
python manage.py migrate mysite
```

## 10. 创建应用

```bash
python manage.py startapp index
```

## 11. 启动应用

```bash
python manage.py runserver

# 启动应用
python manage.py runserver 0.0.0.0:8000
```

## 12. 访问应用

```bash
http://127.0.0.1:8000/
```

## 13. 项目结构

```bash
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── mysite.settings.py
├── index
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── views.py
```

## 14. 项目配置

```
# mysite/settings.py

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 应用配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
]

# 静态文件配置
STATIC_URL = '/static/'

# 日志配置
LOGGING = {
   'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
       'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)
            d %(message)s'
            'level': 'DEBUG'
            'handlers': ['console']
            'propagate': True
            'formatter':'verbose'
            'class':'logging.Formatter'
            'filename':'logs/django.log'
            'encoding':'utf-8'
            'filters':['require_debug_true']
            'level':'DEBUG'
        }
    }
}
```

## 15. 数据库迁移

```bash
python manage.py makemigrations mysite
python manage.py migrate mysite
```

## 16. 创建模型

```bash
python manage.py makemigrations index
python manage.py migrate index
```

## 17. 创建视图

```python
# index/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    # 查询所有图书
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def detail(request, id):
    # 查询单个图书
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        # 接收数据
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        # 保存数据
        book = Book(title=title, author=author, price=price)
        book.save()


def delete(request, id):
    # 删除单个图书
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponse('删除成功')


def update(request, id):
    # 查询单个图书
    book = Book.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'update.html', {'book': book})
    elif request.method == 'POST':
        # 接收数据
        title = request.POST.get('title')
        author = request.POST
        price = request.POST.get('price')
        # 更新数据
        book.title = title
        book.author = author
        book.price = price
        book.save()
        return HttpResponse('更新成功')


def search(request):
    # 接收数据
    keyword = request.GET.get('keyword')
    # 查询图书
    books = Book.objects.filter(title__contains=keyword)
    return render(request, 'search.html', {'books': books})


def detail(request, id):
    # 查询单个图书
    book = Book.objects.get(id=id)
    return render(request, 'detail.html', {'book': book})
```

## 18. 启动应用

```bash
python manage.py runserver
```

## 19. 访问应用

```bash
http://127.0.0.1:800
1. 首先，我们需要在项目的urls.py中添加路由，以便访问我们的应用。

```python
# mysite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
]
```

```python
# index/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detail/<int:id>/', views.detail),
    path('add/', views.add),
    path('delete/<int:id>/', views.delete),
    path('update/<int:id>/', views.update),
    path('search/', views.search),
]
```

## 19. ORM 操作
```
数据表的读写
$ python manage.py  shell
>>> from index.models import *
>>> n = Name()
>>> n.name='红楼梦'
>>> n.author='曹雪芹'
>>> n.stars=9.6
>>> n.save()

使用ORM框架api实现
增
>>> from index.models import *
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')


查
>>> Name.objects.get(id=2).name

改
>>> Name.objects.filter(name='红楼梦').update(name='石头记')

删 
单条数据
>>> Name.objects.filter(name='红楼梦').delete()
全部数据
>>> Name.objects.all().delete()

其他常用查询
>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')
>>> Name.objects.create(name='活着', author='余华', stars='9.4')
>>> Name.objects.all()[0].name
>>> n = Name.objects.all()
>>> n[0].name
>>> n[1].name

>>> Name.objects.values_list('name')
<QuerySet [('红楼梦',), ('活着',)]>
>>> Name.objects.values_list('name')[0]
('红楼梦’,)
filter支持更多查询条件
filter(name=xxx, id=yyy)

可以引入python的函数
>>> Name.objects.values_list('name').count()
2
```