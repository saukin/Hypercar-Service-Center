from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponse


menu = {'change_oil' : "Change oil", 'inflate_tires' : "Inflate tyres", 'diagnostic' : "Diagnostics",}
# print(menu[1])


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/menu.html", context={"menu": menu})


class TicketView(TemplateView):
    template_name = "tickets/get_ticket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        n_ticket = kwargs['n_ticket']
        context['n_ticket'] = n_ticket
        context['service'] = menu[n_ticket]
        return context
