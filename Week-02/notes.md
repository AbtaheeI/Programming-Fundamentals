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

**Corrections**

- `hash(42) == hash(42.0)` because `42 == 42.0`. Equal things must hash equally, or `d[42]` and `d[42.0]` would land in different slots. Same last-write-wins trap as `{len(word): word}` in week 1.
- `{}` is an empty **dict**, not an empty set. Use `set()`.
- Naming: `counts` not `dictionary`, `word` not `i`, `pair` not `word` when iterating `.items()`. A name should say what it holds, not what type it is.
- `set(nums)` inside a function does not make the function O(1). The lookup is O(1); the construction is O(n).

**Measured** — 100,000 items, single lookup:

```
list:  0.000481   s
set:   0.0000013  s     ~370x faster
build: ~0.003     s     more than several thousand list lookups
```

**Complexity drill**

```python
sum(nums)                       # O(n)  — visits everything
nums[0]                         # O(1)
for w in words: w in some_set   # O(n)
for w in words: w in some_list  # O(n²)
```

Last two are one word apart. That difference is the point of the week.

---

## Tue 1 Sep — defaultdict, Counter, deque

### Three ways to count

Lines inside the loop: **1, 1, 0**

```python
counts[word] = counts.get(word, 0) + 1     # 1 line, no import

counts = defaultdict(int)                   # 1 line, needs import
counts[word] += 1

counts = Counter(text.split())              # 0 lines, loop deleted
counts.most_common(3)
```

`defaultdict` saves nothing over `.get()` when the value is a number. It earns its keep when the value is a **list or a set**.

`defaultdict(int)` — you pass the *function*, not a value. No brackets. Missing key calls it: `int()` is 0, `list()` is `[]`, `set()` is empty set.

### The defaultdict trap

Reading a missing key **creates** it.

```python
counts = defaultdict(int)
counts["the"] += 1
len(counts)          # 1
counts["zebra"]      # returns 0...
len(counts)          # 2 — zebra is now in the dict
```

Silent. No error. Your dict fills with junk and `len()` lies.

**Rule: `[ ]` creates, `in` and `.get()` don't.** Use `[ ]` when storing, `in` or `.get()` when checking.

Careful: `count["zebra"] in count` triggers the bug *and* asks the wrong question (it checks whether `0` is a key). Just `"zebra" in count`.

### list vs deque

A **list** is one continuous block. Items sit physically in order, all the same size, so `nums[500]` is arithmetic: block start + 500 × slot size. One sum, instant. That same layout means position 0 is genuinely occupied — `insert(0, x)` shifts every item right, O(n).

A **deque** is a chain of fixed-size blocks, doubly linked. The leftmost block keeps unused slots on its left, so `appendleft` writes into a slot that was already empty and moves a marker. Nothing shifts. When that block fills, allocate one more and rewire two pointers — still O(1).

The price: `q[500]` walks block by block. Can't calculate an address across separate blocks.

|  | search by value | fetch by index | append/pop left |
|---|---|---|---|
| list | O(n) | **O(1)** | O(n) |
| deque | O(n) | O(n) | **O(1)** |
| set/dict | **O(1)** | n/a | n/a |

Deque is worse than a list at both lookups. You pick it for one reason only: both ends are O(1). Needed for BFS in week 11.

**"Look up by index" and "search for a value" are different questions.**

**Measured** — insert in a loop, 100,000 items:

```
list.insert(0, i)   2.087  s     O(n) inside an n loop  = O(n²)
deque.appendleft(i) 0.0062 s     O(1) inside an n loop  = O(n)
```

Both versions are *correct*. One just picked the container that fights the operation. **The algorithm and the data structure are the same decision.**

### Ensure the container exists, then use it

When both branches of an if/else end the same way, the shared part belongs outside:

```python
groups = {}
for word in text.split():
    key = word[0]
    if key not in groups:      # if only does the setup
        groups[key] = []
    groups[key].append(word)   # runs either way
```

Don't write `groups[key] = groups.get(key, [])` *inside* `if key not in groups`. The key is definitely missing, so `.get()` can only return `[]`. Two safety mechanisms doing one job, and the second is unreachable. (Outside an `if`, `.get(key, [])` is legitimate — it's doing the ensure job itself.)

### Key and value are separate decisions

Grouping by first letter: key is `word[0]`, value is `word`. Changing both is the easy slip — `{"t": ["t","t","t"]}` instead of `{"t": ["the","the","the"]}`.

