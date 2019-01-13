# Simulations for the SET board game

## Introduction

SET is a board game where there are 81 different cards.

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

#### 100K trials

| k     | probability        |
|-------|--------------------|
| 12    | 0.968              |
| 13    | 0.9903             |
| 14    | 0.99789            |
| 15    | 0.99959            |
| 16    | 0.999999           |
| 17    | 1.0                |
| 18    | 1.0                |

#### 1M trials

| k     | probability        |
|-------|--------------------|
| 12    | 0.967979           |
| 13    | 0.990034           |
| 14    | 0.997674           |
| 15    | 0.99966            |
| 16    | 0.999962           |
| 17    | 0.999999           |
| 18    | 1.0                |

## References

* [SET by BRIAN CONREY AND BRIANNA DONALDSON](https://www.mathteacherscircle.org/assets/session-materials/BConreyBDonaldsonSET.pdf)
* [The Odds of Finding a SET in The Card Game SET](http://norvig.com/SET.html)
* [SETs and Anti-SETs: The Math Behind the Game of SET](http://www-personal.umich.edu/~charchan/SET.pdf)