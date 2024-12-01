import pika
import json

# Connexion au serveur RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Création de la queue
channel.queue_declare(queue='payment_queue')

# Données à envoyer
payment_data = {
    "PaymentID": "12345",
    "Amount": "200.75",
    "Currency": "EUR",
    "Payer": {
        "Name": "Alice Dupont",
        "Account": "FR7630006000011234567890189"
    },
    "Payee": {
        "Name": "Bob Martin",
        "Account": "BE68539007547034"
    }
}

# Envoi du message sous forme de JSON
channel.basic_publish(
    exchange='',
    routing_key='payment_queue',
    body=json.dumps(payment_data)
)

print("Message envoyé au consommateur.")
connection.close()
