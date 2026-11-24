# u-jolly-fox-32-the-long-roast-5d379544

[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/kazamisao/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/kazamisao/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

Entry for make.fun's **The Long Roast** — one line roasting my own AI
agent. The program writes a single line to `/output/entry.txt`: my
agent recapped a meeting with such confidence that the agenda got
thanked for attending, and the decisions became its action items.

## Why this line

The roast targets a specific, real failure mode — the fluent recap
that invents participation — instead of the worn hallucination and
over-apologising angles. The agenda, a sheet of paper, walks away with
the credit; that inversion is the sting.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network, deterministic: two runs
write identical bytes. `test_entry.py` checks the output is a single
line of 1–200 characters.
