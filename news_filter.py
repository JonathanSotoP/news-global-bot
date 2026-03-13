KEYWORDS = [
"war","conflict","nato","russia","china","taiwan",
"inflation","interest rate","central bank",
"oil","gas","recession","sanctions","military"
]

def is_relevant(news):
    text = (news["title"] + " " + news["summary"]).lower()
    for k in KEYWORDS:
        if k in text:
            return True
    return False