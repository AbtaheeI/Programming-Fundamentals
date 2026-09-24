# Week 4 Monday · Converging two pointers


l = 0<br>
r = len(nums) - 1<br>
while l < r:<br>
    # look at nums[l], nums[r]<br>
    # move l, r, or both. At least one MUST move.<br>

- `<` when you only care about pairs. `<=` when the middle element needs handling on its own.
- O(n): each iteration moves at least one pointer inward, so the gap shrinks by 1+ every time. At most n iterations.
- Reversal takes n // 2 swaps. With `<=` on odd length, the middle swaps with itself: harmless, just wasted.

## Reverse
- reverse_in_place(nums) = reverse_range(nums, 0, len(nums) - 1). Write the general one, call it for the special case.
- reverse_range time is O(j - i), not O(n). The whole list's size never enters it. Always say what n is.
- Space O(1) for both: two indexes, nothing else.
- In-place functions return None (like list.reverse(), list.sort()). Returning nums makes callers think it's a copy.

## Shape recognition
- Sorted + find a pair → converging. Moving l raises the sum, moving r lowers it.
- Remove/keep in place + return length → same-direction (reader/writer).
- Palindrome / mirror → converging.
- Counting → neither, hashmap.

## Why one-pass swapping doesn't sort
- One pass comparing everything to nums[0] only fixes index 0 (the min). Repeat for every index = selection sort, O(n²).
- Converging beats it because sorted input already tells you where the extremes are, so every comparison places an element for good.