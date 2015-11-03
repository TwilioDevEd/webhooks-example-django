from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from twilio import twiml


@require_POST
@csrf_exempt
def incoming_call(request):
    """Twilio Voice URL - receives incoming calls from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    resp.say("Thanks for calling! I got your call because of Twilio's webhook. Goodbye!")

    # Return the TwiML
    return HttpResponse(resp)

@require_POST
@csrf_exempt
def incoming_message(request):
    """Twilio Messaging URL - receives incoming messages from Twilio"""
    # Create a new TwiML response
    resp = twiml.Response()

    # <Say> a message to the caller
    resp.message("Thanks for your text! Webhooks are neat :)")

    # Return the TwiML
    return HttpResponse(resp)
