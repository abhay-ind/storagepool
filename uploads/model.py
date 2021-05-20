from django.db import models


class FileModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/storage
    namefield = models.CharField(max_length=50)
    filepath = models.FileField(upload_to='storage')
    
    # uploader = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(null=True)

    sha1sum = models.CharField(max_length=40, null=True)
    filesize = models.IntegerField(null=True)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    # upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

# class Owership(models.Model):
#     uid = models.IntegerField()
#     hash = models.CharField(max_length=40)