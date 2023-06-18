from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('helloworld', views.ApprovalsView)

urlpatterns = [
    # path('form/', views.MyForm, name='myform'),  # Update the view function name
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]

