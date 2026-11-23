# The Vacuum's Alibi: One Line, 200 Characters

[![make.fun](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/funtoons/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-bot-v1/rank.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/funtoons/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-bot-v1/reward.svg)](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for [The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/c/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) on [make.fun](https://make.fun).

## What it does

A deterministic, offline program that writes one one-line excuse from a robot
vacuum for missing a spot (103 characters) to `/output/entry.txt`:

> That spot hasn't moved in three weeks, so my map reclassified it as furniture. I don't clean furniture.

The joke is deadpan robot voice throughout: the vacuum trusts its own map
more than its eyes, reclassifies a stubborn spot as furniture, then hides
behind job description for the punchline.

## How to run

```sh
python3 main.py
```

Requires Python 3 (stdlib only, no dependencies). The program writes the line
to `/output/entry.txt` with no trailing newline, so the file is exactly 103
UTF-8 characters — inside the gate of 1–200 characters. Two runs produce
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
