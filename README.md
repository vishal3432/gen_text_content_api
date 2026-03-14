# Gen-Text Content API (Django + NLP)

An end-to-end **AI text generation API** built using Python, Django REST Framework, and transformer-based language models.

This project allows users to send a **topic or prompt** to an API endpoint and receive **AI-generated blog content** or text responses.

The system integrates Natural Language Processing techniques with modern transformer models to demonstrate practical **Generative AI backend engineering**.

---

# Project Overview

The goal of this project is to design and implement a **production-style NLP service** that generates structured text content using a pretrained language model.

Instead of training a heavy model locally, the project uses **DistilGPT2**, a lightweight version of **GPT-2**, loaded through the **Hugging Face Transformers** library.

This makes the project:

* lightweight
* faster to run on a laptop
* production-friendly
* easier for recruiters to test

---

# Features

• AI text generation API
• Django REST backend
• Transformer-based NLP model
• Prompt-based content generation
• Clean modular project structure
• Dataset preprocessing pipeline
• Professional GitHub project structure

---

# Tech Stack

Language

* Python

Framework

* Django
* Django REST Framework

Machine Learning / NLP

* Transformers
* PyTorch
* NLTK

Tools

* Pandas
* Git
* Virtual Environment

---

# Model Used

This project uses **DistilGPT2**, a distilled version of **GPT-2**.

Reasons for choosing DistilGPT2:

* Smaller model size
* Faster inference
* Lower memory usage
* Suitable for local development

The model is loaded using **Hugging Face Transformers**.

---

# Dataset

The dataset used in this project contains Medium blog articles with metadata such as title, subtitle, reading time, and claps. ([Baselight][1])

Example columns:

* id
* url
* title
* subtitle
* claps
* reading_time
* publication
* date

Dataset Download Link:

https://www.kaggle.com/datasets/arnabchaki/medium-articles-dataset

The dataset is not included in the repository because GitHub has a **100MB file size limit**.

---

# Data Loading

Dataset is loaded using Pandas.

Example:

```python
import pandas as pd

df = pd.read_csv("dataset/blog_dataset.csv")

df["text"] = df["title"] + " " + df["subtitle"].fillna("")
```

---

# Project Structure

```
gen-text-content-api
│
├── backend
│   ├── api
│   │   ├── views.py
│   │   ├── urls.py
│   │
│   ├── settings.py
│
├── ml_model
│   └── generator.py
│
├── dataset
│   └── blog_dataset.csv   (ignored in git)
│
├── requirements.txt
├── README.md
└── manage.py
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/gen-text-content-api.git
```

Move into the project directory

```
cd gen-text-content-api
```

Create a virtual environment

```
python -m venv venv
```

Activate virtual environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Project

Start the Django server:

```
cd backend
python manage.py runserver
```

The API will run on

```
http://127.0.0.1:8000
```

---

# Example API Request

Endpoint

```
POST /api/generate
```

Example request body

```
{
 "prompt": "Write a blog introduction about artificial intelligence"
}
```

Example response

```
{
 "generated_text": "Artificial intelligence is transforming the way businesses operate..."
}
```

---

# Problems Faced During Development

This project involved solving multiple real-world engineering problems.

1️⃣ GitHub file size limit

Dataset size was 763MB which exceeded GitHub's 100MB limit.

Solution:

* Added dataset to `.gitignore`
* Removed dataset from Git history

---

2️⃣ Dataset column mismatch

Error:

```
KeyError: 'text'
```

Cause:
Dataset did not contain a column named `text`.

Solution:
Combined `title` and `subtitle` columns.

---

3️⃣ Memory errors during model training

Error:

```
pyarrow.lib.ArrowMemoryError
```

Cause:
Large dataset processing exceeded available RAM.

Solution:
Used pretrained transformer model instead of training locally.

---

4️⃣ Module import errors

Error:

```
ModuleNotFoundError: No module named ml_model
```

Solution:
Corrected Python module structure and imports.

---

5️⃣ Hugging Face model loading errors

Error related to model path and repository ID.

Solution:
Loaded pretrained models directly using Transformers.

---

# Future Improvements

Possible extensions to this project:

* Add Swagger API documentation
* Implement prompt temperature control
* Deploy API using Docker
* Add frontend interface
* Use larger LLMs for improved generation
* Implement text summarization and sentiment analysis

---

# Author

Vishal Singh
Aspiring Python Developer / AI Developer

GitHub
https://github.com/vishal3432

LinkedIn
https://www.linkedin.com/in/vishal3432

---

# License

This project is for educational and portfolio purposes.

[1]: https://baselight.app/u/kaggle/dataset/arnabchaki_medium_articles_dataset?utm_source=chatgpt.com "Medium Articles Dataset 📝 by Kaggle | Media and Entertainment Data | Baselight"
