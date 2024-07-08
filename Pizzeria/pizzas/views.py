from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pizza, Topping
from .forms import CommentForm

# Create your views here.
def pizzas(request):
  pizza_list = Pizza.objects.all().values()
  template = loader.get_template('all_pizzas.html')
  context = {
    'pizza_list': pizza_list,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  pizza = Pizza.objects.get(id=id)
  pizza_toppings = pizza.topping_set.all()
  comments = pizza.comment_set.all()

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # Don't save yet
        comment.pizza = pizza  # Associate comment with the current pizza
        comment.save()
  else:
    form = CommentForm()


  template = loader.get_template('details.html')
  context = {
    'pizza': pizza,
    'pizza_toppings': pizza_toppings,
    'comments': comments,
    'form': form,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())