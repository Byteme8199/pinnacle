from django.template import Library

from workoutsheet.models import WorkoutSheet

register = Library()

@register.filter
def get_range(value):
	"""
	Filter - returns a list containing range made from given value
	Usage (in template):

	<ul>{% for i in 3|get_range %}
	  <li>{{ i }}. Do something</li>
	{% endfor %}</ul>

	Results with the HTML:
	<ul>
	  <li>0. Do something</li>
	  <li>1. Do something</li>
	  <li>2. Do something</li>
	</ul>

	Instead of 3 one may use the variable set in the views
	"""
	if value:
		return range(value)
	else:
		pass
	
@register.filter(name='in_year')
def in_year(self, set):
	set = set.split(",")
	cat = set[1]
	year = set[0]
	yearstart = year + "-01-01" 
	yearend = year + "-12-31" 
	return WorkoutSheet.objects.filter(start_date__range=[yearstart, yearend], exercise_category=cat)

@register.filter(name='truncate')
def truncate(self, num):
	num = num.split(",")
	return num[0]