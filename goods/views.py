from csv import reader
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from goods import entities
from goods.forms import UploadPriceForm
from goods import models
from goods.models import ItemNew
from goods.serializers import ItemSerializer


def item_list(request):
    items = models.Item.objects.all()
    return render(request, 'goods/items_list.html', context={'items_list': items})


def update_prices(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split()
            csv_reader = reader(price_str, delimiter=',', quotechar='"')
            count_updated = 0
            count_not_updated = 0
            new_codes_list = []
            for row in csv_reader:
                if row[1] not in models.Item.objects.values_list('code', flat=True):
                    new_codes_list.append(row[1])
                    models.Item.objects.create(name=row[0], code=row[1], price=row[2])
                if float(models.Item.objects.get(code=row[1]).price) != float(row[2]):
                    models.Item.objects.filter(code=row[1]).update(price=Decimal(row[2]))
                    count_updated += 1
                else:
                    count_not_updated += 1
            return HttpResponse(content=f'Цены были успешно обновлены. Количество обновленных товаров: {count_updated},'
                                        f'Не обновленных: {count_not_updated}, Новые артикли: {",".join(new_codes_list)}',
                                status=200)
    else:
        upload_file_form = UploadPriceForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)


def items_list(request):
    if request.method == 'GET':
        items_for_sale = [
            entities.Item(
                name='Кофеварка',
                description='Варит кофе',
                weight=100
            ),
            entities.Item(
                name='Беспроводные наушники',
                description='Можно послушать музыку',
                weight=150
            )
        ]
        return JsonResponse(ItemSerializer(entities.Item(
            name='Кофеварка',
            description='Варит кофе',
            weight=100
        )).data, safe=False)


class ItemList(APIView):
    def get(self, request):
        items = ItemNew.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ItemListNew(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = ItemNew.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = ItemNew.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, filter=None):
        return self.create(request)
