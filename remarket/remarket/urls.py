"""
URL configuration for remarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import CategoryListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentications.urls')),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('listings/', include('listings.urls')),
    path('products/', include('products.urls')),
    path('interests/', include('interests.urls')),
    path('inquiries/', include('inquiries.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
