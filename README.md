# HF_language_translator

## 🌐 UN Official Language Translator

This Hugging Face Space provides quick, accessible translation services covering the six official languages of the United Nations : Arabic, Chinese, English, French, Russian, and Spanish.

## 🚀 How It Works

This application utilizes Helsinki-NLP Opus-MT transformer models for machine translation.

## Supported Translations:
The application supports translation between English and the five other official languages in both directions (e.g., Spanish to English, or English to Spanish).

English is used as the pivot language. 
Direct translation between two non-English languages (e.g., Arabic to Chinese) is currently not supported in this simplified setup.

## 🔧 Setup & Dependencies

The application relies on the following packages, defined in the requirements.txt file:
gradio
transformers
torch
