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

@register.filter
def points_summation(obj_arr):
    try:
        return sum(getattr(item, "points") for item in obj_arr)
    except:
        return None

@register.filter
def width_giver(obj_arr, arg):
    try:
        return "width:" + str((int(arg)/sum(getattr(item, "points") for item in obj_arr))*100) + "%"
    except:
        return None