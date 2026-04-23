# Feedback Dynamics in Agentic LLM-Based Text Accessibility

This is the repository of the study published in AIED 2026:  
📄 **“Feedback Dynamics in Agentic LLM-Based Text Accessibility”**  
by Eleni Ilkou, Maria Angela Pellegrino, and Olga Viberg.

- L3S Research Center, Leibniz University Hannover, Germany  
- University of Salerno, Italy  
- KTH Royal Institute of Technology, Sweden  

---

## 📌 Project Summary

This project investigates **feedback dynamics in agentic large language models** when applied to **text accessibility tasks**.

It focuses on how iterative feedback mechanisms can influence accessibility-oriented text rewriting in LLM systems.

The study examines:

- Agentic LLM-based text refinement loops  
- Accessibility-aware rewriting behavior  
- Feedback-driven optimization of generated text  
- Stability and quality of iterative model outputs  

This work provides a structured analysis of how feedback signals affect accessibility outcomes in modern language models.

---

## 🔬 Research Context

- Feedback-driven behavior in agentic LLM systems  
- Accessibility evaluation in iterative feedback pipelines  
- Alignment of LLM outputs with accessibility requirements  

---

## Repository structure

## 📁 src/
Contains all source code for the project.
- `agent.py`: main entry point for running the pipeline.
- `prompter.py`: task specification, prompts and connection with LLM.
- `checker.py`: formative assessment, checks on long phrases and factual drift.
- `judge.py`: feedback policy, learning analytic metrics on readability and dyslexia acceessibility.

## 📁 data/
Contains the input data used in the experiments.
- `chapters.json`: the dataset of text chapters.

## 📁 results/
Contains the outputs produced by the system, including computed metrics and analysis results.

---

## ▶️ How to Run

Make sure you have Python installed and an OpenAI key to be added in `prompter.py`.  
Run the main pipeline using:

```bash
python src/agent.py data/chapters.json YOUR-EXPORT.json
