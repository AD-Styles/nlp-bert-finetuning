# 📝 Transformer-based NLP: From Self-Attention to BERT
### 어텐션(Attention) 메커니즘의 이해와 BERT 모델 구현

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Hugging%20Face-yellow?style=flat-square)

---

## 📌 프로젝트 개요 (Project Overview)
본 프로젝트는 트랜스포머(Transformer)의 핵심인 셀프 어텐션(Self-Attention) 구조를 파악하고, 사전 학습된 BERT 모델을 특정 목적에 맞춰 조정하는 파인튜닝(Fine-tuning) 과정을 다뤘습ㄴ디ㅏ. 현대 NLP 아키텍처의 근간을 이해하고 실무적인 모델 최적화 역량을 확보하는 데 중점을 두었으며 단순히 사전 학습된 모델을 사용하는 것을 넘어, BERT의 양방향 문맥 이해 원리와 MLM(Masked Language Model) 학습 방식을 연구하였습니다.

---

## 📂 프로젝트 구조 (Project Structure)
```text
📂 src/                                     
    └── 1_bert_finetuning_pipeline.py     # BERT 모델 정의 및 파인튜닝 파이프라인 구현
├── .gitignore                            # 프로젝트 관리 제외 설정
├── LICENSE                               # MIT License (AD-Styles)
├── README.md                             # 프로젝트 요약 및 가이드
└── requirements.txt                      # 필수 라이브러리 목록
```

---

## 🛠️ 기술 스택 (Tech Stack)
| 구분 | 상세 항목 |
| :--- | :--- |
| **Language** | Python |
| **Libraries** | Transformers (Hugging Face), Tokenizers |
| **Frameworks** | PyTorch |
| **Infrastructure** | CUDA (GPU Acceleration) |

---

## 🚀 주요 기능 및 워크플로우 (Key Features & Workflow)
| 단계 | 주요 기능 (Features) | 핵심 기술 (Key Tech) |
| :--- | :--- | :--- |
| **1. 문맥적 임베딩** | 단어의 위치와 관계를 고려한 벡터 생성 | Self-Attention, Positional Encoding |
| **2. 사전 학습 이해** | 모델이 언어를 학습하는 방식 분석 | Masked LM (MLM), Next Sentence Prediction |
| **3. 파인튜닝** | 특정 태스크를 위한 가중치 미세 조정 | Backpropagation, Learning Rate Scheduling |
| **4. 전이 학습** | 지식 전이를 통한 학습 효율 극대화 | Transfer Learning, [CLS] Token Pooling |

---

## 💡 회고록 (Retrospective)
&emsp;&emsp;이전 프로젝트였던 'NLP 전처리 및 시퀀스 모델링 기초' 포트폴리오에서 기초를 다지며 가졌던 가장 큰 궁금증은 '어떻게 기계가 단어 사이의 미묘한 문맥을 파악할까?'였습니다. 이번 프로젝트를 통해 트랜스포머의 어텐션 메커니즘이 그 해답임을 알게 되었습니다. 특히 특정 단어가 문장 내 다른 모든 단어와 상호작용하며 가중치를 계산하는 셀프 어텐션 과정은 기존 RNN의 한계를 뛰어넘는 놀라운 발상이었습니다.
<br>&emsp;&emsp;BERT 모델을 직접 파인튜닝해 보면서 가장 인상 깊었던 점은 전이 학습(Transfer Learning)의 강력함이었습니다. 대규모 코퍼스로 이미 언어를 배운 모델을 가져와 내 목적에 맞는 출력층만 살짝 얹어 학습시켰음에도 불구하고, 비약적인 성능 향상을 보이는 것을 확인했습니다. 물론 거대한 파라미터를 다루는 만큼 메모리 관리나 학습 속도 제어가 쉽지 않았지만, 이 과정에서 GPU 가속과 효율적인 배치 처리의 중요성도 배울 수 있었습니다.
<br>&emsp;&emsp;이제 '모델링'의 즐거움을 알게 된 만큼, 다음 과제는 이렇게 완성된 고성능 모델을 실제 서비스 환경에서 어떻게 빠르고 가볍게 서빙(Serving)할 수 있을지 고민하는 것입니다. 최적화와 배포라는 더 넓은 엔지니어링의 환경을 경험할 계획입니다.
