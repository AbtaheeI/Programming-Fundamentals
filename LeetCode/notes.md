# Week 1 — Notes

What clicked, what didn't, and what to carry forward.

---

## Python

**Comprehensions vs constructors.** If the expression is identical to the loop target, you don't need a comprehension — use `list()`, `dict()`, `tuple()`. Unpacking and repacking unchanged is wasted work. Comprehension = transforming. Constructor = collecting.

**Filter `if` vs ternary `if/else`.** Filter goes at the end, no `else`, output can shrink. Ternary goes at the front in the expression slot, needs an `else`, output stays the same length.

**Dict keys must be unique.** A later item with the same key silently overwrites the earlier one. No error, no warning — just fewer rows than you started with. Values can repeat freely; only keys collide.

**No such thing as a tuple comprehension.** `(x for x in y)` is a generator. Use `tuple(...)` around a generator instead.

**Slicing is forgiving, indexing is strict.** `nums[10]` raises; `nums[10:20]` returns `[]`. A wrong slice fails silently.

**Negative step flips the defaults.** `nums[::-1]` works because both ends are omitted. Write explicit numbers with a negative step and the start must be *after* the stop, or you get nothing.

**`sorted(key=)`** — the key is a function. `sorted` calls it once per element and supplies the argument. Bare references (`len`, `str.lower`) work when the element *is* the thing being measured; digging into a structure means writing your own function. Tuple keys give multi-level sorts; negate a number to reverse just that level.

---

## Data structures

**`in` on a list is O(n). `in` on a set is O(1).**
Hit this early on Contains Duplicate. Lists scan; sets hash and jump straight there. This single difference collapses O(n²) into O(n) and is the core of week 2.

Trade-off: sets lose order and can't hold duplicates. Use `.add()`, not `.append()`.

---

## Loops

**`for` vs `while`.**
- `for` — you know what you're iterating over. One pointer visits every position unconditionally.
- `while` — you're looping until a condition changes. Multiple counters moving at different rates, or an end condition based on values rather than position.

**The tell:** if you're writing a guard inside a `for` that duplicates what the loop condition should be, it should be a `while`. Hit this on Merge Sorted Array.

---

## The recurring DSA idea this week

**The writer never touches data the readers still need.**

Three problems, three ways of achieving it:

- **Running Sum** — read one position behind, which is already finalised
- **Remove Element** — writer lags behind the reader, only advancing on a keep
- **Merge Sorted Array** — reverse direction entirely, writing into empty space first

Same invariant every time. Worth recognising when it shows up again.

---

## SQL

**`ON` decides what matches. `WHERE` decides what survives.**
On an INNER JOIN it makes no difference. On a LEFT JOIN it changes everything — a `WHERE` on the right table silently converts it to an INNER JOIN, because `NULL = 'anything'` is never true.

**Join on the key that expresses the relationship**, not on any column the two tables happen to share. A reaction belongs to a post, so join on `post_id`, not on `poster`.

**The phantom row.** LEFT JOIN fabricates a row when there's no match — real data on the left, NULLs on the right. It's a real row in the result. `COUNT(*)` counts it and reports 1 where the answer is 0. Always `COUNT` a column from the optional table after an outer join.

**Anti-join.** LEFT JOIN, then `WHERE <optional table's primary key> IS NULL`. Test the key specifically, because a primary key can never legitimately be NULL — so NULL there can only mean "no match found." Test the preserved side and you get zero rows every time.

**Row multiplication.** A one-to-many join duplicates the "one" side. Counting it without `DISTINCT` inflates the number. Sydney showed 4 customers instead of 2 because Aaron had three orders.

**`IS NULL`, never `= NULL`.** NULL isn't a value; nothing equals it, including another NULL.

**Empty-set aggregates.** `COUNT` returns 0. `SUM`, `AVG`, `MIN`, `MAX` return NULL. Wrap `SUM` in `COALESCE(..., 0)` when zero is the honest answer — but not `MAX`, where NULL genuinely means "no orders."

---

## Open / revisit

- Best Time to Buy and Sell Stock — one-pass version didn't land. Scheduled again Saturday.
- Merge Sorted Array — needed a hint on the drain loop. Redo cold.
- `RIGHT JOIN` — understood, but confirm the LEFT equivalent by rewriting one.