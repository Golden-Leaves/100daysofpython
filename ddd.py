import genanki
import random

model_id = random.randint(1 << 30, 1 << 31)

model = genanki.Model(
  model_id,
  'Basic Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

deck = genanki.Deck(
  2059400110,
  'Demo Deck: Random Precalc Flashcards')

cards = [
    ("What’s the domain of √(x - 5)?", "x ≥ 5"),
    ("(f ∘ g)(2) given f(x) = x + 1, g(x) = x²", "f(g(2)) = f(4) = 5"),
    ("What is a function?", "A relation where each input has exactly one output."),
    ("Is y² = x a function?", "No, it fails the vertical line test."),
    ("What’s the inverse of f(x) = 3x + 6?", "f⁻¹(x) = (x - 6) / 3")
]

for q, a in cards:
    note = genanki.Note(model=model, fields=[q, a])
    deck.add_note(note)

genanki.Package(deck).write_to_file('precalc_flashcards.apkg')
