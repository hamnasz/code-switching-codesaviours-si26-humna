import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

MODEL_REPO = "hamnaheh/code-switching-langid-si26-humna"  # <-- must match the repo_id you pushed to

st.set_page_config(page_title="Roman Urdu Code-Switching Language ID", page_icon="\U0001F524")

@st.cache_resource
def load_model():
    tok = AutoTokenizer.from_pretrained(MODEL_REPO)
    mdl = AutoModelForTokenClassification.from_pretrained(MODEL_REPO)
    mdl.eval()
    return tok, mdl

tokenizer, model = load_model()

COLORS = {"URD": "#2ecc71", "ENG": "#3498db", "MIX": "#e67e22"}

def predict(sentence):
    words = sentence.strip().split()
    if not words:
        return []
    encoded = tokenizer(words, is_split_into_words=True, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**encoded).logits
    preds = torch.argmax(logits, dim=2)[0].tolist()
    word_ids = encoded.word_ids(batch_index=0)

    results, seen = [], set()
    for idx, wid in enumerate(word_ids):
        if wid is None or wid in seen:
            continue
        seen.add(wid)
        results.append((words[wid], model.config.id2label[preds[idx]]))
    return results

st.title("\U0001F524 Roman Urdu Code-Switching Language ID")
st.caption("Code Saviours SI-26 \u00b7 Project 2 \u00b7 XLM-RoBERTa fine-tuned for token classification")
st.write("Type a Roman Urdu / English mixed sentence \u2014 each word gets tagged URD, ENG, or MIX.")

text = st.text_input("Sentence", "Aaj ka meeting bohot important tha yaar")

if text:
    tagged = predict(text)
    html = " ".join(
        f'<span style="background-color:{COLORS.get(l, "#bbb")};'
        f'padding:2px 6px;border-radius:4px;margin:2px;display:inline-block;">'
        f'{w} <sub>{l}</sub></span>'
        for w, l in tagged
    )
    st.markdown(html, unsafe_allow_html=True)

    st.divider()
    st.subheader("Word-by-word breakdown")
    st.table({"word": [w for w, _ in tagged], "label": [l for _, l in tagged]})
