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
| 29 Aug | Best Time to Buy and Sell Stock | Easy | Unaided | | One-pass, track min so far + best profit. Ordering of the two ifs is cosmetic but worth fixing |