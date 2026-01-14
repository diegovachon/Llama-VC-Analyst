# Llama-VC-Analyst
This repository contains a full-stack ML pipeline for Venture Capitalist analysis. It features a Llama-3.2-3B SML fine-tuned via QLoRA on synthetic data. This model is run on Raspberry Pi 5 to generate structured investment memos. This project demonstrates how to create a private, low-latency "AI Analyst".

Project Goal

By converting raw startup descriptions into a structured investment memos (Problem, Solution, Market, Verdict) using a specialized local LLM, it reduces manual due diligence time.

Key Features

- Data Extraction: Scripts to process startup descriptions from GitHub and synthetic datasets (github_startups.csv)

- Fine-Tuning: Fine-tuning of Llama-3.2-3B using QLoRA (Quantized Low-Rank Adaptation) to specialize the model in financial analysis and structured reporting

- Edge Deployment: A fully offline inference engine running on Raspberry Pi 5 using Ollama

- Interactive UI: A generic Streamlit dashboard for real-time interaction with the model

Tech Stack

- Hardware: Raspberry Pi 5 (8GB RAM)

- Model: Llama-3.2-3B (Quantized)

- Training: PyTorch, PEFT (QLoRA), Transformers

- Inference: Ollama

- Interface: Streamlit (Python)

Repository Structure

- /data: Contains processed datasets used for training

- /extraction: Python scripts for cleaning startup data

- /fine-tuning: Jupyter notebook for fine-tuning Llama-3.2 using QLoRA

- /deploy: Streamlit application code and Ollama Modelfiles for the Raspberry Pi

