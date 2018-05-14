
# Login credentials
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

username= ""
apikey = ""

# Specify number to send to
to = "+254..."

# Message
message = "Hello, world"

# New gateway instance
gateway = AfricasTalkingGateway(username, apikey)

try:

    results = gateway.sendMessage(to, message)

    for recipient in results:
        print('number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                            recipient['status'],
                                                            recipient['messageId'],
                                                            recipient['cost']))
except AfricasTalkingGatewayException:
    print('Encountered an error while sending: %s' % str(AfricasTalkingGatewayException))