**Pull the key into a variable.** Repeating the key expression three times is wasted work once it costs something (`tuple(sorted(word))` is O(k) each time), and it's the line you'll forget to update when the rule changes.

### Methods that mutate return None

```python
y = x.append(3)     # y is None. x changed.
```

`.append()`, `.sort()`, `.reverse()`, `.extend()`, `.insert()` all return `None`. Never put them on the right of an `=`.

The ones that return something build a **new** object: `sorted()`, `list()`, `.copy()`, comprehensions. That's also why `sorted(s)` costs O(n) space and `s.sort()` costs O(1).

---

## Wed 2 Sep — Two Sum

Brute force: nested loops, `j = i + 1`. That one choice handles both constraints at once — never pairs an element with itself, never checks the same pair twice. O(n²) time, O(1) space.

The optimisation, stated generally: **if the inner loop is *searching* for something, a dict deletes it.** Searching a list is O(n); searching a dict is O(1).

```python
complement = target - value
if complement in seen:
    return [seen[complement], index]
seen[value] = index
```

**Key is what you search by.** You're looking for the complement, which is a value, so values are keys and the index rides along as the payload. `{2: 0}`, not `{0: 2}`. Feels inside-out compared to a list.

**Check before store.** Order matters. Store first and `[3,3]` with target 6 matches 3 against itself and returns `[0,0]`.

O(n) time, O(n) space. Say the trade out loud: **n² down to n, at the cost of n space.**

**Space is O(1) when nothing you allocate grows with the input.** Two counters and a 2-element return list is O(1) no matter how big `nums` gets.

### Correction to a week 1 note

On Best Time to Buy and Sell Stock, the order of the two ifs is *not* load-bearing. Both orders give the same answer. What's load-bearing is `profit = 0` — a same-day comparison yields 0, and 0 can never beat a profit that starts at 0. It would matter if `profit` started at `-inf`, or the test were `>=`.

---

## Thu 3 Sep — SQL: self-joins and multi-table joins

A self-join is one table joined to itself under two aliases. Two different jobs:

**Following a link.** Employee table with `manager_id` pointing at another row. `ON e.manager_id = m.id`. Write down in English what each alias represents before writing the `ON` — backwards gives a plausible-looking wrong answer.

**Pairing rows to compare them.** No pointer column. The join makes every combination of rows, and you filter down.

### The self-pair problem

A self-join pairs every row with **itself** too. That's the diagonal. It's why:

- "employees earning the same as another employee" returns everyone — each person matches themselves
- fix: `AND a.worker_id <> b.worker_id`

### `<>` vs `<` on the id

- `<>` removes only the diagonal → keeps both `(1,2)` and `(2,1)`. Same pair twice.
- `<` removes the diagonal **and** one side of every mirror → each pair exactly once.

`DISTINCT` does not fix this. `(5,3)` and `(3,5)` are genuinely different rows.

Which to use depends on the output shape: pairs → `<`. One row per entity → `<>`.

### INNER vs LEFT

`LEFT JOIN` keeps every left row **even with no match**, filling the right columns with NULL. So it silently undoes a filter you thought you'd applied. If the answer is "must have a match", it's `INNER`.

### WHERE vs HAVING

**`WHERE` runs before `GROUP BY`. `HAVING` runs after.**

So an aggregate in a `WHERE` fails — nothing has been grouped yet, there's no average to compare to. If the condition mentions `AVG`, `COUNT`, `SUM`, it belongs in `HAVING`.

**`WHERE` filters rows, `HAVING` filters groups.**

Also: `ON` describes how the two copies relate; `WHERE` filters on values. Don't write the same condition in both.

---

## Fri 4 Sep — Valid Anagram, Contains Duplicate II

### Valid Anagram, three ways

```python
return sorted(s) == sorted(t)        # O(n log n) time, O(n) space
```

O(n) space, not O(1) — `sorted()` builds two new lists. Strings are immutable so there's no in-place option.

Manual dict: count up from `s`, count down from `t`, fail on negative. With a length check at the top, `< 0` is sufficient — the counts must sum to zero, so a positive is impossible without a negative. **But that's load-bearing on the length check.** Write `!= 0` unless you can explain the dependency.

```python
return Counter(s) == Counter(t)      # Counters are dicts; == compares contents
```

Interview answer: write the one-liner, say "in production I'd use `Counter`", then write the manual version.

### Contains Duplicate II

