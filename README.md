### 📝 nlp-bert-finetuning
### 어텐션(Attention) 메커니즘의 이해와 BERT 모델 구현

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

---

## 📌 프로젝트 개요 (Project Overview)
본 프로젝트는 트랜스포머(Transformer)의 핵심인 셀프 어텐션(Self-Attention) 구조를 파악하고, 사전 학습된 BERT 모델을 특정 목적에 맞춰 조정하는 파인튜닝(Fine-tuning) 과정을 다뤘습ㄴ디ㅏ. 현대 NLP 아키텍처의 근간을 이해하고 실무적인 모델 최적화 역량을 확보하는 데 중점을 두었으며 단순히 사전 학습된 모델을 사용하는 것을 넘어, BERT의 양방향 문맥 이해 원리와 MLM(Masked Language Model) 학습 방식을 연구하였습니다.

---

## 📂 프로젝트 구조 (Project Structure)
```text
📂 src/                                     
    └── 1_bert_finetuning_pipeline.py     # BERT 모델 정의 및 파인튜닝 파이프라인 구현
├── .gitignore                            # 체크포인트 및 캐시 제외 설정
├── LICENSE                               # MIT License (AD-Styles)
├── README.md                             # 트랜스포머 및 BERT 핵심 요약서
└── requirements.txt                      # Transformers, Torch 등 필수 라이브러리
```

---
