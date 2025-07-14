# Dyslexia and AI

This is the repository of the proof-of-concept study published in AIED 2025:  
📄 *“Dyslexia and AI: Do Language Models Align with Dyslexic Style Guide Criteria?”*  
by Eleni Ilkou, Thomai Alexiou, Grigoris Antoniou, and Olga Viberg.

- L3S Research Center, Leibniz University Hannover, Germany  
- Aristotle University of Thessaloniki, Greece  
- Leeds Beckett University, UK  
- KTH Royal Institute of Technology, Sweden

## 📣 News

⭐ Our paper has been **[nominated for the Best Paper Award](https://aied2025.itd.cnr.it/index.php/program/main-track-best-papers-nominees/)** at the  
**26th International Conference on Artificial Intelligence in Education (AIED 2025).**

We are honored by this recognition and grateful to the community! 🙏

## Project Summary

This project uses **DysText**, a novel metric designed to evaluate and quantify the dyslexia-friendliness of text outputs, particularly from language models (LMs). It is built on accessibility principles from the **[British Dyslexia Association’s Dyslexia Style Guide](https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf?v=1680514568)** and aims to support research into how well AI systems adhere to these criteria.

The study critically assesses popular LLMs on their ability to:
- Identify dyslexia-relevant stylistic features
- Generate accessible, dyslexia-friendly content

## 🔬 Research Context

- LMs knowledge of dyslexia-friendly criteria in text _(Go to [data/RQ1](https://github.com/eilkou/DysText/tree/main/data/RQ1))_
- A custom metric for measuring dyslexia-friendliness in text 
- Implementation based on the British Dyslexia Association’s Style Guide
- Proof-of-concept evaluation of LLM outputs _(Check our paper)_
- Easily extensible and open-source

For more context, please refer to the [original paper](https://github.com/eilkou/DysText/blob/main/_AIED25__Dyslexia___AI___Camera_ready.pdf)


## 🛠️ Usage of DysText

Clone the repository:

```bash
git clone https://github.com/eilkou/DysText.git
cd DysText
```

### Requirements
- Python ≥ 3.11
  
Install packages:

```bash
pip install -r requirements.txt
```

Run DysText:

```bash
python src/main.py
```


## How to Cite
**BibTeX:**
```bibtex
@inproceedings{ilkou2025dyslexia,
  author    = {Eleni Ilkou and Thomai Alexiou and Grigoris Antoniou and Olga Viberg},
  title     = {Dyslexia and AI: Do Language Models Align with Dyslexic Style Guide Criteria?},
  booktitle = {Proceedings of the 26th International Conference on Artificial Intelligence in Education (AIED)},
  year      = {2025}
}
```

## ✉️ Contact

**Lead author:** Eleni Ilkou  

**Email:** eleni(dot)ilkou(at)tib.eu

**GitHub:** [@eilkou](https://github.com/eilkou)

**LinkedIn:**  [@eilkou](https://www.linkedin.com/in/eilkou/)
