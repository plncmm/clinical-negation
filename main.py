import fastapi
import negex

app = fastapi.FastAPI(title="Clinical Negation Detector", description="API for detecting negation in clinical text", version="1.0")

rfile = open(r'negex_triggers_es.txt')
irules = negex.sortRules(rfile.readlines())

@app.get("/detector")
async def negation(s: str, p: str):  
    tagger = negex.negTagger(sentence = s, phrases = [p], rules = irules, negP=False)
    negated = True if tagger.getNegationFlag() == "negated" else False
    response = {
        "negated" : negated
    }
    return response