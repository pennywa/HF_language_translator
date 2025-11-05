# HF_language_translator

## 🌐 UN Official Language Translator

This Hugging Face Space provides quick, accessible translation services covering the six official languages of the United Nations : Arabic, Chinese, English, French, Russian, and Spanish.

## Link: https://huggingface.co/spaces/pennywa/language_translator

## 🌎 Supported Translations:
The application supports translation between English and the five other official languages in both directions (example: Spanish to English, or English to Spanish), as well as direct translation between two non-English languages (example: French to Spanish). 

## 🚀 How It Works

This app uses an API-based approach:
Reasoning: Applications that download and run massive machine learning models locally (often fail due to memory or time limits on the free CPU tier)

The deep-translator library supports several translation services. The API being used is the Google Translate service accessed via the GoogleTranslator class.

This allows for fast startup and reliable translation performance, regardless of the server capacity assigned to your space. 

1. When you click "Translate," the app sends a request to an external translation service
2. The service performs the translation and instantly returns the result to your Gradio interface.

## 🛠️ Required Files

The application requires only the essential files in the root directory:

* `app.py`: The main Python script defining the Gradio interface and translation logic.
* `requirements.txt`: Specifies the necessary dependencies: `gradio` and `deep-translator`.
  


