import jsonpickle
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from cart.cartmanager import getCartManger


class ToOrderView(View):
    def get(self, request):
        # 获取请求参数
        cartitems = request.GET.get('cartitems', '')

        # 判断用户是否登录
        if not request.session.get('user'):
            return render(request, 'login.html', {'cartitems': cartitems, 'redirect': 'order'})

        return HttpResponseRedirect('/order/order.html?cartitems=' + cartitems)


class OrderListView(View):
    def get(self, request):
        # 获取请求参数
        cartitems = request.GET.get('cartitems', '')

        # jiangjson格式字符串转换成python对象列表
        cartitemLIst = jsonpickle.loads("[" + cartitems + "]")
        # 将python对象列表转换成cartitem对象列表
        cartitemObjList = [getCartManger(request).get_cartitems(**item) for item in cartitemLIst if item]

        # 获取用户的默认收货地址
        address = request.session.get('user').address_set.get(isdefault=True)

        # 获取支付总金额
        totalPrice = 0
        for cm in cartitemObjList:
            totalPrice += cm.getTotalPrice()

        return render(request, 'order.html',
                      {'cartitemObjList': cartitemObjList, 'address': address, 'totalPrice': totalPrice})
