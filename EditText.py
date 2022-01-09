import re

class EditText:
    def change_unicode_sumniki_to_text(text):
        # šumniki converted in chars
        text = text.replace("\\xc5\\xa1", "š")
        text = text.replace("\\xc4\\x8d", "č")
        text = text.replace("\\xc5\\xbe", "ž")
        return text


    def change_unicode_emoji_to_text(text):
        # unicode emojis converted to words
        text = text.replace("\\xf0\\x9f\\x98\\x87", "smile ")
        text = text.replace("\\xf0\\x9F\\x98\\x88", "evil happy ")
        text = text.replace("\\xf0\\x9f\\x98\\x8e", "cool ")
        text = text.replace("\\xf0\\x9f\\x98\\x90", "neutral ")
        text = text.replace("\\xf0\\x9f\\x98\\x91", "expressionless ")
        text = text.replace("\\xf0\\x9f\\x98\\x95", "confused ")
        text = text.replace("\\xf0\\x9f\\x98\\x97", "kissing ")
        text = text.replace("\\xf0\\x9f\\x98\\x99", "kissing ")
        text = text.replace("\\xf0\\x9f\\x98\\x9b", "funny ")
        text = text.replace("\\xf0\\x9f\\x98\\x9f", "worried ")
        text = text.replace("\\xf0\\x9f\\x98\\xa6", "frowning ")
        text = text.replace("\\xf0\\x9f\\x98\\xa7", "anguished ")
        text = text.replace("\\xf0\\x9f\\x98\\xac", "grimacing ")
        text = text.replace("\\xf0\\x9f\\x98\\xae", "shoked ")
        text = text.replace("\\xf0\\x9f\\x98\\xaf", "hushed ")
        text = text.replace("\\xf0\\x9f\\x98\\xb4", "sleeping ")
        text = text.replace("\\xf0\\x9f\\x98\\xb6", "silent ")
        text = text.replace("\\xf0\\x9f\\x98\\x81", "smile ")
        text = text.replace("\\xf0\\x9f\\x98\\x82", "hilarious ")
        text = text.replace("\\xf0\\x9f\\x98\\x83", "happy ")
        text = text.replace("\\xf0\\x9f\\x98\\x84", "happy ")
        text = text.replace("\\xf0\\x9f\\x98\\x85", "happy Sweat ")
        text = text.replace("\\xf0\\x9f\\x98\\x86", "grinning ")
        text = text.replace("\\xf0\\x9f\\x98\\x89", "wink happy ")
        text = text.replace("\\xf0\\x9f\\x98\\x8a", "smiling ")
        text = text.replace("\\xf0\\x9f\\x98\\x8b", "savouring  ")
        text = text.replace("\\xf0\\x9f\\x98\\x8c", "relieved ")
        text = text.replace("\\xf0\\x9f\\x98\\x8d", "love ")
        text = text.replace("\\xf0\\x9f\\x98\\x8f", "smirking ")
        text = text.replace("\\xf0\\x9f\\x98\\x92", "unamused ")
        text = text.replace("\\xf0\\x9f\\x98\\x93", "hard work ")
        text = text.replace("\\xf0\\x9f\\x98\\x94", "sad ")
        text = text.replace("\\xf0\\x9f\\x98\\x96", "confounded ")
        text = text.replace("\\xf0\\x9f\\x98\\x98", "kissing love ")
        text = text.replace("\\xf0\\x9f\\x98\\x9a", "kiss ")
        text = text.replace("\\xf0\\x9f\\x98\\x9c", "joking ")
        text = text.replace("\\xf0\\x9f\\x98\\x9d", "joking ")
        text = text.replace("\\xf0\\x9f\\x98\\x9r", "disappointed ")
        text = text.replace("\\xf0\\x9f\\x98\\xa0", "angry ")
        text = text.replace("\\xf0\\x9f\\x98\\xa1", "furious ")
        text = text.replace("\\xf0\\x9f\\x98\\xa2", "crying ")
        text = text.replace("\\xf0\\x9f\\x98\\xa3", "helpless ")
        text = text.replace("\\xf0\\x9f\\x98\\xa4", "frustrated ")
        text = text.replace("\\xf0\\x9f\\x98\\xa5", "disappointed ")
        text = text.replace("\\xf0\\x9f\\x98\\xa8", "fearful ")
        text = text.replace("\\xf0\\x9f\\x98\\xa9", "weary ")
        text = text.replace("\\xf0\\x9f\\x98\\xaa", "sleepy ")
        text = text.replace("\\xf0\\x9f\\x98\\xab", "tired ")
        text = text.replace("\\xf0\\x9f\\x98\\xad", "crying ")
        text = text.replace("\\xf0\\x9f\\x98\\xb0", "nervous ")
        text = text.replace("\\xf0\\x9f\\x98\\xb1", "screaming ")
        text = text.replace("\\xf0\\x9f\\x98\\xb2", "astonished ")
        text = text.replace("\\xf0\\x9f\\x98\\xb3", "flushed ")
        text = text.replace("\\xf0\\x9f\\x98\\xb5", "dizzy ")
        text = text.replace("\\xf0\\x9f\\x98\\xb7", "mask ")
        return text

    def remove_url(text):
        # remove url
        text = re.sub(r'http.?://[^\s]+[\s]?', '', text)
        return text

    def remove_mentions(text):
        # remove mentions
        text = re.sub(r'@\w+', '', text)
        return text

    def remove_numbers_and_other_signs(text):
        text = text.replace("b'", "")
        text = text.replace("RT ", "")
        text = re.sub('[\'?|.,():;>=<#$%&*+_}{1234567890]', '', text)
        text = text.replace("-", "")
        text = text.replace('\\n', " ")
        return text
