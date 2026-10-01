# Failure List

Anything marked `Hint` or `Failed` in a week log goes here.
Redo it cold. When it comes out unaided, move it to Closed with both dates.

## Open

- [ ] 23 Sep — **Product of Array Except Self (O(1) space version)** — needed the left-times-right framing handed over on 23 Sep. Cold redo 24 Sep: O(n) space version came clean, O(1) version failed twice.
  First attempt had no accumulator, so each slot only got one element from the right. Second attempt added `run` but read `output[j]` while writing `output[j-1]`, and the range skipped index n-1.
  Must get, unprompted: the framing sentence first, "output[i] = everything left of i × everything right of i" · left pass writes into `output` · right pass uses ONE variable, not an array · walk EVERY index, `reversed(range(len(nums)))` · read and write the SAME slot · multiply into `output[i]` FIRST, then fold `nums[i]` into the variable.

- [ ] 27 Sep — **Rising Temperature (LC 197)** — joined on id = id, then had the date direction backwards (thought w2 was tomorrow) and returned yesterday's id.
  Must get, unprompted: join ON the date condition, no ids · plug in a real date to check which alias is yesterday · select the id of the day being judged.

- [ ] 29 Sep — **Remove Duplicates from Sorted Array (LC 26)** — heavy guidance. Compared k to k+1 instead of reading nums[i], branches swapped (wrote on duplicates), wrote before moving k, returned k instead of k + 1.
  Must get, unprompted: decide what k means BEFORE coding ("last kept" or "next empty") · reader starts at 1 · duplicates do nothing · new value: move k, then write · return matches the convention.

- [ ] 30 Sep — **3Sum (LC 15)** — brute force had index tied to j (neighbour bug). O(n²) needed heavy guidance: sorted() result thrown away, left/right set once outside the for, no pointer move after a match (hang), reset to the ends after a match, left -= 1 in the else, stored -nums[i], skip check inside the while (hang), nums[i - 1] at i = 0, skip condition flipped.
  Must get, unprompted: nums.sort() · break if nums[i] > 0 · skip if i > 0 and same as previous, BEFORE setting pointers · left = i + 1, right = end · on match: append, both in, skip repeats on left · explain why moving inward can't miss a pair.

## Closed

- [x] 28 Aug — Merge Sorted Array — hint on drain loop — solved cold 29 Aug
- [x] 28 Aug — Best Time to Buy and Sell Stock — brute force only — solved one-pass 29 Aug
- [x] 4 Sep — Contains Duplicate II — cold redo crashed on `len(check) != 0` instead of `value in check` — clean first attempt 6 Sep
- [x] 4 Sep — Valid Anagram — used `< 0` without being able to justify it — explained the length-check dependency correctly 6 Sep
- [x] 5 Sep — Group Anagrams — counting key needed heavy prompting — structurally right cold 6 Sep, including `[0] * 26` inside the loop
- [x] 18 Sep — Missing Number (XOR) — over 25 min, needed the `[0,1,3]` trace — solved cold 24 Sep with a two-pass XOR, unaided
- [x] 21 Sep — Subarray Sum Equals K — needed the full code before the idea landed — solved cold 24 Sep
- [x] 5 Sep — Majority Element (Boyer-Moore) — failed cold twice (check at the bottom) — solved cold 1 Oct with the check at the top, and stated the argument after one clue: each decrement cancels a pair, the majority has more than n/2 copies, so the others run out first. Cold code used two `if`s instead of `if / elif / else`: correct, but write the three-branch version next time

## Recurring habits (not problems)

These cost time in multiple sessions. None of them are conceptual.

- **Repeating a key expression instead of assigning it to `key`** — flagged six times. On 6 Sep you finally made the variable and then didn't use it on the next line. `tuple(...)` is O(k) per call, so by Group Anagrams this stopped being cosmetic. Two Sum II on 27 Sep computed the sum twice per loop, Container With Most Water on 30 Sep computed the area twice
- **`.get(k, default)` inside `if k not in d`** — the `.get()` can only return the default. Unreachable code, and unreachable code is where bugs hide
- **Naming**: `i` for a non-index (4x) · `is_valid` / `valid` for a dict of counts (3x) · `alphabet` for a list of counts · `immutable_conversion` describing the mechanism instead of the meaning
- **Sending code before running it** — the `complement` line outside the loop, the `immuatble_conversion` typo, `employees` vs `employee`, `return subarrays3`. Week 4: swap line that swapped a value with itself, `RIGHTWITH`, `yelp_businesses`, missing `)` on UNNEST, `t.total_orders` after renaming the column. Run it first
- **Dead edge-case branches** — 18 Sep, `range_sum` had `if len(prefix) == 0` and `== 1` guards that could never fire. Edge cases are things to **test**, not `if`s to add. Ask "can this condition actually happen?" before writing the branch
- **Fixed details regressing on the cold redo** — Plus One on 24 Sep lost the early return and the `if carry:` after the loop, both of which were fixed on Friday. Then dropped the final `return digits`. The logic survived, the details didn't. When you close a problem, write down the two or three details you had to be told, and check for them on the redo
- **Loop bounds off by one** — `range(1, len(nums), -1)`, stop at 1 instead of -1, `range(len(nums) - 1)` skipping the last index. Before running any loop, say out loud which indices it visits
- **Calling something that returns a new object and not keeping it** — `sorted(nums)` on its own in 3Sum (30 Sep), then `df.rename(...)` twice on 1 Oct. `sorted()` and most pandas methods (`rename`, `sort_values`, `drop`, `fillna`) don't change the original. Assign it (`df = df.rename(...)`) or chain it, or it's gone
- **One set of brackets for several columns** — `df["a", "b", "c"]` twice on 1 Oct. That looks for one column named the whole tuple. Several columns = `df[["a", "b", "c"]]`
- **Returning `nums` from in-place functions** — Monday reverse, Wednesday Move Zeroes. In-place means return nothing (or k if asked). Returning the list makes callers think it's a copy

## SQL habits

- **A CTE holding one value used bare in WHERE, or joined ON a column it doesn't have** — three times on 19 Sep, then `ON c.id = t.id` on 25 Sep. A one-row CTE attaches with CROSS JOIN, no ON
- **Aggregating over a column that's also in the GROUP BY** — `b.bonus` 18 Sep, `risk_category` 19 Sep, `review_count` 25 Sep, `user_id` 27 Sep. Four times. Check before running: anything inside COUNT/SUM must not be in GROUP BY. Find the "for each" in the question, that's the only thing you group by
- **Aliases used outside the query they belong to** — `b.worker_ref_id` in the outer query (18 Sep), `l.user_id` in the final SELECT (23 Sep). An alias defined inside a CTE doesn't exist outside it
- **Aggregate in WHERE** — `timestamp = MAX(timestamp)` on 23 Sep. WHERE runs before GROUP BY. Filter with WHERE, aggregate in SELECT with GROUP BY
- **NULL vs ''** — `IS NOT NULL` doesn't catch empty strings, and `x || NULL` is NULL. Check which one the blanks are before filtering