from django import template
from jalali_date import date2jalali , datetime2jalali
from jdatetime import date
register = template.Library()

@register.filter('jdate')
def jalali_date(value):
    return date2jalali(value)


@register.filter('jtime')
def jalali_datetime(value):
    return datetime2jalali(value).strftime(' %H:%M:%S')


@register.filter('number_digits')
def digits(value):
    return '{:,}'.format(value)
