import uuid
import time

from flask import Flask, request, jsonify
from flask.views import View
from pydantic import BaseModel

app = Flask(__name__)


class Message(BaseModel):
    uuid: uuid.UUID


class PayloadProcessor:
    validated_message = None

    def validate(self, message: dict):
        data = Message.model_validate(message)
        self.validated_message = data.model_dump()

    def process(self, message: dict):
        self.validate(message)

        time.sleep(3)  # simulation of I/O blocking operation (gevent monkey patches time.sleep to become green)

        # do some post-processing
        if str(self.validated_message["uuid"]) != str(message["uuid"]):
            print(f"ERROR IN DATA INTEGRITY {self.validated_message['uuid']} != {message['uuid']}")
        else:
            print(f"CORRECT DATA INTEGRITY {self.validated_message}")


class ProcessMessageView(View):
    processor = PayloadProcessor()

    def dispatch_request(self):
        self.processor.process(message=request.json)
        return jsonify(message="OK")


app.add_url_rule("/", view_func=ProcessMessageView.as_view("test_view"), methods=["POST"])
