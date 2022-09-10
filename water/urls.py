"""water URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path

from client.views import *
from core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('about/', about),
    path('', MakerListView.as_view(), name='makers-list'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/order-list/', ClientOrderList.as_view(), name="client-order-list"),
    path('client/update/<int:id>/', ClientUpdateView.as_view(), name="client-update"),
    path('order/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-details'),
    path('order/update/<int:id>/', OrderUpdateView.as_view(), name="order-update"),
    path('order/del/<int:id>/', OrderDeleteView.as_view(), name="order-delete"),
    path('order/djangoform/', CreateOrderDjangoView.as_view(), name='order-djangoform'),
    path('order/create/', CreateOrderView.as_view(), name='create-order'),
    path('test/', MyView.as_view()),
    path('signin/', LoginView.as_view(), name="sign-in"),
    path('signout/', LoginOutView.as_view(), name="sign-out")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
