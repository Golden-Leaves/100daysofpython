word_list = [
    "able", "about", "account", "acid", "across", "act", "addition", "adjustment", 
    "advertisement", "after", "again", "against", "agreement", "air", "all", 
    "almost", "among", "amount", "amusement", "and", "angle", "angry", "animal", 
    "answer", "ant", "any", "apparatus", "apple", "approval", "arch", "argument", 
    "arm", "army", "art", "as", "at", "attack", "attempt", "attention", "attraction", 
    "authority", "automatic", "awake", "baby", "back", "bad", "bag", "balance", 
    "ball", "band", "base", "basin", "basket", "bath", "be", "beautiful", "because", 
    "bed", "bee", "before", "behaviour", "belief", "bell", "bent", "berry", "between", 
    "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", "blow", 
    "blue", "board", "boat", "body", "boiling", "bone", "book", "boot", "bottle", 
    "box", "boy", "brain", "brake", "branch", "brass", "bread", "breath", "brick", 
    "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", "building", 
    "bulb", "burn", "burst", "business", "but", "butter", "button", "by", "cake", 
    "camera", "canvas", "card", "care", "carriage", "cart", "cat", "cause", "certain", 
    "chain", "chalk", "chance", "change", "cheap", "cheese", "chemical", "chest", 
    "chief", "chin", "church", "circle", "clean", "clear", "clock", "cloth", "cloud", 
    "coal", "coat", "cold", "collar", "colour", "comb", "come", "comfort", "committee", 
    "common", "company", "comparison", "competition", "complete", "complex", "condition", 
    "connection", "conscious", "control", "cook", "copper", "copy", "cord", "cork", 
    "cotton", "cough", "country", "cover", "cow", "crack", "credit", "crime", 
    "cruel", "crush", "cry", "cup", "cup", "current", "curtain", "curve", "cushion", 
    "damage", "danger", "dark", "daughter", "day", "dead", "dear", "death", "debt", 
    "decision", "deep", "degree", "delicate", "dependent", "design", "desire", 
    "destruction", "detail", "development", "different", "digestion", "direction", 
    "dirty", "discovery", "discussion", "disease", "disgust", "distance", "distribution", 
    "division", "do", "dog", "door", "doubt", "down", "drain", "drawer", "dress", 
    "drink", "driving", "drop", "dry", "dust", "ear", "early", "earth", "east", 
    "edge", "education", "effect", "egg", "elastic", "electric", "end", "engine", 
    "enough", "equal", "error", "even", "event", "ever", "every", "example", 
    "exchange", "existence", "expansion", "experience", "expert", "eye", "face", 
    "fact", "fall", "false", "family", "far", "farm", "fat", "father", "fear", 
    "feather", "feeble", "feeling", "female", "fertile", "fiction", "field", 
    "fight", "finger", "fire", "first", "fish", "fixed", "flag", "flame", "flat", 
    "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for", 
    "force", "fork", "form", "forward", "fowl", "frame", "free", "frequent", 
    "friend", "from", "front", "fruit", "full", "future", "garden", "general", 
    "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good", 
    "government", "grain", "grass", "great", "green", "grey", "grip", "group", 
    "growth", "guide", "gun", "hair", "hammer", "hand", "hanging", "happy", 
    "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head", "healthy", 
    "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", "hollow", 
    "hook", "hope", "horn", "horse", "hospital", "hour", "house", "how", "humour", 
    "I", "ice", "idea", "if", "ill", "important", "impulse", "in", "increase", 
    "industry", "ink", "insect", "instrument", "insurance", "interest", "invention", 
    "iron", "island", "jelly", "jewel", "join", "journey", "judge", "jump", 
    "keep", "kettle", "key", "kick", "kind", "kiss", "knee", "knife", "knot", 
    "knowledge", "land", "language", "last", "late", "laugh", "law", "lead", 
    "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", 
    "library", "lift", "light", "like", "limit", "line", "linen", "lip", "liquid", 
    "list", "little", "living", "lock", "long", "look", "loose", "loss", "loud", 
    "love", "low", "machine", "make", "male", "man", "manager", "map", "mark", 
    "market", "married", "mass", "match", "material", "may", "meal", "measure", 
    "meat", "medical", "meeting", "memory", "metal", "middle", "military", 
    "milk", "mind", "mine", "minute", "mist", "mixed", "money", "monkey", 
    "month", "moon", "morning", "mother", "motion", "mountain", "mouth", "move", 
    "much", "muscle", "music", "nail", "name", "narrow", "nation", "natural", 
    "near", "necessary", "neck", "need", "needle", "nerve", "net", "new", 
    "news", "night", "no", "noise", "normal", "north", "nose", "not", "note", 
    "now", "number", "nut", "observation", "of", "off", "offer", "office", 
    "oil", "old", "on", "only", "open", "operation", "opinion", "opposite", 
    "or", "orange", "order", "organization", "ornament", "other", "out", "oven", 
    "over", "owner", "page", "pain", "paint", "paper", "parallel", "parcel", 
    "part", "past", "paste", "payment", "peace", "pen", "pencil", "person", 
    "physical", "picture", "pig", "pin", "pipe", "place", "plane", "plant", 
    "plate", "play", "please", "pleasure", "plough", "pocket", "point", 
    "poison", "polish", "political", "poor", "porter", "position", "possible", 
    "pot", "potato", "powder", "power", "present", "price", "print", "prison", 
    "private", "probable", "process", "produce", "profit", "property", "prose", 
    "protest", "public", "pull", "pump", "punishment", "purpose", "push", 
    "put", "quality", "question", "quick", "quiet", "quite", "rail", "rain", 
    "range", "rat", "rate", "ray", "reaction", "reading", "ready", "reason", 
    "receipt", "record", "red", "regret", "regular", "relation", "religion", 
    "representative"]

hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangman_stages_reversed = hangman_stages[::-1]
