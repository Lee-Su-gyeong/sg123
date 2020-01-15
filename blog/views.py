from datetime import timezone
from django.shortcuts import render
from .models import Post
#models.py파일에 정의된 모델을 가져옴.


# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
#요청(request)을 넘겨받아 render메서드를 호출
#render 메서드를 호출하여 받은(return) blog/post_list.html템플릿을 보여줌.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#posts쿼리셋을 템플릿에 보내기 위해 {'posts': posts}를 추가