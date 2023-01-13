import torch
from transformers import (AutoConfig, AutoModelForSequenceClassification, AutoTokenizer, GPT2LMHeadModel, GPT2Tokenizer)


# класс
class zodiac_model:
    def __init__(self, model_name):
        self.config = AutoConfig.from_pretrained(model_name)
        self.DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name, config=self.config).to(self.DEVICE)

    def generate_zodiac(self, zodiac_name: str) -> str:
        text = "[START]" + zodiac_name + ':'
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to(self.DEVICE)
        self.model.eval()
        with torch.no_grad():
            out = self.model.generate(input_ids,
                                      do_sample=True,
                                      temperature=1.5,
                                      top_p=0.9,
                                      num_beams=2,
                                      max_length=300,
                                      pad_token_id=self.tokenizer.eos_token_id,
                                      )
        generated_text = list(map(self.tokenizer.decode, out))[0]
        return zodiac_name + ' : ' + generated_text[len(text):generated_text.find('[END]')]


def main():
    model = zodiac_model('./trainedGPT')
    print('Введи название:')
    print(model.generate_zodiac(input()))


if __name__ == '__main__':
    main()
