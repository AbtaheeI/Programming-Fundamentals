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

# Week 4 Wednesday · Valid Palindrome + Move Zeroes

## LC 125 Valid Palindrome (converging)
l, r = 0, len(s) - 1
while l < r:
    if not s[l].isalnum():
        l += 1
        continue
    elif not s[r].isalnum():
        r -= 1
        continue
    elif s[l].lower() != s[r].lower():
        return False
    l += 1
    r -= 1
return True

- O(n) time, O(1) space.
- `continue` after a skip sends it back through `while l < r`, so the bounds check comes free.
- Don't use `list(s)` to read characters. Strings index directly with `s[l]`. `list(s)` builds a whole new list every call: inside a loop that's O(n²) time, O(n) space.
- Only need `list(s)` when you want to CHANGE characters (strings are immutable).
- Cleaned string vs `[::-1]` works but is O(n) space. Pointer version is the target.

## LC 283 Move Zeroes (reader/writer)

Swap version, one pass:
k = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[k], nums[i] = nums[i], nums[k]
        k += 1

- Swap pushes the zero forward instead of losing it.
- Invariant: before `k` = finished non-zeros. From `k` to `i - 1` = always zeros.
- When there are no zeros yet, `k == i` and it swaps with itself. Harmless.

Two-loop version:
k = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[k] = nums[i]
        k += 1
for i in range(k, len(nums)):
    nums[i] = 0

- Tuesday's overwrite loop, then fill the tail with zeros.
- Unlike Tuesday, `nums[k:]` can't be left as junk here: the problem wants the zeros there.

Both: O(n) time, O(1) space.
- Writes: swap = 2 per non-zero. Two loops = n total. Swap is NOT faster.
- Interview answer: name both, same complexity. Two loops is easier to reason about, swap is a single pass.

## General
- In-place problems return nothing. Drop `return nums`. (Flagged Monday too.)