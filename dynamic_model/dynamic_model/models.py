__author__ = "alex"
from django.db import models
from dynamic_model.yamls import doc

#print doc
model_list = []
names = doc.keys()
field_list = doc.values()
for i in range(len(field_list)):
    name = names[i]
    dict = {}
    for k in field_list[i].get("fields"):
        #print k, "dsd"
        for m in k:
            if (m == "type") and (k[m] == "char"):
                dict[k["id"]] = models.CharField(max_length=255)
            if (m == "type") and (k[m] == "int"):
                dict[k["id"]] = models.IntegerField()
            if (m == "type") and (k[m] == "date"):
                dict[k["id"]] = models.DateField()
    dict["__module__"] = "dynamic_model.models"
    if name == "users":
        dict["__unicode__"] = lambda self: self.name
    elif name == "rooms":
        dict["__unicode__"] = lambda self: self.department
    model = type(name, (models.Model,), dict)
    model_list.append(model)

'''

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

'''
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

'''




#install(Post)
