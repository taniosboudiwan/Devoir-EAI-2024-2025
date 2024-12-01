import pika
import json
import xml.etree.ElementTree as ET

# Fonction pour écrire le fichier XML
def write_payment_request(data):
    root = ET.Element("PaymentRequest")
    ET.SubElement(root, "PaymentID").text = data["PaymentID"]
    ET.SubElement(root, "Amount").text = data["Amount"]
    ET.SubElement(root, "Currency").text = data["Currency"]

    payer = ET.SubElement(root, "Payer")
    ET.SubElement(payer, "Name").text = data["Payer"]["Name"]
    ET.SubElement(payer, "Account").text = data["Payer"]["Account"]

    payee = ET.SubElement(root, "Payee")
    ET.SubElement(payee, "Name").text = data["Payee"]["Name"]
    ET.SubElement(payee, "Account").text = data["Payee"]["Account"]

    # Écrire dans un fichier XML
    tree = ET.ElementTree(root)
    with open("PaymentRequest.xml", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)

    print("Fichier XML 'PaymentRequest.xml' créé.")

# Connexion au serveur RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Déclarer la queue
channel.queue_declare(queue='payment_queue')

# Fonction callback pour traiter les messages
def callback(ch, method, properties, body):
    print("Message reçu du producteur.")
    payment_data = json.loads(body)  # Convertir le message JSON en dict
    write_payment_request(payment_data)  # Écrire le fichier XML

# Consommation des messages
channel.basic_consume(queue='payment_queue', on_message_callback=callback, auto_ack=True)

print("En attente de messages. Appuyez sur Ctrl+C pour quitter.")
channel.start_consuming()
