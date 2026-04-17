import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

class BERTClassifier(nn.Module):
    """BERT 기반의 텍스트 분류기 아키텍처"""
    def __init__(self, bert_model_name: str, num_classes: int):
        super(BERTClassifier, self).__init__()
        # 사전 학습된 BERT 모델의 인코더 활용
        self.bert = BertModel.from_pretrained(bert_model_name)
        self.dropout = nn.Dropout(0.1)
        self.fc = nn.Linear(self.bert.config.hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        # [CLS] 토큰의 출력을 사용하여 문장 전체의 맥락 파악
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        x = self.dropout(pooled_output)
        return self.fc(x)

class BERTFineTuner:
    """BERT 파인튜닝 프로세스 제어 클래스"""
    def __init__(self, model_name: str = 'bert-base-uncased', num_classes: int = 2):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BERTClassifier(model_name, num_classes)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def preprocess(self, text: str):
        """텍스트 토큰화 및 어텐션 마스크 생성"""
        return self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_attention_mask=True,
            return_tensors='pt'
        )

    def predict(self, text: str):
        self.model.eval()
        inputs = self.preprocess(text)
        with torch.no_grad():
            outputs = self.model(
                input_ids=inputs['input_ids'].to(self.device),
                attention_mask=inputs['attention_mask'].to(self.device)
            )
            return torch.argmax(outputs, dim=1).item()

if __name__ == "__main__":
    tuner = BERTFineTuner()
    sample = "This deep learning project is a great start for my career."
    print(f"--- BERT Prediction ---")
    print(f"Input: {sample}")
    print(f"Result Class: {tuner.predict(sample)}")
