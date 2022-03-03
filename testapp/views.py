from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from config.settings import CACHE_TTL
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers as testapp_serializer
from . import models as testapp_model
from django.core.cache import cache
import time
# Create your views here.

# 함수 자체를 캐시화
@cache_page(CACHE_TTL)
def testView(request):
    text = "Helloooooo"
    return render(request, 'test.html', {'text': text})

class testApiViewSet(viewsets.ModelViewSet):
    queryset = testapp_model.testApiModel.objects.all()
    serializer_class = testapp_serializer.testApiSerializer

    # 캐시에 저장하여 속도 비교
    @action(detail = False)
    def check_cache(self, request):
        if request.method == "GET":
            start = time.time()
            param = request.GET.get('text')
            print("쿼리 매개변수", param)
            check_param_in_cache = cache.get(param)
            if check_param_in_cache is None:
                print("캐시에 존재하지 않음")
                cache.set(param, param, 60*60)
                print("저장 완료")
            else:
                print("캐시에 존재 함", cache.get(param))
            print("걸린 시간 : ", time.time() - start)
            n = testapp_model.testApiModel.objects.filter(text=param).count()
            return Response(n)