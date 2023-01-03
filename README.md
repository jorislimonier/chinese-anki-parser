# Parser for Anki Chinese cards

In this repo, I take a text file with chinese characters and convert it to a CSV that can be passed to Anki.

The following steps are performed:

- Translate Chinese characters to English
- Convert Chinese characters to Pinyin (latin alphabet writing of the characters)
- Group the following columns to a dataframe that is passed to Anki:
  - Character
  - Pinyin
  - Translation
  - Sound (empty, but required because it is a field in the target Anki deck)
