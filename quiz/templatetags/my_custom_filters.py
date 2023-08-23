from django import template
import math

register = template.Library()

QUESTIONS_PER_SET = 3

@register.filter
def divide(value):
    try:
        return math.ceil(int(value) / QUESTIONS_PER_SET)
    except (ValueError, ZeroDivisionError):
        return None
    
@register.filter
def user_set(points):
    try:
        return math.floor(int(points)/ QUESTIONS_PER_SET) + 1
    except (ValueError, ZeroDivisionError):
        return None