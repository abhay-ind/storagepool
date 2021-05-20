# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import ModelFormWithFileField
# from .model import FileModel

# def upload_file(request):
#     if request.method == 'POST':
#         form = ModelFormWithFileField(request.POST, request.FILES)
#         if form.is_valid():
#             # instance = FileModel(file_field=request.FILES['file'])
#             # instance.save()
#             form.save()
#             return HttpResponseRedirect('success.html')#TODO: update view
#     else:
        
#         form = ModelFormWithFileField()
#     return render(request, 'upload.html', {'form': form})


#######################################################################################################3

#implementation using REST api
from django.http.response import HttpResponse
from rest_framework import response
from .serializers import FileSerializer

from .model import FileModel

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from .producer import publish

class FileViewSet(viewsets.ViewSet):
    def enlist(self, request):
        '''
            Method: GET  
            APIgateway: /display
            
            displays all the DB entries.
        '''
        q=FileModel.objects.values("filesize","filepath","timestamp")
        result=[]
        exist=set()
        q=reversed(q)
        for e in q:
            if(e["filepath"] not in exist and e["filesize"] is not  None):
                result.append(e)
                exist.add(e["filepath"])
        result.reverse()
        return Response(result,status=status.HTTP_200_OK)

    def show_site(self, request):
        '''
            Method: GET
            APIgateway: /api/upload

            displays the site through which files can be uploaded 
        '''
        pass


    def upload_file(self, request):
        '''
            Method: POST 
            APIgateway: /api/upload

            Uploads the file and creates a entry in the DB.

        '''
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('file_added', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


        

    def delete_file(self, request, pk=None):
        pass

    def update_link(self, request, pk=None):
        '''
            Method: GET

            /api/update/
        '''

        File = FileModel.objects.get(id=pk)
        serializer = FileSerializer(instance=File, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



    # def upload_file(self, request):
    #     '''
    #         Method: POST 
    #         APIgateway: /api/upload

    #         Uploads the file and creates a entry in the DB.

    #     '''
    #     form = ModelFormWithFileField(request.POST, request.FILES)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return Response(status=status.HTTP_202_ACCEPTED)
    #         except Exception as e:
    #             #TODO: Implement better exception handler
    #             print(e.__class__," occurred. ")
    #             return Response(status=status.HTTP_400_BAD_REQUEST)

    #     else:
    #         return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)