
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model=OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    prompt= ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results =[]

    for i, chunk in enumerate(dom_chunks, start=1):
        response= chain.invoke(
            {"dom_content": chunk,"parse_description":parse_description}
        )

        print(f"Parsed batch {i} of {len(dom_chunks)}")

        parsed_results.append(response)

    return "\n".join(parsed_results)
"""
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# ✅ Load API Key
GEMINI_API_KEY = os.getenv("AIzaSyDXwXkdwMe1DrnwTvXSJlLO6fuBCRrSLUU")
if not GEMINI_API_KEY:
    raise ValueError("❌ Google Gemini API Key not found. Set GEMINI_API_KEY in environment variables.")

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# ✅ Initialize Gemini API Model
model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

def parse_with_gemini(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )

        print(f"Parsed batch {i} of {len(dom_chunks)}")

        parsed_results.append(response)

    return "\n".join(parsed_results)
"""