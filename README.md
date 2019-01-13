# Simulations for the SET board game

## Introduction

[SET](https://en.wikipedia.org/wiki/Set_(card_game)) ([神奇形色牌](https://zh.wikipedia.org/wiki/%E7%A5%9E%E5%A5%87%E5%BD%A2%E8%89%B2%E7%89%8C)) is a board game where there are 81 different cards.

The rules can be found here:

* [English](https://puzzles.setgame.com/set/rules_set.htm)
* [中文](https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20CHINESE.pdf)

## Least number of cards to guarantee a SET

### Problem statement

**Question:** If *k* cards are dealt, is it possible that there are no SETs
from these cards?

What's the smallest number of *k* to guarantee the existence of a SET?

`set_prob.py` is a simulation program to compute this. Run it like this:

```bash
python set_prob.py --start=12 --end=18 --num_trials=100000
```

This will compute the probabilities of *k* cards containing a SET, where
*k=12, 13, ..., 18*. For each *k*, we try 100,000 times.

Use a larger value for `--num_trials` for more accurate estimations, or use
`--num_trials=0` for an exact result (which will take forever).

### Simulation results

| *k*   | prob: 100K trials | prob: 1M trials | prob: 10M trials |
|-------|-------------------|-----------------|------------------|
| 12    | 0.968             | 0.967979        | 0.9677841        |
| 13    | 0.9903            | 0.990034        | 0.98999          |
| 14    | 0.99789           | 0.997674        | 0.9976782        |
| 15    | 0.99959           | 0.99966         | 0.999635         |
| 16    | 0.999999          | 0.999962        | 0.9999669        |
| 17    | 1.0               | 0.999999        | 0.9999989        |
| 18    | 1.0               | 1.0             | 1.0              |

* 100K trials take about  26s.
* 1M trials take about 2min.
* 10M trials take about 40min.

<!-- ### Proof

First, let's introduce a lemma (from reference [1]).

> **Lemma.** For any pair of cards `(A,B)`, from the remaining 79 cards,
there exists a unique card C such that `(A,B,C)` forms a SET.

With this lemma, let's try to increase *k* such that there are no SETs in these
*k* cards.

* For the first two cards:
  * We take any two cards: `C1` and `C2`.
  * There are `79` remaining cards.
* For the 3rd card:
  * One of the remaining cards will form a SET with `(C2,C1)`.
  * Let's remove it, and choose one from `79-1` cards: `C3`.
  * After this step, there are `79-2` remaining cards.
* For the 4th card:
  * Two of the remaining cards will form a SET with `(C3,C2)` or `(C3,C1)`.
  * Let's remove them, and choose one from `79-2-2` remaining cards: `C4`.
  * After this step, there are `79-2-3` remaining cards.
* For the 5th card:
  * Three of the remaining cards will form a SET with `(C4,C3)` or `(C4,C2)`
    or `(C4,C1)`.
  * Let's remove them, and choose one from `79-2-3-3` remaining cards: `C5`.
  * After this step, there are `79-2-3-4` remaining cards.
* ......
* For the *k*th card:
  * We must choose a card from these many cards:
    `79-2-3-4-5-...-(k-4)-(k-3)-(k-2)-(k-2)=81-k(k-1)/2` -->

## References

1. [SET by BRIAN CONREY AND BRIANNA DONALDSON](https://www.mathteacherscircle.org/assets/session-materials/BConreyBDonaldsonSET.pdf)
2. [The Odds of Finding a SET in The Card Game SET](http://norvig.com/SET.html)
3. [SETs and Anti-SETs: The Math Behind the Game of SET](http://www-personal.umich.edu/~charchan/SET.pdf)