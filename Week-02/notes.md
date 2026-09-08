# Week 2 — Hashmaps and sets

## Mon 31 Aug — dicts, sets, hashing

**What a hash function does**

Turns a value into a number, and that number is used as an address. It is not random — it is deterministic. `hash("apple")` gives the same result every time within a run, which is the whole reason lookup works. The number just looks scattered.

**Why lookup is O(1) but building is O(n)**

Building visits every item once, hashing each one and placing it, so O(n).
Looking one up afterwards is a single calculation and a single jump, so O(1).

The set is an investment: pay O(n) once, then every future lookup is free. Roughly 6–7 lookups before it beats scanning a list. Also costs extra memory — a hash table keeps ~1/3 of its slots empty on purpose so collisions stay rare.

**Why lists can't be dict keys**

Lists are mutable, meaning they can be changed. Imagine you have a key and then something is appended to it — it will point to a completely different hash value, with nothing stored there. The item is still in the dict but permanently unreachable. Tuples and strings can't change, so their hash is stable, so they're allowed.

Hashable = can't change. Required because the hash *is* the address.

**Reading complexity off a line: count the passes**

Read left to right, ask at each operation: does this touch every element?

- 0 passes → O(1)
- 1 pass → O(n)
- a pass nested inside a pass → O(n²)

Don't classify by which data structure appears. Count passes.

| Free (0 passes) | Costs a pass |
|---|---|
| `len(x)` | `set(x)`, `list(x)` |
| `d[key]`, `key in d` | `x in some_list` |
| `s.add(x)`, `x in s` | `for item in x` |
| `nums[5]`, `nums.append(x)` | `sum(x)`, `max(x)`, `min(x)` |

`sorted(x)` is O(n log n) — worse than one pass. Covered properly in week 3.

`len()` is free because a list stores its own size and updates it on every append. There is no equivalent stored sum, so `sum()` has to visit everything.

## Corrections from tonight

- `hash(42) == hash(42.0)` because `42 == 42.0`. Equal things must hash equally, or `d[42]` and `d[42.0]` would land in different slots. Same last-write-wins trap as `{len(word): word}` in week 1.
- `{}` is an empty **dict**, not an empty set. Use `set()`.
- Naming: `counts` not `dictionary`, `word` not `i`, `pair` not `word` when iterating `.items()`. A name should say what it holds, not what type it is.
- `set(nums)` inside a function does not make the function O(1). The lookup is O(1); the construction is O(n).

## The counter pattern

Check, default, update. Written out long-hand:

```python
counts = {}
for word in text.split():
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
```

The loop body is boilerplate. **The key is the decision.** Same four lines, different key:

- count words → key is `word`
- count first letters → key is `word[0]`
- group anagrams → key is the sorted letters of the word

Shorter forms (rebuild properly on Tuesday):

```python
counts[word] = counts.get(word, 0) + 1        # .get with a fallback

counts = defaultdict(int)                      # missing keys auto-create as 0
counts[word] += 1                              # careful: reading a key creates it

counts = Counter(text.split())                 # deletes the loop entirely
counts.most_common(3)
```

`Counter` only works when the value is a count. Two Sum needs a dict of indexes, group anagrams needs a dict of lists — neither is a `Counter` problem, both are the four lines above.

## Measured tonight

100,000 items, single lookup:

```
list:  0.000481   s
set:   0.0000013  s     ~370x faster
build: ~0.003     s     more than several thousand list lookups
```

## Complexity drill

```python
sum(nums)                      # O(n)  — visits everything
nums[0]                        # O(1)
for w in words: w in some_set   # O(n)
for w in words: w in some_list  # O(n²)
```

Last two are one word apart. That difference is the point of the week.

## Trade to say out loud

n² time down to n time, at the cost of n space.

Two Sum: brute force is O(n²) time, O(1) space. Hashmap is O(n) time, O(n) space. Spend memory to buy speed — almost always the right trade.