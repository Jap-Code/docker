import pika
import time

def send_message():
    # Verbindung zu RabbitMQ herstellen
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Queue erstellen
    channel.queue_declare(queue='message_queue')

    message = "Hello from Container 1"
    channel.basic_publish(exchange='',
                          routing_key='message_queue',
                          body=message)

    print(f"Container 1: Nachricht gesendet: {message}")
    connection.close()

if __name__ == "__main__":
    send_message()


