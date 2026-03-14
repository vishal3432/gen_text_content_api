from nltk.translate.bleu_score import sentence_bleu

reference = ["this is a product description".split()]
candidate = "this is a generated product description".split()

score = sentence_bleu(references,candidate)

print("BLEU Score:", score)