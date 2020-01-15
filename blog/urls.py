from django.urls import path
from . import views
#장고 함수인 path와 blog 애플리케이션에서 사용할 모든 views를 가져왔어요.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    #post_list라는 view가 루트 URL에 할당
]