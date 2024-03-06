import gradio as gr
from langchain.prompts import PromptTemplate
import os
from langchain_openai import ChatOpenAI

openai_api_key = "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"
os.environ["OPENAI_API_KEY"] = openai_api_key

# Mendefinisikan model AI
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key= openai_api_key
)

# Mendefinisikan PromptTemplate sebagai format prompt untuk input dari user
prompt = PromptTemplate(
    input_variables=["nama", "posisi", "perusahaan", "keterampilan"],
    template="Kepada yang terhormat \nHRD Manajer {perusahaan},\n\nDengan surat ini, saya {nama}, ingin melamar untuk posisi {posisi} di {perusahaan}. \n\nSaya memiliki pengalaman di bidang {keterampilan}. \n\nTerima kasih telah mempertimbangkan lamaran saya.\n\nHormat saya,\n{nama}",
)

# Define a function to generate a cover letter using the llm and user input
def generate_cover_letter(nama: str, posisi: str, perusahaan: str, keterampilan: str) -> str:
    formatted_prompt = prompt.format(nama=nama, posisi=posisi, perusahaan=perusahaan, keterampilan=keterampilan)
    response = llm.invoke(formatted_prompt).content
    return response

# Define the Gradio interface inputs
inputs = [
    gr.Textbox(label="Nama"),
    gr.Textbox(label="Posisi"),
    gr.Textbox(label="Perusahaan"),
    gr.Textbox(label="Keterampilan")
]

# Define the Gradio interface output
output = gr.Textbox(label="Template Surat")

# Launch the Gradio interface
gr.Interface(fn=generate_cover_letter, inputs=inputs, outputs=output).launch(share=True)