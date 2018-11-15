import base64
import gzip
import http.client
import json

from util import BgColors


class ExchangeMsg:
    def __init__(self, name):
        self.vhost = "/"
        self.name = name
        self.properties = {}
        self.routing_key = None
        self.delivery_mode = 1
        self.payload = None
        self.headers = {}
        self.props = {}
        self.payload_encoding = "string"

    def set_routing_key(self, routing_key):
        self.routing_key = routing_key
        return self

    def set_payload(self, payload):
        self.payload = payload
        return self

    def build(self):
        return json.dumps(self.__dict__)


json_header = {
    'Content-Type': "application/json",
    'User-Agent': 'PostmanRuntime/7.3.0',
    'Accept': '*/*',
    'Host': "localhost:15672",
    'accept-encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}


class RabbitClient:

    def __init__(self, host, port, exchange_name, user_name, password):
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.exchange_name = exchange_name
        if not port:
            self.schema = 'https'
            self.port = 443
        else:
            self.schema = 'http'
            self.port = 15672

    @staticmethod
    def get_auth_header(user_name, password):
        _bytes = bytes('{}:{}'.format(user_name, password), 'utf-8')
        _value = base64.b64encode(_bytes).decode('utf-8')
        return "Basic {}".format(_value)

    def build_publish_url(self):
        return "/api/exchanges/{}/{}/publish".format("%2F", self.exchange_name)

    def publish_message(self, routing_key, message_body):
        msg = ExchangeMsg(self.exchange_name).set_routing_key(routing_key).set_payload(message_body).build()
        conn = http.client.HTTPConnection(self.host, self.port)
        json_header['Authorization'] = self.get_auth_header(self.user_name, self.password)
        conn.request('POST', self.build_publish_url(), msg, json_header)
        res = conn.getresponse()
        if res.code == 200:
            print(BgColors.BOLD + message_body + BgColors.ENDC)
            print(BgColors.BOLD + BgColors.OKGREEN, gzip.decompress(res.read()).decode('utf-8'), BgColors.ENDC)
        else:
            print(BgColors.BOLD, BgColors.FAIL, res.read().decode('utf-8'), BgColors.ENDC)


if __name__ == '__main__':
    client = RabbitClient("localhost", 15672, 'item-master-exchange-item-updated', 'guest', 'guest')
    client.publish_message('item-master-wh-item-data', 'hello world')
