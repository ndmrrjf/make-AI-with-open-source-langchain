import gradio as gr
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

# Mengatur LLM
os.environ["OPENAI_API_KEY"] = "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"
llm = ChatOpenAI(temperature=0.9)

def handle_complaint(komplain: str) -> str:
    #Buat instance LLM dengan nilai temprature 0,9 (nilai lebih tinggi membuat keluaran lebih acak).
    

    # Merancang template untuk merespon komplain
    prompt = PromptTemplate(input_variables=["komplain"], template="Saya seorang perwakilan layanan pelanggan. Saya menerima keluhan berikut: {komplain}. Respon saya adalah:")

    # Membuat model bahasa berantai dengan template yang telah dirancang
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(komplain)

# Membuat antarmuka Gradio untuk fungsi handle_complaint
iface = gr.Interface(fn=handle_complaint, inputs="text", outputs="text")
iface.launch(share=True)