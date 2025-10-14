Simple TicTacToe Environment for RL


Number of possible states:
with invalid states = 3^9
total winning ways = total number of winning positions * number of ways to win * 2 players = 8*3*2 = 48

total illegal states = cannot have 5 or more of X (or O) in a row = (total number of states with 5 consecutive Xs) * 2 = 9C5 * 2 = 252 * 2 = 504

# Tic-Tac-Toe Winning States Calculation

## Problem Statement
Calculate the total number of winning board configurations for X in tic-tac-toe.

## Key Constraints
1. X moves first (player 0), O moves second (player 1)
2. Game ends immediately when a player wins
3. A winning configuration has exactly one winner (no simultaneous wins)
4. X can win with 3, 4, or 5 pieces on the board
5. There are 8 possible winning lines: 3 rows + 3 columns + 2 diagonals

## Calculation Method

### Case 1: X=3, O=2
**Setup:**
- X has exactly 3 pieces forming a winning line
- O has 2 pieces (game ended after 5 total moves)

**Calculation:**
- 8 winning lines for X
- C(6,2) = 15 ways to place O's 2 pieces in remaining cells
- O cannot form a winning line with only 2 pieces

**Result:** 8 × 15 = **120 configurations**

---

### Case 2: X=4, O=3
**Setup:**
- X has 3 pieces forming a winning line + 1 extra piece
- O has 3 pieces (game ended after 7 total moves)

**Diagonal Wins (2 lines):**
- C(6,1) × C(5,3) = 6 × 10 = 60 ways to place extra X and 3 O's
- No possible O winning lines from remaining cells
- Subtotal: 60 × 2 = **120 configurations**

**Row Wins (3 lines):**
- C(6,1) × C(5,3) = 60 total placements
- Subtract 2: O can complete the other two rows
- Valid configurations per row: 60 - 2 = 58
- Subtotal: 58 × 3 = **174 configurations**

**Column Wins (3 lines):**
- By symmetry with rows: 58 × 3 = **174 configurations**

**Result:** 120 + 174 + 174 = **468 configurations**

---

### Case 3: X=5, O=4
**Setup:**
- X has 3 pieces forming a winning line + 2 extra pieces
- O has 4 pieces (game ended after 9 total moves)

**Diagonal Wins (2 lines):**
- C(6,4) = 15 ways to place 4 O's
- C(2,2) = 1 way to place 2 extra X's (forced)
- No possible O winning lines
- Subtotal: 15 × 1 × 2 = **30 configurations**

**Row Wins (3 lines):**
- C(6,4) = 15 total ways to place O's
- Subtract 2: O can complete the other two rows
- Valid configurations: (15 - 2) × 1 = 13 per row
- Subtotal: 13 × 3 = **39 configurations**

**Column Wins (3 lines):**
- By symmetry with rows: 13 × 3 = **39 configurations**

**Result:** 30 + 39 + 39 = **108 configurations**

---

## Final Result

**Total X Winning States:**
```
120 + 468 + 108 = 696
```

## Notes
- This calculation assumes perfect play detection (game ends immediately upon win)
- O winning states can be calculated similarly with adjusted piece counts
- These counts are essential for Q-learning state space analysis
