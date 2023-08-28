from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def stars_display(rating_value):
    full_stars = int(rating_value)
    decimal_part = rating_value - full_stars
    empty_stars = 5 - full_stars - (1 if decimal_part >= 0.3 else 0)

    stars_html = ''.join([
        '<i class="fi fi-ss-star text-yellow-400"></i>' * full_stars,
        '<i class="fi fi-ss-star-sharp-half-stroke text-yellow-400"></i>' if decimal_part >= 0.3 else '',
        '<i class="fi fi-rs-star text-yellow-400"></i>' * int(empty_stars),
    ])

    return mark_safe(stars_html)