from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.http.response import HttpResponse

from .tickets_logic import tickets, menu, get_waiting_time, _all, get_next, do_next


def increase_t_number(service_type):
    if tickets[service_type] is not None:
        tickets[service_type] = tickets[service_type] + 1


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "tickets/menu.html", context={"menu": menu, "tickets": tickets})


class TicketView(TemplateView):
    template_name = "tickets/get_ticket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        n_ticket = kwargs['n_ticket']
        context['n_ticket'] = n_ticket
        context['service'] = menu[n_ticket]
        context['wait_time'] = get_waiting_time(context['service'])
        _all[0] += 1
        tickets[menu[n_ticket]][0] += 1
        tickets[menu[n_ticket]][1].append(_all[0])
        context['tNumber'] = _all[0]

        return context


class OperatorView(TemplateView):
    template_name = "tickets/operator menu.html"

    def get_context_data(self, **kwargs):
        context={'queue': tickets,}
        return context

    def post(self, request, *args, **qwargs):
        do_next()
        return redirect("/next")


class NextView(View):
    # template_name = "tickets/next.html"
    #
    # def get_context_data(self, **kwargs):
    #     _next = get_next()
    #     if _next < 1:
    #         next_text = "Waiting for the next client"
    #     else:
    #         next_text = _next
    #     context = {'next': next_text}
    #     return context

    def get(self, request, *args, **kwargs):
        _next = get_next()
        if _next < 1:
            next_text = "Waiting for the next client"
        else:
            next_text = f'Next ticket #{_next}'
        context = {'next': next_text}
        return render(request, "tickets/next.html", context=context)
