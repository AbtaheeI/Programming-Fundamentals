# DSA Log

`Unaided` · `Hint` · `Failed`

| Date | Problem | Difficulty | Result | Time | Notes |
|---|---|---|---|---|---|
| 26 Aug | Running Sum of 1d Array | Easy | Unaided | | Wrote O(n) space version, then in-place O(1) — list carries the state |
| 26 Aug | Remove Element | Easy | Unaided | | Two pointers, writer never overtakes reader. Return k, not the list |
| 28 Aug | Merge Sorted Array | Easy | Hint | | Fill from the back. Needed help on the drain loop for leftover nums2 — and on while vs for when two pointers move independently |
| 28 Aug | Contains Duplicate | Easy | Unaided | | Set for O(1) membership. Learned list `in` is O(n), set `in` is O(1) — big one |
| 28 Aug | Best Time to Buy and Sell Stock | Easy | Failed | | Brute force O(n²) works. One-pass version not landing yet — deferred |
| 29 Aug | Merge Sorted Array (cold) | Easy | Unaided | | Clean from blank. Failure closed |
| 29 Aug | Remove Element (cold) | Easy | Unaided | | |
| 29 Aug | Running Sum (cold) | Easy | Unaided | | Wrote O(n) space first, then in-place. Used range(len()) unnecessarily again |
| 29 Aug | Best Time to Buy and Sell Stock | Easy | Unaided | | One-pass, track min so far + best profit. Ordering of the two ifs turns out to be cosmetic — `profit = 0` is what makes it safe |
| 2 Sep | Two Sum | Easy | Unaided | | Brute force first, then hashmap after working the gap out on paper. Key is the value, index is the payload. Check before store or `[3,3]` matches itself |
| 2 Sep | Two Sum (cold) | Easy | Unaided | 5:23 | |
| 4 Sep | Valid Anagram | Easy | Unaided | | Three ways: sorting O(n log n), manual dict, Counter. `sorted()` is O(n) space — builds new lists |
| 4 Sep | Contains Duplicate II | Easy | Hint | | Idea was right (store `{value: latest index}`) but needed prompting to drop `.get()` and store unconditionally. Keep the newest index — older ones are dominated |
| 4 Sep | Valid Anagram (cold) | Easy | Unaided | | Used `< 0` instead of `!= 0`. Correct but only because of the length check |
| 4 Sep | Contains Duplicate II (cold) | Easy | Failed | | KeyError — wrote `len(check) != 0` instead of `value in check` |
| 5 Sep | Group Anagrams | Medium | Hint | | **First medium.** Got the sorted-word key alone, plus tuple-for-hashability. Needed heavy prompting for the 26-slot counting key and `ord()`. Pattern: group by canonical form |
| 5 Sep | Majority Element | Easy | Hint | | Dict version instant. Boyer-Moore needed most of a session — the token-pile model, `if/elif/else`, and checking `count == 0` at the top |