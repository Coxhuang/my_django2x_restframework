"""
Django settings for my_django2x_restframework project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i^ze2&bdzbqk^vc2y6re9wrd+m_l_s3$t-7!*5es0)-a&vz)p@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_swagger', # swagger 文档
    'django_filters', #
    'django_crontab', #
    'rest_framework.authtoken', #
    'rest_framework', #
    'app',
    'app_user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_django2x_restframework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_django2x_restframework.wsgi.application'

# *******************************************************************************
# *                                                                             *
# * @标题  : Django参数
# * @功能  : 配置自定义Django参数
# * @备注  : None
# *                                                                             *
# *******************************************************************************
AUTH_USER_MODEL = 'app_user.UserProfile' # 使用抽象类(AbstractUser)时,打开这个 from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import authenticate # 验证使用
# AUTHENTICATION_BACKENDS = (
#     'app.utils.common.authenticates.authenticate.CustomBackend',
# )

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# *******************************************************************************
# *                                                                             *
# * @标题  : 数据库引擎
# * @功能  : 配置数据库类型
# * @备注  : None
# *                                                                             *
# *******************************************************************************
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', # mysql 引擎
    #     'NAME': 'blog_db', # 数据库名
    #     'USER': 'root', # 登录用户名
    #     'PASSWORD': 'root', # 登录密码
    #     'HOST': '127.0.0.1', # mysql地址
    #     'PORT': '3306', # mysql 端口号
    #     'CONN_MAX_AGE': 600, # 最大链接时间
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True

LANGUAGE_CODE = 'zh-hans' # Django admin 中文显示

TIME_ZONE = 'Asia/Shanghai' # 上海时区

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# *******************************************************************************
# *                                                                             *
# * @标题  : Django RESTFramework
# * @功能  : 配置DRF插件
# * @备注  : None
# *                                                                             *
# *******************************************************************************
REST_FRAMEWORK = {
    "DEFAULT_VERSION": 'v1',  # 默认的版本
    "ALLOWED_VERSIONS": ['v1', 'v2'],  # 允许的版本
    "VERSION_PARAM": 'version',  # GET方式url中参数的名字  ?version=xxx
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', # 浏览器模式,浏览器访问,渲染DRF自带UI界面
    ),
    'EXCEPTION_HANDLER': 'app.utils.common.exceptions.exception.custom_exception_handler',

    'DEFAULT_THROTTLE_CLASSES': ( # 自定义节流
        # 'rest_framework.throttling.AnonRateThrottle',
        # 'rest_framework.throttling.UserRateThrottle'
        'rest_framework.throttling.ScopedRateThrottle',  # throttle_scope = 'uploads'
    ),
    'DEFAULT_THROTTLE_RATES': { # 节流限流配置
        # 'anon': '2/m',
        # 'user': '5/m',
        "throttle_base_30_Min": "30/m",  # 所有接口
        'login_throttle': '20/m', # 登录节流
    },
}

# *******************************************************************************
# *                                                                             *
# * @标题  : TOKEN
# * @功能  : token配置
# * @备注  : None
# *                                                                             *
# *******************************************************************************
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1), # 指明token的有效期
    'JWT_ISSUER': 'http://fasfdas.baicu',
    'JWT_AUTH_HEADER_PREFIX': 'TOKEN',
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1)
}


# *******************************************************************************
# *                                                                             *
# * @标题  : 分页
# * @功能  : 分页参数配置
# * @备注  : None
# *                                                                             *
# *******************************************************************************
MY_PAGE_SIZE = 20 # 默认分页,每页显示条数
MY_ARTICLE_PAGE_SIZE = 5 # 客户端文章列表分页,每页显示条数
MY_PAGE_SIZE_QUERY_PARAM = "size" # 可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
MY_MAX_PAGE_SIZE = 1000 # 最大页数不超过1000
MY_PAGE_QUERY_PARAM = "page"  # 获取页码数的


# *******************************************************************************
# *                                                                             *
# * @标题  : 跨域配置
# * @功能  : 解决前后端分离跨域问题
# * @备注  : 看一下说明,有几个需要注意的地方
# * #说明2 : 在settings.py文件中添加中间件 corsheaders.middleware.CorsMiddleware
# * #说明2 : 中间件corsheaders.middleware.CorsMiddleware必须放在第三的位置,不能任意放
# *                                                                             *
# *******************************************************************************
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    # 'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'User-agent',
    'x-csrftoken',
    'x-requested-with',
    'token',
)

