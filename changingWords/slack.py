from slackclient import SlackClient

class slack:
    def __init__(self, slack_token):
        self.slack_token = slack_token

    def send_message(self):
        try:
            sc = SlackClient(self.slack_token)
            response = sc.api_call("chat.postMessage", channel="#" + channel, text=message, as_user=True)

            if response["ok"] == False:
                print("Cannot send message. Error: " + response["error"])
        except:
            print("Invalid token")