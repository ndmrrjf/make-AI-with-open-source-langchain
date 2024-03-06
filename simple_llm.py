import os
from langchain_openai import ChatOpenAI
import gradio as gr

# Memasukkan API key
os.environ["OPENAI_API_KEY"] = "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"

gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

def chatbot(Prompt):
    return gpt3.invoke(Prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)