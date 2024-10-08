from django.urls import re_path
from .consumers import ChatConsumer, NotificationStudentConsumer ,AdminConsumer

websocket_urlpatterns = [
    re_path(r"ws/some_path/$", ChatConsumer.as_asgi()),  
    re_path(r"ws/student/(?P<student_id>\d+)/$", NotificationStudentConsumer.as_asgi()),  
    re_path(r"ws/dish_choise/",AdminConsumer.as_asgi())
]