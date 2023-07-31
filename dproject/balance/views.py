import json

from django.db.models import F
from django.views.generic import TemplateView
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Balance


class UsersView(APIView):
    def get(self, request):
        allBalances = Balance.objects.all().values()
        return Response(list(allBalances))

    def post(self, request):
        data = json.loads(request.body)
        if 'add' in data:
            id = data['user']
            money = data['add']
            if int(money) > 0:
                person = Balance.objects.filter(pk=id).update(balance=F("balance") + money)
        if 'remove' in data:
            id = data['user']
            money = data['remove']
            balanceObject = Balance.objects.get(pk=id)
            balanceValue = balanceObject.balance
            if int(money) > 0 and balanceValue >= int(money):
                person = Balance.objects.filter(pk=id).update(balance=F("balance") - money)
        if 'exchange' in data:
            first_user = data['root']
            second_user = data['endpoint']
            money = data['exchange']
            balanceObject = Balance.objects.get(pk=first_user)
            balanceValue = balanceObject.balance
            if int(money) > 0 and balanceValue >= int(money):
                person_one = Balance.objects.filter(pk=first_user).update(balance=F("balance") - money)
                person_two = Balance.objects.filter(pk=second_user).update(balance=F("balance") + money)
        if 'balance' in data:
            user = data['user']
            balanceObject = Balance.objects.filter(pk=user).values()
            if not balanceObject:
                return Response(status=400)
            return Response(balanceObject)
        return JsonResponse(data)


class TestView(TemplateView):
    template_name = 'balance/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
