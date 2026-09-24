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
| 6 Sep | Two Sum (cold) | Easy | Unaided | | Clean. Added a first-index guard that wasn't there before — fine here, but it's the opposite of Contains Duplicate II. Decide deliberately, don't let it creep in |
| 6 Sep | Valid Anagram (cold) | Easy | Unaided | | `< 0` again, but explained the length-check dependency correctly this time. **Closed** |
| 6 Sep | Contains Duplicate II (cold) | Easy | Unaided | | First attempt, `value in last_seen`. **Closed** |
| 6 Sep | Group Anagrams (cold) | Medium | Unaided | | Counting version, structurally right cold including `[0] * 26` inside the loop. Slips: unused `key` variable, pointless f-string, typo. **Closed** |
| 6 Sep | Majority Element (cold) | Easy | Hint | | Regressed to the bottom-check structure with `count < 1` and a `0` seed. Passes LeetCode either way — the guarantee hides it. **Stays open** |
| 18 Sep | Single Number | Easy | Unaided | | Went straight to XOR after the primer, then wrote the hashmap version for contrast. Pairs cancel, `0 ^ x = x` |
| 18 Sep | Missing Number | Easy | Hint | 25+ | Set and maths (`n(n+1)//2`) versions unaided. XOR version needed the `[0,1,3]` trace to land. Final `^= len(nums)` because enumerate stops one short |
| 19 Sep | Intersection of Two Arrays | Easy | Unaided | | Set version first. Redundant `not in result` check before `.add()`. Brute force, one-liner, and derived the sorted two-pointer rules with prompting |
| 20 Sep | Plus One | Easy | Hint | | Needed a walkthrough of what hand-tracing means. Insert first sat inside the loop keyed on `digits[0] == 0`; early return added after prompting. Walk right to left because carries flow left |
| 21 Sep | Subarray Sum Equals K | Medium | Failed | | Brute force after three loop fixes. Prefix-array version was O(n²) and O(n) space, strictly worse. Needed the full hashmap code before `prefix[l] = prefix[r+1] - k` clicked |
| 23 Sep | Product of Array Except Self | Medium | Hint | | Left-times-right framing handed over. Needed help on reverse loop bounds (`range(n-2, -1, -1)`). O(1) version came after range fix |
| 24 Sep | Single Number (cold) | Easy | Unaided | | Self-reported |
| 24 Sep | Missing Number (cold) | Easy | Unaided | | Two-pass XOR, range then values. **Closed** |
| 24 Sep | Intersection of Two Arrays (cold) | Easy | Unaided | | Set plus `remove()` to handle uniqueness. Couldn't produce the sorted follow-up without the rules restated |
| 24 Sep | Plus One (cold) | Easy | Hint | | Logic survived, details didn't: lost the early return and `if carry:` from Friday, then dropped the final `return digits` |
| 24 Sep | Prefix sum build + range_sum (cold) | Easy | Unaided | | Correct first time. Wrote it as a script before wrapping in functions |
| 24 Sep | Subarray Sum Equals K (cold) | Medium | Unaided | | Self-reported. **Closed** |
| 24 Sep | Product of Array Except Self (cold) | Medium | Hint | | O(n) space clean. O(1) failed twice: no accumulator, then read `output[j]` while writing `output[j-1]`. **Stays open** |