from deliverer import Deliverer
from common.enum import HttpMethods
from os import environ

class Notifier(Deliverer):
    @staticmethod
    def _make_message_from_req(request):
        user_name = request.POST.get('user_name', '')
        text = request.POST.get('text', '')
        return "各自slackを確認してください。\n発言者 {}\n内容 : {}".format(user_name, text)

    @staticmethod
    def slack_to_line(request):
        to = 'notify-api.line.me/api/notify'
        method = HttpMethods.POST
        params = {
            'message' : Notifier._make_message_from_req(request)
        }
        headers = {
            'Authorization' : {
                'Bearer' : environ('LINE_TOKEN')
            },
            'Content-Type' : 'application/x-www-form-urlencoded',
        }
        return Notifier.send(request, to, method, params, headers=headers, is_secure=True)
