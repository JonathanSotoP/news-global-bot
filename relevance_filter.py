KEYWORDS = [

"war",
"ukraine",
"russia",
"china",
"taiwan",
"israel",
"iran",
"sanctions",
"oil",
"gas",
"inflation",
"interest rate",
"economy",
"recession",
"military",
"conflict",
"trade",
"nato"

]


def is_relevant(news):

    text = (news["title"] + " " + news["summary"]).lower()

    for word in KEYWORDS:
        if word in text:
            return True

    return False