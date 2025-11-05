import gradio as gr
from deep_translator import GoogleTranslator

# Dictionary mapping language names to their ISO 639-1 codes 
# GoogleTranslator uses standard codes, including simplified Chinese (zh-CN)
LANGUAGE_MAP = {
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-CN", 
    "English": "en",
    "French": "fr",
    "Russian": "ru",
    "Spanish": "es" 
}
LANGUAGE_OPTIONS = list(LANGUAGE_MAP.keys())

def translate_text(input_text, src_lang_name, tgt_lang_name):
    if not input_text:
        return "", "Please enter text to translate."

    if src_lang_name == tgt_lang_name:
        return input_text, "Source and Target languages are the same."

    src_code = LANGUAGE_MAP.get(src_lang_name)
    tgt_code = LANGUAGE_MAP.get(tgt_lang_name)

    if not src_code or not tgt_code:
        return "", "Invalid language selection."

    try:
        translator = GoogleTranslator(source=src_code, target=tgt_code)
        
        translated_text = translator.translate(input_text)
        
        return translated_text, "Translation successful."
        
    except Exception as e:
        return "", f"Translation failed during execution: {e}"

# Define Gradio Interface
with gr.Blocks(title="UN Official Language Translator", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
    """
    # 🌐 UN Official Language Translator
    
    This app supports translation between the six official languages of the UN: 
    **Arabic, Chinese, English, French, Russian, and Spanish**.
    """
    )

    with gr.Row():
        source_lang = gr.Dropdown(
            label="Source Language",
            choices=LANGUAGE_OPTIONS,
            value="English",
            scale=1
        )
        target_lang = gr.Dropdown(
            label="Target Language",
            choices=LANGUAGE_OPTIONS,
            value="French",
            scale=1
        )

    input_text = gr.Textbox(
        label="Input Text", 
        placeholder="Enter the text you want to translate...", 
        lines=4
    )
    
    translate_button = gr.Button("Translate", variant="primary")
    
    output_text = gr.Textbox(
        label="Translated Output", 
        interactive=False, 
        lines=4
    )
    
    status_message = gr.Textbox(label="Status", interactive=False, value="Ready to translate.")
    
    translate_button.click(
        fn=translate_text, 
        inputs=[input_text, source_lang, target_lang], 
        outputs=[output_text, status_message]
    )

    if __name__ == "__main__":
        demo.launch(server_name="0.0.0.0", server_port=7860)