from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def stars_display(rating_value):
    full_stars = int(rating_value)
    decimal_part = rating_value - full_stars
    half_star = 0.5 if rating_value - full_stars >= 0.25 else 0
    empty_stars = 5 - full_stars - (1 if decimal_part >= 0.25 else 0)

    stars_html = ''.join([
        '<i class="fi fi-ss-star text-lg text-orange-500"></i>' * full_stars,
        '<i class="fi fi-ss-star-sharp-half-stroke text-lg text-orange-500"></i>' if decimal_part >= 0.25 else '',
        '<i class="fi fi-rs-star text-lg text-orange-500"></i>' * int(empty_stars),
    ])

    return mark_safe(stars_html)