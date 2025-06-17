from django.http import HttpResponse


class StipeWH_Handler:
    """ Handle Stripe webhools """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknow unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
