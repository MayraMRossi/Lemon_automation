import pika
import json
from domain.models.task_models import TaskPayload

class TaskConsumer:
    def __init__(self, rabbitmq_url: str, task_handler):
        self.connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_url))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="tasks")
        self.task_handler = task_handler

    def start_consuming(self):
        self.channel.basic_consume(
            queue="tasks",
            on_message_callback=self._process_task,
            auto_ack=True
        )
        print("Starting task consumer...")
        self.channel.start_consuming()

    def _process_task(self, ch, method, properties, body):
        try:
            task_data = json.loads(body)
            task = TaskPayload.parse_obj(task_data)
            result = self.task_handler(task)
            print(f"Task processed successfully: {result}")
        except Exception as e:
            print(f"Error processing task: {e}")