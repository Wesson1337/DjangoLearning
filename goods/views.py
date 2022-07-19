from csv import reader
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render
from goods.forms import UploadPriceForm
from goods.models import Item


def item_list(request):
    items = Item.objects.all()
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
                if row[1] not in Item.objects.values_list('code', flat=True):
                    new_codes_list.append(row[1])
                    Item.objects.create(name=row[0], code=row[1], price=row[2])
                if float(Item.objects.get(code=row[1]).price) != float(row[2]):
                    Item.objects.filter(code=row[1]).update(price=Decimal(row[2]))
                    count_updated += 1
                else:
                    count_not_updated += 1
            return HttpResponse(content=f'Цены были успешно обновлены. Количество обновленных товаров: {count_updated},'
                                        f'Необновленных: {count_not_updated}, Новые артикли: {",".join(new_codes_list)}',
                                status=200)
    else:
        upload_file_form = UploadPriceForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)
