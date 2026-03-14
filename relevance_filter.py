KEYWORDS = [

"war",
"conflict",
"sanctions",
"china",
"russia",
"oil",
"inflation",
"interest rate",
"global economy",
"recession",
"military",
"trade war"

]


def is_relevant(news):

    text = (news["title"] + " " + news["summary"]).lower()

    for word in KEYWORDS:
        if word in text:
            return True

    return False