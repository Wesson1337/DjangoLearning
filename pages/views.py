import datetime
from time import sleep
from django.shortcuts import render
from django.utils.formats import date_format
from django.utils.translation import gettext


def translation_example(request, *args, **kwargs):
    sleep(4)
    greetings_message = gettext('Hello there! Today is %(date)s %(time)s') % {
        'date': date_format(datetime.datetime.now().date(), use_l10n=True, format='SHORT_DATE_FORMAT'),
        'time': datetime.datetime.now().time()
    }
    return render(request, 'pages/translation_example.html', context={
        'greetings_message': greetings_message
    })
