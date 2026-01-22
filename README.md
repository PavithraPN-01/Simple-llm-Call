# AI Text Generation with DistilGPT2

This project demonstrates a simple implementation of text generation using the Hugging Face `transformers` library. It utilizes the **DistilGPT2** model—a smaller, faster, and more light-weight version of GPT-2—to generate coherent text sequences based on a provided prompt.

## 🚀 Features
* **Model:** DistilGPT2 (82M parameters).
* **Pipeline:** Uses the Hugging Face `text-generation` pipeline for easy inference.
* **Customization:** Configured with repetition penalties and sequence limits to ensure high-quality output.

## 🛠️ Prerequisites

Before running the script, ensure you have Python 3.8+ installed. You will also need to install the following dependencies:

```bash
pip install transformers torch

