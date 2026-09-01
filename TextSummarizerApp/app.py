# fastapi
from fastapi import FastAPI, Request
from pydantic import BaseModel 
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates  # UI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 

# initialize our fastapi app
app = FastAPI(
    title="Text Summarizer App",
    description="Text Summarization using T5",
    version="1.0"
)

# load our model & tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

# templating
templates = Jinja2Templates(directory=".")

# Input schema for dialogue => string
class DialogueInput(BaseModel):
    dialogue: str


def clean_data(text):
    text = re.sub(r"\r\n", " ", text)  # remove lines
    text = re.sub(r"\s+", " ", text)   # remove spaces
    text = re.sub(r"<.*?>", " ", text) # remove html tags
    text = text.strip().lower()
    return text


def summarize_dialogue(dialogue: str) -> str:
    dialogue = clean_data(dialogue)  # clean

    # Tokenize
    inputs = tokenizer(
        dialogue,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # Generate summary
    model.to(device)

    targets = model.generate(
        input_ids=inputs["input_ids"],          # ✅ FIXED
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )

    # Decode token IDs into text
    summary = tokenizer.decode(
        targets[0],
        skip_special_tokens=True
    )

    return summary


# API Endpoints
@app.post("/summarize/")
async def create_item(item: DialogueInput):
    summary = summarize_dialogue(item.dialogue)
    return {
        "summary": summary
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
