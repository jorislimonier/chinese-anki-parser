import pandas as pd
from deep_translator import GoogleTranslator  # type: ignore
from pypinyin import pinyin  # type: ignore


class ChineseParser:
  def __init__(self, vocab: list[list[str]]) -> None:
    self.vocab = vocab
    self._set_translations()
    self._set_pinyin()

  def _set_translations(self) -> None:
    trans = GoogleTranslator(source="zh-CN", target="en")
    self.translation = trans.translate_batch(self.vocab)
    self.translation = [t.capitalize() for t in self.translation]

  def _set_pinyin(self) -> None:
    vocab_pinyin = []

    # Iterate over propositions
    for prop in self.vocab:

      # Get pinyin
      pin = pinyin(prop)

      prop_pinyin = []

      # Iterate over list of possible pinyins
      for possible_pinyins in pin:

        # Warn if there are actually several possible pinyins
        # Most of the time (almost always), there is just one possible pinyin
        if len(possible_pinyins) != 1:
          print(
            f"Char {possible_pinyins} has several possibilities."
            + "Taking the first one."
          )

        prop_pinyin.append(possible_pinyins[0].strip())

      vocab_pinyin.append(" ".join(prop_pinyin))

      self.pinyin = vocab_pinyin

  def make_df(self) -> pd.DataFrame:
    results = pd.DataFrame(
      data={
        "chinese": self.vocab,
        "pinyin": self.pinyin,
        "translation": self.translation,
        "sound": None,
      }
    )
    ordered_col_names = ["chinese", "pinyin", "translation", "sound"]
    results = results[ordered_col_names]
    return results
