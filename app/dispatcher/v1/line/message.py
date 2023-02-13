from linebot.models import MessageEvent, TextMessage, TextSendMessage

from app.dispatcher.v1.chatgpt import get_response

from .line import linebot_api
from .line import webhook_handler as handler


@handler.add(MessageEvent, message=(TextMessage))
def handling_message(event):
    if isinstance(event, MessageEvent) and \
        isinstance(event.message, TextMessage):
        messages = event.message.text

        # echo_messages = TextSendMessage(text=messages)
        reply_messages = TextSendMessage(text=get_response(messages))
        linebot_api.reply_message(
            reply_token=event.reply_token,
            messages=reply_messages,
        )

    return "OK"
