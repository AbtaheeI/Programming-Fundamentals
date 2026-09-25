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

# Week 4 Tuesday · Same-direction pointers

## Reader / writer
- Reader `r` visits every element. Writer `w` marks the next slot to fill.
- Reader always moves. Writer only moves when it writes.
- Invariant: everything before `w` is finished and correct. Everything from `w` on is junk nobody reads.

w = 0
for r in range(len(nums)):
    if keep(nums[r]):
        nums[w] = nums[r]
        w += 1
return w

- Return `w`, not `w + 1`. `w` is the NEXT slot to fill, and since indexes start at 0, that equals the count.
- `w <= r` always, so the writer only overwrites slots the reader has already passed. Nothing unread gets lost.
- `nums[w:]` is leftover originals (can include copies of moved values). Don't clean it up: the caller only reads `nums[:w]`.
- Never delete. `pop(i)` / `del` shifts everything, O(n) each, O(n²) total. Reader/writer is O(n) time, O(1) space.
- The `if` is the KEEP condition. Check it says what you want kept. Positive means `> 0`, zero isn't positive.
- Print `nums[:k]`, not just `k`, when testing. The count alone hides which elements survived.

## Fast / slow
- Both move every step, different speeds: slow 1, fast 2.
- When fast hits the end, slow is at the middle. Used on linked lists (no indexes, no len()). Week 7.
- Reader/writer vs fast/slow: reader/writer = one pointer moves conditionally. Fast/slow = both always move, different speeds.

## Sort first?
- Unsorted + need a pair: sort O(n log n), then converge O(n). Beats O(n²).
- If the question wants original INDEXES, sorting breaks it. Use a hashmap.
- Pair exists (True/False), no indexes: both work.
  - Hashmap: O(n) time, O(n) space
  - Sort + converge: O(n log n) time, O(1) extra space

## Input shape signals
- Sorted, find a pair → converging
- Mirror / reverse / palindrome → converging
- "In place", "return k", "first k elements" → reader/writer
- Middle of something, cycles → fast/slow
- Need original indexes → hashmap, don't sort