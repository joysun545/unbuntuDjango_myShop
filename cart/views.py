# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from cart.cartmanager import getCartManger


class AddCartView(View):
    def post(self,request):
        #1.获取当前操作类型
        flag = request.POST.get('flag','')

        #2.判断当前操作类型
        if flag == 'add':
            #创建cartManager对象
            carManagerObj = getCartManger(request)
            #加入购物车操作
            carManagerObj.add(**request.POST.dict())

        elif flag == 'plus':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            #修改商品的数量（添加）
            carManagerObj.update(step=1,**request.POST.dict())

        elif flag == 'minus':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            # 修改商品的数量（添加）
            carManagerObj.update(step=-1, **request.POST.dict())

        elif flag == 'delete':
            # 创建cartManager对象
            carManagerObj = getCartManger(request)
            #逻辑删除购物车选项
            carManagerObj.delete(**request.POST.dict())

        return HttpResponseRedirect('/cart/queryAll/')


class CartListView(View):
    def get(self,request):
        # 创建cartManager对象
        carManagerObj = getCartManger(request)

        #查询所有购物项信息
        cartList = carManagerObj.queryAll()


        return render(request,'cart.html',{'cartList':cartList})