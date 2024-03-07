# WhatsApp ChatGPT Integration

This project enables you to interact with OpenAI's ChatGPT model via WhatsApp. By connecting WhatsApp with the ChatGPT API, you can send messages to a WhatsApp number, which are then processed by ChatGPT to generate responses.

## Features

- Send messages to a WhatsApp number to initiate conversations with ChatGPT.
- Receive responses from ChatGPT directly on WhatsApp.
- Easy setup and integration with Twilio for WhatsApp API.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository.
2. Set up a Twilio account and obtain your Twilio API credentials.
3. Set up an OpenAI account and obtain your OpenAI API key.
4. Configure your environment variables with your API credentials.
5. Install the required dependencies using `pip install -r requirements.txt`.
6. Run the Flask application using `python3 app.py`.
7. Set up ngrok to expose your local server to the internet.
8. Configure your Twilio account to use the ngrok URL as the webhook for incoming messages.

## Usage

Once the setup is complete, you can start sending messages to the WhatsApp number connected to the Twilio account. ChatGPT will process your messages and generate responses, which will be sent back to you via WhatsApp.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
