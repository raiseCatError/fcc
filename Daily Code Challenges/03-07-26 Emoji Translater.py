# Emoji Translator
# Given a string of emojis, return the phrase using the following table:
#
# Emoji	Word
# 👶	"baby"
# 🐱	"cat"
# 🐕	"dog"
# 🐟	"fish"
# 🥵	"hot"
# 🧊	"ice"
# 🪨	"rock"
# 🦈	"shark"
# 🍲	"soup"
# ⭐	   "star"
# Return the words separated by spaces.
#



def get_emoji_phrase(emojis):

    emoji_words = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star"
    }

    words = []

    for emoji in emojis:
        if emoji in emoji_words:
            words.append(emoji_words[emoji])

    return " ".join(words)

get_emoji_phrase("🪨⭐")
get_emoji_phrase("🥵🐕")
get_emoji_phrase("👶🦈")
get_emoji_phrase("⭐🐟")
get_emoji_phrase("🧊🧊👶")
get_emoji_phrase("🐱🐟🍲")