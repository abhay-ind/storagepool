"""meganz_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from .views import upload_file

# urlpatterns = [
#     ### api/upload
#     path('api/upload', upload_file),

#     ### api/destroy
#     # path('api/destroy', ),

# ]

from .views import FileViewSet
urlpatterns = [
    path('api/upload', FileViewSet.as_view({
        # 'get': "", #show upload page
        'post': 'upload_file', #start upload and update DB.
        'get':'enlist'
    }))
]