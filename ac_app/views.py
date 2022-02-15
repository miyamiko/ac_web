from django.shortcuts import render

from .models import Access
from django.views import View
class AccessView(View):

    def get(self, request, *args, **kwargs):
        q=Access.objects.get(id=1)
        kaisuu=int(q.access_no)+1
        q.access_no=kaisuu
        q.save()
        test_text=str(kaisuu)+'回目のアクセスです'
        context = { "test_text"     : test_text
                    }
    
        return render(request,"ac_app/index.html",context)

    def post(self, request, *args, **kwargs):
        q=Access.objects.get(id=1)
        if request.POST['name'] == 'Reset':
            kaisuu=0
        q.access_no=kaisuu
        q.save()

        test_text='カウンタークリア'
        context = { "test_text"     : test_text
                    }
    
        return render(request,"ac_app/index.html",context)
