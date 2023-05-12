from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
from transformers import PegasusForConditionalGeneration, AutoTokenizer


model_name = "google/pegasus-xsum"
torch_device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(model_name)
# tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


# model = AutoModelForSequenceClassification.from_pretrained(output_dir).to(device)
src_text = [
    """ The novelist J.K. Rowling once said, “there’s always room for a story that can transport people to another place.” But what if that place we’re transported to is here, inside the rich web of life of our Mother Earth. The objective of this class is to expand our imagination in relationship to nature; to awaken a soulful journey within ourselves and the earth; to discover how to create and tell stories that ignite our heart’s connection to life; and to learn how to teach our younger generations to perceive nature through a creative and engaging lens. Whether you’re a soulful journeyer, parent, grandparent, teacher, or you want to create children’s stories centered on nature, this class is designed to be a dynamic journey that serves our earth, our children, and all of us. As a children’s author and storyteller, I’ll also share my own creative process and introduce the Japanese Kamishibai Theatre boxes used to tell stories in Japanese parks in the 1930s."""
]

batch = tokenizer.prepare_seq2seq_batch(
    src_text, truncation=True, padding="longest", return_tensors="pt"
).to(torch_device)
# batch = tokenizer.prepare_seq2seq_batch(
#     src_text, truncation=True, padding="longest", return_tensors="pt"
# )
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
print(tgt_text)
