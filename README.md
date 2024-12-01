# RabbitMQ Producer and Consumer Example

This project demonstrates a basic producer-consumer pattern using RabbitMQ, where a producer sends payment data in JSON format to a RabbitMQ queue, and a consumer retrieves the data and converts it into an XML file.

---

## Scripts Overview

### `producer.py`
- **Purpose**: Sends payment data as a JSON message to a RabbitMQ queue named `payment_queue`.
- **Key Features**:
  - Establishes a connection with RabbitMQ.
  - Sends payment information, including details about the payer and the payee.
- **Data Example**:
  ```json
  {
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

  ### `consumer.py`
- **Purpose**: Receives the JSON message from the `payment_queue` and saves it as an XML file.
- **Key Features**:
  - Listens for messages on the `payment_queue`.
  - Converts the received JSON data into an XML format.
  - Saves the XML data to a file named `PaymentRequest.xml`.
- **Output Example**:
  ```xml
<?xml version='1.0' encoding='utf-8'?>
<PaymentRequest>
    <PaymentID>12345</PaymentID>
    <Amount>200.75</Amount>
    <Currency>EUR</Currency>
    <Payer>
        <Name>Alice Dupont</Name>
        <Account>FR7630006000011234567890189</Account>
    </Payer>
    <Payee>
        <Name>Bob Martin</Name>
        <Account>BE68539007547034</Account>
    </Payee>
</PaymentRequest>

