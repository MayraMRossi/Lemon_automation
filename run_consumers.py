from infrastructure.messaging.consumers.email_consumer import EmailConsumer
from infrastructure.messaging.consumers.intent_consumer import IntentConsumer
from infrastructure.messaging.consumers.rag_consumer import RAGConsumer

import threading

def start_email_consumer():
    consumer = EmailConsumer()
    consumer.start_consuming()

def start_intent_consumer():
    consumer = IntentConsumer()
    consumer.start_consuming()

def start_rag_consumer():
    consumer = RAGConsumer()
    consumer.start_consuming()

if __name__ == "__main__":
    email_thread = threading.Thread(target=start_email_consumer)
    intent_thread = threading.Thread(target=start_intent_consumer)
    rag_thread = threading.Thread(target=start_rag_consumer)

    email_thread.start()
    intent_thread.start()
    rag_thread.start()

    email_thread.join()
    intent_thread.join()
    rag_thread.join()