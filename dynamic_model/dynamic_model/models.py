__author__ = "alex"
from django.db import models
#import type


def install(model):
    from django.core.management import sql, color
    from django.db import connection

    style = color.no_style()

    cursor = connection.cursor()
    statements = sql.sql_create(model, style, connection)
    for sql in statements:
        cursor.execute(sql)


names = ('first', 'second', 'third', 'fourth')
model_list = []

for i in names:
    dct = {
        "__module__": "dynamic_model.models",
        "title": models.CharField(max_length=255),
        "content": models.TextField()
    }
    model = type(i, (models.Model,), dct)
    model_list.append(model)
    install(model)


'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

'''




#install(Post)
