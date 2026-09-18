# Failure List

Anything marked `Hint` or `Failed` in a week log goes here.
Redo it cold. When it comes out unaided, move it to Closed with both dates.

## Open

- [ ] 5 Sep — **Majority Element (Boyer-Moore)** — failed the cold redo on 6 Sep, second time in two days. Reverted to checking the count at the *bottom* with `count < 1` and a `majority_element = 0` seed.
  Must get, unprompted: `count == 0` checked at the **top** · `if / elif / else`, not two `if`s · adopt with `count = 1` · no seed needed.
  It passes LeetCode either way because a true majority survives sloppy bookkeeping. That's exactly why the cold rep is the only real test. If you can't state the cancellation argument while writing it, it isn't learned.

- [ ] 18 Sep — **Missing Number (XOR version)** — over 25 minutes, needed the concrete `[0,1,3]` trace before the idea landed. Got there but couldn't see it from the hint alone.
  Must get, unprompted: the signal is **"O(1) space demanded + set is the obvious answer"** → accumulate into one variable → sum or XOR · XOR the indices AND the values into one pile, matching numbers cancel · the final `output ^= len(nums)` after the loop, because `enumerate` stops one short of the range.
  The set and maths versions came unaided. This is specifically about recognising XOR as the third option in the accumulate-into-one-variable bucket.

## Closed

- [x] 28 Aug — Merge Sorted Array — hint on drain loop — solved cold 29 Aug
- [x] 28 Aug — Best Time to Buy and Sell Stock — brute force only — solved one-pass 29 Aug
- [x] 4 Sep — Contains Duplicate II — cold redo crashed on `len(check) != 0` instead of `value in check` — clean first attempt 6 Sep
- [x] 4 Sep — Valid Anagram — used `< 0` without being able to justify it — explained the length-check dependency correctly 6 Sep
- [x] 5 Sep — Group Anagrams — counting key needed heavy prompting — structurally right cold 6 Sep, including `[0] * 26` inside the loop

## Recurring habits (not problems)

These cost time in four separate sessions this week. None of them are conceptual.

- **Repeating a key expression instead of assigning it to `key`** — flagged six times. On 6 Sep you finally made the variable and then didn't use it on the next line. `tuple(...)` is O(k) per call, so by Group Anagrams this stopped being cosmetic
- **`.get(k, default)` inside `if k not in d`** — the `.get()` can only return the default. Unreachable code, and unreachable code is where bugs hide
- **Naming**: `i` for a non-index (4x) · `is_valid` / `valid` for a dict of counts (3x) · `alphabet` for a list of counts · `immutable_conversion` describing the mechanism instead of the meaning
- **Sending code before running it** — the `complement` line outside the loop, the `immuatble_conversion` typo, `employees` vs `employee`. Run it first
- **Dead edge-case branches** — 18 Sep, `range_sum` had `if len(prefix) == 0` and `== 1` guards that could never fire given how `build_prefix` works. Edge cases are things to **test**, not `if`s to add. Ask "can this condition actually happen?" before writing the branch