import requests
import json
import time


class SendReportMessage:
    @staticmethod
    def send_talk_message(data):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=13c296d9-ec40-4ecb-b7c7-d6720f9a4269'
        uploads = {"text": {"content": data}, "msgtype": "text"}
        response = requests.post(url=url, json=uploads)
        result = response.json()
        print(f'机器人消息发送结果：{result}')


if __name__ == "__main__":
    # 配置企业微信Webhook URL（必须替换为实际URL）
    WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=13c296d9-ec40-4ecb-b7c7-d6720f9a4269"
