# Diamond Kata

## My Approach

I worked out the formular on paper before writing any code. See `/notes`for my working.

- Leading spaces start at `diff` (distance from A to any given letter) and decease by 1 each row
- Inner spaces start at 1 for row B and increase by 2 each row.
- The diamond is split into two loops: the first prints up to the letter before the given letter. The second starts at the given leter, and mirrors back to A.
- A helper function `build_row` handles the single-letter case (A) separately from the two-letter rows

## Edge Cases Handled

- Non-alphabetic input returns early
- Input is uppercased to handle lowercase letters

## Diamond Kata Problem Description

Given a letter, print a diamond starting with ‘A’ with the supplied letter at the widest point.

For example: print-diamond ‘C’ prints
```
  A
 B B
C   C
 B B
  A
```