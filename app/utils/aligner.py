from sentence_transformers import SentenceTransformer, util
from app.utils.segmenter import split_segments
from app.utils.translation import translate_nllb

labse_model = SentenceTransformer("sentence-transformers/LaBSE")

# Example language codes: "eng_Latn", "fra_Latn", "zho_Hans"
def align_segments(src_text, tgt_text, src_lang_code, tgt_lang_code, threshold=0.75):
    src_segs = split_segments(src_text)
    tgt_segs = split_segments(tgt_text)

    src_embeddings = labse_model.encode(src_segs, convert_to_tensor=True)
    tgt_embeddings = labse_model.encode(tgt_segs, convert_to_tensor=True)

    results = []

    for idx, src_emb in enumerate(src_embeddings):
        src_sentence = src_segs[idx]
        sims = util.cos_sim(src_emb, tgt_embeddings)[0]
        best_idx = sims.argmax().item()
        best_score = sims[best_idx].item()
        tgt_sentence = tgt_segs[best_idx]

        if best_score < threshold:
            corrected = translate_nllb(src_sentence, src_lang_code, tgt_lang_code)
        else:
            corrected = tgt_sentence

        results.append({
            "source": src_sentence,
            "target": tgt_sentence,
            "similarity": best_score,
            "corrected": corrected,
            "was_corrected": corrected != tgt_sentence
        })

    return results
