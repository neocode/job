__author__ = "alex"
from django.db import models
from dynamic_model.yamls import doc

print doc


def install(model):
    from django.core.management import sql, color
    from django.db import connection

    style = color.no_style()

    cursor = connection.cursor()
    statements = sql.sql_create(model, style, connection)
    print statements
    for sql in statements:
        cursor.execute(sql)


names = ('first', 'second', 'third', 'fourth')
model_list = []
supermodel_list = []

for i in names:
    dct = {
        "__module__": "dynamic_model.models",
        "title": models.CharField(max_length=255),
        "content": models.TextField()
    }
    model = type(i, (models.Model,), dct)
    model_list.append(model)
    install(model)

print model_list

dct = {
    "__module__": "dynamic_model.models",
    "title": models.CharField(max_length=255),
    "first": models.ForeignKey(model_list[0]),
    "second": models.ForeignKey(model_list[1]),
    "third": models.ForeignKey(model_list[2]),
    "fourth": models.ForeignKey(model_list[3]),
}
supermodel = type('This_new', (models.Model,), dct)
supermodel_list.append(supermodel)
install(supermodel)



'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

'''




#install(Post)
