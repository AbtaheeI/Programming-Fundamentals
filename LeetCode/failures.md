# Failure List

Anything marked `Hint` or `Failed` in a week log goes here.
Redo it cold. When it comes out unaided, move it to Closed with both dates.

## Open

- [ ] 4 Sep — Contains Duplicate II — cold redo crashed. Wrote `len(check) != 0` (is the dict non-empty) instead of `value in check` (is this key present). KeyError on the first unseen value. Structure and the latest-index logic were right.
- [ ] 4 Sep — Valid Anagram — cold redo used `< 0` in the final loop. Correct, but only because the length check at the top forces the counts to sum to zero. Write `!= 0` unless you can explain the dependency out loud.
- [ ] 5 Sep — Group Anagrams — sorted-word key was own work; the 26-slot counting key needed heavy prompting. Redo the counting version cold, and state both complexities without looking.
- [ ] 5 Sep — Majority Element — Boyer-Moore took most of a session. Redo cold. Must get: `count == 0` checked at the **top**, `if/elif/else` not two ifs, adopt with `count = 1`.

## Closed

- [x] 28 Aug — Merge Sorted Array — hint on drain loop — solved cold 29 Aug
- [x] 28 Aug — Best Time to Buy and Sell Stock — brute force only — solved one-pass 29 Aug
