from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "facebook/nllb-200-distilled-600M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def translate_nllb(text: str, src_lang_code: str, tgt_lang_code: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", src_lang=src_lang_code)
    generated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[tgt_lang_code],
        max_length=512,
        num_beams=5
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