Store `{value: most recent index}`. On a repeat, compare the gap.

**Keep the newest index, not the first.** You're scanning left to right, so any future partner is to the right. The most recent occurrence is the closest possible partner for anything ahead; an older one can only be further away. Keeping it is strictly worse — and gives a *wrong answer*, not an error. `[1,0,1,1]`, k=1 is the test.

General form: **when scanning forward and only recency matters, keep the newest.** Older occurrences are dominated.

`abs()` isn't needed — the stored index is always smaller.

### Where the dict pattern applies

The trigger: **have I seen this before, and what do I know about it?**

Three variants, differing only in what the value holds:

| Need | Structure | Example |
|---|---|---|
| Existence | set, no value | Contains Duplicate |
| Position | `{value: index}` | Two Sum, Contains Duplicate II |
| Count | `{value: count}` | Valid Anagram |
| Grouping | `{key: [items]}` | Group Anagrams |

Phrases that mean hashmap: "two elements such that" → complement · "duplicate/distinct/unique" → set · "frequency/most common" → counts · "group by/same when transformed" → dict of lists · "first non-repeating" → counts then second pass.

**Where it does NOT apply:**

- Sorted input → two pointers, O(1) space (Two Sum II, week 4)
- Need order or ranking → dicts don't sort
- Need min/max repeatedly → heap, week 9
- Small fixed range (26 letters) → array beats dict
- "Now do it in O(1) space" → the interviewer is asking you to abandon the dict

---

## Sat 5 Sep — Group Anagrams, Majority Element

### Pattern: group by a canonical form

Items that should be treated as equivalent don't look equal, but each can be transformed **independently** into a form where equivalent items come out identical. The dict does the rest.

1. Find the transformation
2. Make it hashable (tuple or string)
3. `{canonical_form: [original items]}`

**You never compare items to each other.** Each word is transformed alone and the dict matches them. That's why it's n passes, not n² comparisons. This was the hard part to see.

Other instances: rotations → smallest rotation · points on a line → reduced slope as a tuple · isomorphic strings → pattern of first-occurrence positions · duplicate files → hash of contents · shifted strings → gaps between letters.

All thinking goes into step 1. If you can state the transformation out loud, the code is thirty seconds.

Trap: the transformation must be deterministic and must not collide. "Only the non-zero letter counts" fails — nothing fixes their order.

### Group Anagrams, two keys

```python
key = tuple(sorted(word))             # O(k log k) per word
```

`sorted()` returns a **list**, which can't be a key. Convert — `tuple()` or `"".join()`.

```python
counts = [0] * 26                     # O(k) per word — fresh INSIDE the loop
for letter in word:
    counts[ord(letter) - ord("a")] += 1
key = tuple(counts)
```

Write `ord(letter) - ord("a")`, not `- 97`. You don't scan the 26 slots for the right letter — you *calculate* the position and jump, same as `nums[500]`.

| version | time | space |
|---|---|---|
| sorting | O(n · k log k) | O(n · k) |
| counting | O(n · k) | O(n · k) |

n = number of words, k = longest word. **Nested loops are not automatically O(n²)** — count what each loop actually iterates over. Here the outer is n words and the inner is k letters, so O(n · k).

`.values()` returns a **view**, not a list. Wrap in `list()` when the signature says `List[...]`.

### Majority Element — Boyer-Moore voting

Dict version is three minutes. The point of the problem is the O(1) space version.

**Why it works:** the majority appears more than half the time, so it has more copies than everything else combined. Cancel each majority element against one non-majority element and the majority is the only value that can survive.

Two variables: a candidate, and a count of unmatched copies you're "holding". One pass, three branches:

```
if count == 0:   adopt current element, count = 1
elif matches:    count += 1
else:            count -= 1
```

**`if / elif / else`, not two `if`s.** Exactly one action per element or you double-count.

**Check `count == 0` at the TOP, before deciding.** At the bottom, the element that *empties* the pile immediately becomes the candidate — it got counted twice, once cancelling and once adopting. The candidate should be whatever element you're standing on when you find the pile already empty, not the one that emptied it.

The count is a physical pile of tokens. It can't go negative — if it's empty there's nothing left to cancel. Adopting means you're holding **one**, not zero.

No seeding needed. The first iteration has count 0 and adopts `nums[0]` itself.

This is the first problem this week where **the dict is the wrong answer.** After a week of hashmaps the trap is reaching for one by default. Next week is two pointers and sliding window for exactly that reason.