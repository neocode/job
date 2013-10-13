__author__ = "alex"
from django.db import models
from dynamic_model.yamls import doc

print doc


for i in doc.keys():
    print "|", i
    if i == "field":
        print doc.get(i)


names = ('first', 'second', 'third', 'fourth')
model_list = []
supermodel_list = []

for i in names:
    dct = {
        "__module__": "dynamic_model.models",
        "title": models.CharField(max_length=255),
        "content": models.TextField(),
        "__unicode__": lambda self: self.title
    }
    model = type(i, (models.Model,), dct)
    model_list.append(model)
    #install(model)

print model_list

dct = {
    "__module__": "dynamic_model.models",
    "title": models.CharField(max_length=255),
    "first": models.ManyToManyField(model_list[0]),
    "second": models.ManyToManyField(model_list[1]),
    "third": models.ManyToManyField(model_list[2]),
    "fourth": models.ManyToManyField(model_list[3]),
    "__unicode__": lambda self: self.title
}
supermodel = type('This_new', (models.Model,), dct)
supermodel_list.append(supermodel)
#install(supermodel)



'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

'''




#install(Post)
