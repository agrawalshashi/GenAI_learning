# 🧠 GenAI Learning

A hands-on repository documenting my journey into **Generative AI, Transformers, and NLP** through practical implementations and projects.

This repository focuses on understanding the concepts behind modern Generative AI systems and turning those concepts into working applications.

---

## 🚀 What I'm Learning

* 🧠 Generative AI fundamentals
* 🤗 Transformers
* 🔤 Natural Language Processing (NLP)
* 📝 Text Summarization
* 🔥 Transfer Learning
* ⚙️ Fine-tuning Transformer models
* 🚀 Model deployment with FastAPI
* 🐍 PyTorch
* 🤗 Hugging Face Transformers

---

## 📌 Featured Project

### 📝 Text Summarization using T5

A complete end-to-end text summarization project built using the **T5 (Text-to-Text Transfer Transformer)** architecture.

The project covers the complete workflow:

```text
Dataset
   ↓
Data Cleaning & Preprocessing
   ↓
Tokenization
   ↓
T5 Fine-Tuning
   ↓
Model Evaluation
   ↓
Saved Transformer Model
   ↓
FastAPI Backend
   ↓
Web Interface
```

### 📊 Dataset

The model is trained using the **SAMSum dataset**, which contains conversational dialogues along with their corresponding summaries.

Files included:

* `samsum-train.csv`
* `samsum-validation.csv`
* `samsum-test.csv`

---

## 🤖 Model

The project uses:

**T5 — Text-to-Text Transfer Transformer**

The model is fine-tuned specifically for the task of dialogue summarization.

The training workflow is implemented in:

```text
text_summarizer.ipynb
```

The trained model and tokenizer are saved locally and then used by the FastAPI application for inference.

---

## 📓 Jupyter Notebook

The notebook contains the complete machine learning workflow:

* Dataset loading
* Exploratory understanding of the data
* Data preprocessing
* Text cleaning
* Tokenization
* Train/validation preparation
* T5 model loading
* Fine-tuning
* Training configuration
* Model generation
* Summary generation
* Saving the trained model

### Notebook

```text
text_summarizer.ipynb
```

---

## ⚡ FastAPI Application

After training the Transformer model, I built a **FastAPI application** to serve the model.

The application accepts dialogue as input and generates a concise summary using the fine-tuned T5 model.

### FastAPI Structure

```text
TextSummarizerApp/
│
├── app.py
├── index.html
└── saved_summary_model/
```

### API Endpoint

```text
POST /summarize/
```

Example request:

```json
{
    "dialogue": "Your conversation text goes here..."
}
```

Example response:

```json
{
    "summary": "Generated summary..."
}
```

---

## 🌐 Web Interface

The project also includes a simple HTML interface through which users can interact with the summarization application.

```text
index.html
```

The interface is connected to the FastAPI backend and allows users to provide dialogue for summarization.

---

## 🛠️ Tech Stack

| Technology                | Purpose                   |
| ------------------------- | ------------------------- |
| Python                    | Core programming language |
| PyTorch                   | Deep learning framework   |
| Hugging Face Transformers | T5 model & tokenizer      |
| T5                        | Text summarization        |
| Pandas                    | Dataset processing        |
| NumPy                     | Numerical operations      |
| FastAPI                   | Backend API               |
| Jinja2                    | HTML templating           |
| HTML/CSS                  | Web interface             |
| Jupyter Notebook          | Model development         |

---

## 📂 Repository Structure

```text
GenAI_learning/
│
├── text_summarizer.ipynb
│
├── samsum-train.csv
├── samsum-validation.csv
├── samsum-test.csv
│
├── saved_summary_model/
│
├── TextSummarizerApp/
│   ├── app.py
│   ├── index.html
│   └── saved_summary_model/
│
├── results/
│
└── .gitignore
```

> Some large model files and generated training artifacts are excluded using `.gitignore`.

---

## 🔄 Project Workflow

```text
                SAMSum Dataset
                       │
                       ▼
              Data Preprocessing
                       │
                       ▼
                  Tokenization
                       │
                       ▼
                T5 Fine-Tuning
                       │
                       ▼
                Trained Model
                       │
                       ▼
             Saved Model & Tokenizer
                       │
                       ▼
                  FastAPI API
                       │
                       ▼
                 Web Interface
                       │
                       ▼
                Generated Summary
```

---

## 🎯 Learning Outcomes

Through this project, I worked with the complete lifecycle of a Transformer-based Generative AI application:

* Understanding Transformer-based NLP models
* Working with the T5 architecture
* Preparing conversational datasets
* Tokenizing text for Transformer models
* Fine-tuning a pretrained model
* Generating text using beam search
* Saving and loading trained models
* Building an inference pipeline
* Creating REST APIs with FastAPI
* Connecting a frontend with a machine learning backend
* Structuring a Generative AI project for deployment

---

## 🔮 Future Improvements

Some possible improvements for this project:

* [ ] Add ROUGE-based evaluation
* [ ] Improve the frontend UI
* [ ] Add configurable summary length
* [ ] Add batch summarization
* [ ] Add Docker support
* [ ] Deploy the FastAPI application
* [ ] Add API documentation examples
* [ ] Experiment with other Transformer architectures
* [ ] Compare different summarization models

---

## 📚 Learning Journey

This repository is part of my ongoing journey into **Generative AI and Deep Learning**.

I am building projects step-by-step to move from understanding individual concepts to developing complete AI applications.

```text
NLP
 ↓
Transformers
 ↓
T5
 ↓
Fine-Tuning
 ↓
Text Generation
 ↓
Generative AI Application
 ↓
FastAPI Deployment
```

---

## 👨‍💻 Author

### Shashi Agrawal

AI/ML Engineer in Progress
Exploring **Machine Learning · Deep Learning · Generative AI · NLP · Transformers**

🔗 **GitHub:** [agrawalshashi](https://github.com/agrawalshashi)

---

⭐ If you find this repository useful, feel free to explore the projects and follow the learning journey.
