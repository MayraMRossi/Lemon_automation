import pika
import json
from domain.models.task_models import TaskPayload

class TaskProducer:
    def __init__(self, rabbitmq_url: str):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="tasks")

    def publish_task(self, task: TaskPayload):
        self.channel.basic_publish(
            exchange="",
            routing_key="tasks",
            body=task.json()
        )