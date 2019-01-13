# Simulations for the SET board game

## Introduction

[SET](https://en.wikipedia.org/wiki/Set_(card_game)) ([神奇形色牌](https://zh.wikipedia.org/wiki/%E7%A5%9E%E5%A5%87%E5%BD%A2%E8%89%B2%E7%89%8C)) is a board game where there are 81 different cards.

The rules can be found here:

* [English](https://puzzles.setgame.com/set/rules_set.htm)
* [中文](https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20CHINESE.pdf)

## Least number of cards to guarantee a SET

Question: If *k* cards are dealt, is it possible that there's no SETs from these cards?

What's the smallest number of *k* to guarantee the existence of a SET?

`set_prob.py` is a simulation program to compute this. Run it like this:

```bash
python set_prob.py --start=12 --end=18 --num_trials=100000
```

This will compute the probabilities of *k* cards containing a SET, where
*k=12, 13, ..., 18*, and for each *k* a try 100,000 times.

Use a larger value for `--num_trials` for more accurate estimations, or use
`--num_trials=0` for an exact result (which can be very slow).

### Results

| *k*   | prob: 100K trials | prob: 1M trials | prob: 10M trials |
|-------|-------------------|-----------------|------------------|
| 12    | 0.968             | 0.967979        | 0.9677841        |
| 13    | 0.9903            | 0.990034        | 0.98999          |
| 14    | 0.99789           | 0.997674        | 0.9976782        |
| 15    | 0.99959           | 0.99966         | 0.999635         |
| 16    | 0.999999          | 0.999962        | 0.9999669        |
| 17    | 1.0               | 0.999999        | 0.9999989        |
| 18    | 1.0               | 1.0             | 1.0              |

* 100K trials takes about  26s.
* 1M trials takes about 2min.
* 10 trials takes about 40min.

## References

* [SET by BRIAN CONREY AND BRIANNA DONALDSON](https://www.mathteacherscircle.org/assets/session-materials/BConreyBDonaldsonSET.pdf)
* [The Odds of Finding a SET in The Card Game SET](http://norvig.com/SET.html)
* [SETs and Anti-SETs: The Math Behind the Game of SET](http://www-personal.umich.edu/~charchan/SET.pdf)