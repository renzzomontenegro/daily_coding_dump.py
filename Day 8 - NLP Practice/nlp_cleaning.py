sampleText = [
    "The Enrollment-System @ University of Manila is *Very* slow!!!",
    "Tuition.Fee increased again in Ateneo (2024–2025).",
    "Walang Internet!!! sa Campus-Library ng Naga City.",
    "The Classroom [Room-301] in Building-A is TOO hot!!!",
    "Professor Santos gave an Exam without Announcement!!!",
    "Payment confirmation @ Registrar's Office takes too long...",
    "The School-App crashes whenever I log-in :(",
    "Walang Tubig!!! sa C.R. ng Building-B @ Main Campus.",
    "Homework deadlines @ Computer-Science Dept. are unrealistic!!!",
    "The WiFi in University of the Philippines - Diliman is weak...",
    "Late Announcements from Admin-Office cause confusion!!!",
    "The AirCon (Samsung™) in Room-204 is not working!!!",
    "Enrollment @ Central-System failed again—ERROR: 504!!!",
    "Ang Mahal!!! ng Miscellaneous-Fees sa Bicol University.",
    "The Library@Naga-Campus closes too early!!!"
]

def cleanText(text):
    cleaned_token = []
    sp_char = [",", ".", "'", "?", "!", "(", ")", "[", "]", "{", "}", "™", ":", ";", "|", "/", "`", "~", "*"]
    separators = ["@", "-", "—", "–"]

    for word in text.split():
        normalized = word.lower()
        for chara in sp_char:
            normalized = normalized.replace(chara, "")
        for sep in separators:
            normalized = normalized.replace(sep, " ")
        cleaned = normalized.split()
        for word in cleaned:
            cleaned_token.append(word)

    return cleaned_token

for statement in sampleText:
    print(cleanText(statement))