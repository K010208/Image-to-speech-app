import gradio as gr
from transformers import pipeline

# Step 1: Load models
image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
text_to_speech = pipeline("text-to-speech", model="facebook/fastspeech2-en-ljspeech")

# Step 2: Define function
def describe_and_speak(image):
    caption = image_to_text(image)[0]['generated_text']
    speech = text_to_speech(caption)
    return caption, (speech["audio"], speech["sampling_rate"])

# Step 3: Gradio interface
iface = gr.Interface(
    fn=describe_and_speak,
    inputs=gr.Image(type="pil"),
    outputs=[gr.Textbox(label="Caption"), gr.Audio(label="Speech")],
    title="🖼️ Image to Speech AI",
    description="Upload any image — the AI will describe it and read the description aloud!"
)

iface.launch()
