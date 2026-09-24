# Failure List

Anything marked `Hint` or `Failed` in a week log goes here.
Redo it cold. When it comes out unaided, move it to Closed with both dates.

## Open

- [ ] 5 Sep — **Majority Element (Boyer-Moore)** — failed the cold redo on 6 Sep, second time in two days. Reverted to checking the count at the *bottom* with `count < 1` and a `majority_element = 0` seed.
  Must get, unprompted: `count == 0` checked at the **top** · `if / elif / else`, not two `if`s · adopt with `count = 1` · no seed needed.
  It passes LeetCode either way because a true majority survives sloppy bookkeeping. That's exactly why the cold rep is the only real test. If you can't state the cancellation argument while writing it, it isn't learned.

- [ ] 23 Sep — **Product of Array Except Self (O(1) space version)** — needed the left-times-right framing handed over on 23 Sep. Cold redo 24 Sep: O(n) space version came clean, O(1) version failed twice.
  First attempt had no accumulator, so each slot only got one element from the right. Second attempt added `run` but read `output[j]` while writing `output[j-1]`, and the range skipped index n-1.
  Must get, unprompted: the framing sentence first, "output[i] = everything left of i × everything right of i" · left pass writes into `output` · right pass uses ONE variable, not an array · walk EVERY index, `reversed(range(len(nums)))` · read and write the SAME slot · multiply into `output[i]` FIRST, then fold `nums[i]` into the variable.

## Closed

- [x] 28 Aug — Merge Sorted Array — hint on drain loop — solved cold 29 Aug
- [x] 28 Aug — Best Time to Buy and Sell Stock — brute force only — solved one-pass 29 Aug
- [x] 4 Sep — Contains Duplicate II — cold redo crashed on `len(check) != 0` instead of `value in check` — clean first attempt 6 Sep
- [x] 4 Sep — Valid Anagram — used `< 0` without being able to justify it — explained the length-check dependency correctly 6 Sep
- [x] 5 Sep — Group Anagrams — counting key needed heavy prompting — structurally right cold 6 Sep, including `[0] * 26` inside the loop
- [x] 18 Sep — Missing Number (XOR) — over 25 min, needed the `[0,1,3]` trace — solved cold 24 Sep with a two-pass XOR, unaided
- [x] 21 Sep — Subarray Sum Equals K — needed the full code before the idea landed — solved cold 24 Sep

## Recurring habits (not problems)

These cost time in multiple sessions. None of them are conceptual.

- **Repeating a key expression instead of assigning it to `key`** — flagged six times. On 6 Sep you finally made the variable and then didn't use it on the next line. `tuple(...)` is O(k) per call, so by Group Anagrams this stopped being cosmetic
- **`.get(k, default)` inside `if k not in d`** — the `.get()` can only return the default. Unreachable code, and unreachable code is where bugs hide
- **Naming**: `i` for a non-index (4x) · `is_valid` / `valid` for a dict of counts (3x) · `alphabet` for a list of counts · `immutable_conversion` describing the mechanism instead of the meaning
- **Sending code before running it** — the `complement` line outside the loop, the `immuatble_conversion` typo, `employees` vs `employee`, `return subarrays3`. Run it first
- **Dead edge-case branches** — 18 Sep, `range_sum` had `if len(prefix) == 0` and `== 1` guards that could never fire. Edge cases are things to **test**, not `if`s to add. Ask "can this condition actually happen?" before writing the branch
- **Fixed details regressing on the cold redo** — Plus One on 24 Sep lost the early return and the `if carry:` after the loop, both of which were fixed on Friday. Then dropped the final `return digits`. The logic survived, the details didn't. When you close a problem, write down the two or three details you had to be told, and check for them on the redo
- **Loop bounds off by one** — `range(1, len(nums), -1)`, stop at 1 instead of -1, `range(len(nums) - 1)` skipping the last index. Before running any loop, say out loud which indices it visits

## SQL habits

- **A CTE holding one value used bare in WHERE** — three times on 19 Sep. A CTE is a table, not a value. It enters through FROM (CROSS JOIN) or a subquery expression, never `WHERE x = cte_name`
- **Aggregating over a column that's also in the GROUP BY** — `b.bonus` on 18 Sep, `risk_category` on 19 Sep. Nothing collapses. The column you aggregate never goes in GROUP BY
- **Aliases used outside the query they belong to** — `b.worker_ref_id` in the outer query (18 Sep), `l.user_id` in the final SELECT (23 Sep). An alias defined inside a CTE doesn't exist outside it
- **Aggregate in WHERE** — `timestamp = MAX(timestamp)` on 23 Sep. WHERE runs before GROUP BY. Filter with WHERE, aggregate in SELECT with GROUP BY