import pika
import time

def process_message():
    # Verbindung zu RabbitMQ herstellen
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Queue deklarieren
    channel.queue_declare(queue='message_queue')

    def callback(ch, method, properties, body):
        message = body.decode()
        timestamp = time.time()
        new_message = f"{message} | Timestamp: {timestamp} | Processed by Container 2"
        print(f"Container 2: Nachricht empfangen: {message}")
        print(f"Container 2: Bearbeitete Nachricht: {new_message}")

        # Nachricht weiterleiten an Container 3
        channel.basic_publish(exchange='',
                              routing_key='message_queue',
                              body=new_message)

    channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)
    print('Container 2: Warten auf Nachrichten...')
    channel.start_consuming()

if __name__ == "__main__":
    process_message()
