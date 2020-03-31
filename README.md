[TOC]

# 我的Django RESTFramework使用文档 


## #1 命名规范 

### #1.1 app

- 所有app必须在项目根目录下
- 命名 : app_+名字
- 新建app后,在app目录下添加urls.py文件

### #1.2 文件/文件夹

- 所有文件/文件夹均已蛇形命名法命名(小写字母+下划线)

### #1.3 类/函数/变量 

- 类 : 大驼峰命名(首字母大写)
- 函数 : 蛇形命名法
- 变量 : 蛇形命名法 
- 全局变量 : 全大写 

## #2 格式化输出 

### #2.1 代码注释 

#### #2.1.1 settings.py

settings.py注释规范: 

> my_django2x_restframework/app_test/create_code_comments.py 

## #3 我的插件 

> 插件路径 : /my_django2x_restframework/app/utils/common/

```html
.
├── authenticates # 自定义用户验证 
├── base
├── cacheredis # 重写Redis, 解决高版本4.0的Celery与高本版的Redis不兼容问题 
├── exceptions # 异常拦截器 
├── files # 文件操作 
├── jsonschemas # json校验 
├── middlewares # 中间件 
├── mixins
├── mypermissions # 权限 
├── paginations # 分页 
├── serializers # 序列化 
├── signals # 信号量 
└── viewsets # 视图 
```







