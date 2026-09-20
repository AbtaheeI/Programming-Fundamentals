# NeetCode video: Big-O Notation - For Coding Interviews

## What Big-O measures
Time complexity is how the **number of operations** grows as the input size (n) grows. It's not actual seconds. The same code runs faster on a better laptop, but its Big-O doesn't change.

Space complexity is how much **extra memory** the algorithm uses as n grows. A few variables is O(1). A new list/set/dict that grows with the input is O(n).

Rule: assume worst case everywhere **except** hashmaps (dict/set lookups are O(1) on average, worst case O(n) only if every key collides, which basically never happens).

## The classes

### O(1)
Same time no matter how big n gets.
- dict/set lookup and insertion (average)
- `append` to the end of a list (amortised)
- `pop()` from the end of a list

### O(log n)
Every step cuts what's left in half. How many times can you halve n until you hit 1? 2^x = n, so x = log2(n). Base doesn't matter in Big-O, just write log n.
- Binary search: only works on sorted data. Check the middle, throw away the half the target can't be in, repeat. (Week 6)
- Balanced BST: tree where left child is smaller, right child is bigger. Each step down halves the remaining nodes. (Week 9)

### O(sqrt(n))
- Getting all factors of a number. Factors come in pairs (12 = 2x6 = 3x4), so once you pass sqrt(n) you're only seeing the other half of pairs you already found.

### O(n)
Time grows at the same pace as n. Linear.
- Single loop over the input
- Searching an unsorted array
- Inserting or deleting in the middle of an array (everything after has to shift)
- `pop(0)` from the front of a list

### O(n log n)
- Sort first, then loop. `nums.sort()` is O(n log n), the loop is O(n), total O(n log n).
- Merge sort and heapsort are how sorting works under the hood. (Week 9)

### O(n^2)
- Nested loops over the same input
- Insertion sort: take each element and slide it left into the right spot in the sorted part. Each slide can be O(n), done n times.

### O(n * m)
Two independent input sizes. A rectangle, not a square.
- Looping through a grid (rows x columns)
- Looping through two different arrays nested
- Don't simplify to n^2 unless the two sizes are actually the same.

### O(n^3)
- Triple nested loops

### O(2^n)
- Recursion where a function calls itself twice each time. 1 call becomes 2, then 4, then 8. Depth n gives 2^n calls.
- Naive Fibonacci is the classic example. (Weeks 10 and 13)

### O(n!)
- Permutations: n choices for the first slot, n-1 for the second, n-2 for the third. Multiply them all and you get n!.
- Some graph problems

## Ranking: fastest to slowest
1. O(1)
2. O(log n)
3. O(sqrt(n))
4. O(n)
5. O(n log n)
6. O(n^2)
7. O(n^3)
8. O(2^n)
9. O(n!)

O(n * m) doesn't sit at a fixed spot. If m = 1 it's O(n). If m = n it's O(n^2). So it sits somewhere between O(n) and O(n^2) depending on m.


# Week 3 Tuesday: Prefix Sums

## The problem it solves
Lots of questions like "what's the sum from index l to index r?"

Brute force: loop from l to r and add. O(n) per query. With q queries that's O(n*q).
Prefix sums: one O(n) pass up front, then every query is O(1).

## What a prefix sum array is
Each position stores the running total of everything before it.

nums   = [2, 4, 1, 5]
prefix = [0, 2, 6, 7, 12]

- It's ONE LONGER than nums
- prefix[0] = 0, the sum of zero elements
- prefix[i] = sum of the FIRST i elements

Running Sum from week 1 is this without the leading 0.

## The formula
sum of nums[l..r] = prefix[r + 1] - prefix[l]

Everything before the range cancels out.

## Why the leading 0
Without it, a range starting at index 0 has nothing before it to subtract, so you need an `if l == 0` special case. The 0 makes "nothing before" a real slot, so there's one formula and no branch.

Both versions are accepted in interviews. The padded one is preferred because:
- Fewer special cases = fewer off-by-one errors under pressure
- It scales: 2D prefix sums without padding need special cases for the top row, left column AND corner
- Some later problems need the "sum of nothing = 0" slot to work at all

Say why as you write it: "I pad with a 0 so a range starting at index 0 doesn't need a special case."

Same idea as the dummy head node (week 7): one fake element that removes an edge case.

## The code
```python
def build_prefix(nums):
    prefix = [0] * (len(nums) + 1)

    for index, value in enumerate(nums):
        prefix[index + 1] = prefix[index] + value

    return prefix

def range_sum(prefix, l, r):
    return prefix[r + 1] - prefix[l]
```

build_prefix: O(n) time, O(n) space
range_sum: O(1) time, O(1) space

No edge case branches needed. The formula handles empty ranges, single elements and the whole array on its own. Edge cases are things to TEST, not ifs to add.

Gotcha: `[0] * len(nums) + 1` is wrong. `*` binds before `+`, so it's (list) + 1 and crashes. Needs `[0] * (len(nums) + 1)`.

## Complexity tradeoff
|              | Build | Each query | Space |
|--------------|-------|------------|-------|
| Brute force  | none  | O(n)       | O(1)  |
| Prefix sums  | O(n)  | O(1)       | O(n)  |

Worked example: array of 100,000, with 50,000 queries
- Brute force: 50,000 x 100,000 = 5,000,000,000
- Prefix sums: 100,000 build + 50,000 queries = 150,000
- About 33,000x fewer operations

## When brute force is actually better
The build is a FIXED UPFRONT COST. It only pays off spread over enough queries.

With only 2 queries on a 100,000 array:
- Brute force: 200,000
- Prefix sums: 100,002
Basically the same, and prefix costs 100,000 slots of memory for it.

So: few queries, or short ranges, and it's not worth it.

Also: if the array CHANGES between queries the prefix array is invalid and you'd rebuild every time, which kills the whole idea. The structure for that case is a Fenwick tree (not on the plan, just know it exists).

## The bigger idea: it's not just sums
A prefix array stores a running total of ANYTHING COUNTABLE.
Convert each element to a number, then prefix that. The query formula never changes.

Counting evens in a range:
nums    = [3, 4, 6, 1]
is_even = [0, 1, 1, 0]      <- convert: even = 1, odd = 0
prefix  = [0, 0, 1, 2, 2]   <- normal build_prefix on is_even

Evens in nums[1..2] = prefix[3] - prefix[1] = 2 - 0 = 2

prefix[i] now means "how many evens in the first i elements".

Same trick for: how many negatives in a range, how many vowels in a substring, etc.

## Signals in a problem
"sum of a subarray", "range", "many queries", "contiguous"

Prefix sums get much stronger paired with a hashmap (Saturday).

## Sum shortcut worth remembering
1 + 2 + 3 + ... + n = n(n+1)/2, which is O(n^2)

Pairing proof: write the sum forwards and backwards, add column by column, every column is (n+1), there are n of them. So 2x the sum = n(n+1).

Shows up any time a loop shrinks by one each round: nested loop with `range(i, n)`, string building with +=, insertion sort.

# Week 3 Wednesday: XOR, Single Number, Missing Number

## XOR basics
XOR is `^`. Compares two numbers bit by bit. Each position gives 1 if the bits DIFFER, 0 if they're the same.

  5  =  1 0 1
  3  =  0 1 1
  ^ -----------
         1 1 0   = 6

Three properties do all the work:
- `x ^ x == 0`    anything XOR itself cancels to zero
- `x ^ 0 == x`    zero leaves a number unchanged
- order doesn't matter, so `a ^ b ^ c` can be rearranged freely

Example: `2 ^ 7 ^ 2` = 7. Reorder to `2 ^ 2 ^ 7`, the 2s cancel to 0, and `0 ^ 7` is 7.

## When to reach for XOR
Signals:
- Things appear in PAIRS and you want the odd one out
- The problem explicitly demands O(1) extra space and a hashmap/set is the obvious answer
- Finding the DIFFERENCE between two nearly-identical sets
- Words like "appears twice", "appears once", "duplicate", "missing" next to a space constraint

Don't use it when:
- You need counts, not just presence
- Things appear three times (different trick)
- Order or position matters

The reasoning path in an interview: "set version is O(n) space, they want O(1), what can I accumulate into a single variable?" Sum works. XOR works. Those are the two options in that bucket.

It's only about 4-5 problems in the whole NeetCode 150. Small tool, sharp edge.

## Single Number (LC 136)
Every element appears twice except one. Find it.

Hashmap version:
```python
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1
for num in count:
    if count[num] == 1:
        return num
```
O(n) time, O(n) space. Dict holds up to n/2 + 1 keys.

XOR version:
```python
result = 0
for i in nums:
    result ^= i
return result
```
O(n) time, O(1) space.

Why it works: every duplicate pair cancels to 0, and `0 ^ lone_number` is the lone number.

## Missing Number (LC 268)
n distinct numbers from the range [0, n]. One is missing.

Set version:
```python
new_num = set(nums)
for num in range(len(nums) + 1):
    if num not in new_num:
        return num
```
O(n) time, O(n) space.

Maths version:
```python
expected = (len(nums) + 1) * len(nums) // 2
return expected - sum(nums)
```
O(n) time (because of `sum(nums)`), O(1) space.
Uses the n(n+1)/2 shortcut from Tuesday.
Use `//` not `int(.../2)` — `/` makes a float and loses precision on big numbers.

XOR version:
```python
output = 0
for index, value in enumerate(nums):
    output ^= index
    output ^= value
output ^= len(nums)
return output
```
O(n) time, O(1) space.

Why it works: XOR the whole range 0..n and all the values into one pile. Every number present in BOTH cancels itself. Only the missing one survives.

The final `output ^= len(nums)` is the bit people miss: `enumerate` only reaches index n-1, but the range goes to n. That last index has to be added manually.

Trace with nums = [0, 1, 3], n = 3:
- range is 0,1,2,3 and values are 0,1,3
- pile: 0^1^2^3^0^1^3
- the 0s, 1s and 3s cancel, 2 survives

## Complexity table
| Version                   | Time | Space |
|---------------------------|------|-------|
| Single Number, hashmap    | O(n) | O(n)  |
| Single Number, XOR        | O(n) | O(1)  |
| Missing Number, set       | O(n) | O(n)  |
| Missing Number, maths     | O(n) | O(1)  |
| Missing Number, XOR       | O(n) | O(1)  |

## Overflow (why the maths version is riskier in other languages)
In Java/C++ an int has a fixed size (32 bits, max ~2.1 billion). Go past it and the number silently WRAPS to a large negative. Wrong answer, no error.

With a big array, `n(n+1)/2` can blow past that even though the final answer is small.

Python ints grow to whatever size they need, so there's no ceiling. If asked "what if this were Java?" the answer is: use a 64-bit type, or restructure to subtract as you go so the running total never gets large. The XOR version avoids the problem entirely.

# Week 3 Thursday: Subqueries & CTEs

## Correlated vs uncorrelated
UNCORRELATED: the inner query doesn't mention the outer query. Computed ONCE, reused for every row.
```sql
SELECT name FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

CORRELATED: the inner query references the outer query's alias. Recomputed FOR EVERY ROW.
```sql
SELECT name FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id);
```
The `e.dept_id` is what makes it correlated. The answer changes per row, so SQL can't reuse it.

Cost: outer has n rows, inner scans n rows each time = O(n^2). Same nested loop shape as Python.

Nuance for interviews: query planners often rewrite correlated subqueries into joins or window functions, so it isn't always O(n^2) in practice. Assume the worst when writing, reach for a CTE or window function on big tables.

## Using a CTE that holds ONE value
Caught me three times in one session. A CTE is a TABLE, not a value. You can't reference its column bare in a WHERE.

Wrong:
```sql
WHERE cool = max_cool          -- max_cool is a table, SQL has no idea what this is
```

Three ways to fix:
1. Subquery expression: `WHERE cool = (SELECT max_cool FROM maximum_cool)`
2. CROSS JOIN it in: one row crossed onto every row puts the column in scope
3. INNER JOIN on the comparison: `JOIN maximum_cool m ON c.cool = m.max_cool`

CROSS JOIN is the cleanest for "one value I need everywhere".

Also: always alias an aggregate. `SELECT MAX(cool)` gives an auto-generated column name you can't reference. `SELECT MAX(cool) AS max_cool`.

## GROUP BY rule (hit this twice in two days)
THE COLUMN YOU'RE AGGREGATING NEVER APPEARS IN THE GROUP BY.

Grouping by the thing you're trying to collapse means nothing collapses. Each distinct value becomes its own group and the aggregate only ever sees one row.

Wrong:
```sql
SELECT id, SUM(bonus) FROM t GROUP BY id, bonus     -- one row per bonus, SUM does nothing
```
Right:
```sql
SELECT id, SUM(bonus) FROM t GROUP BY id
```

GROUP BY holds the columns you want ONE ROW PER. Nothing else.

## Aggregating twice at two grains
The main reason to reach for a CTE.

Signal: "I need to aggregate, then aggregate the RESULT of that aggregate."

Income by Title and Gender:
```sql
WITH total_compensation AS (
    SELECT e.employee_title, e.sex, (e.salary + SUM(b.bonus)) AS total
    FROM sf_employee e INNER JOIN sf_bonus b ON e.id = b.worker_ref_id
    GROUP BY e.id, e.employee_title, e.sex, e.salary
)
SELECT employee_title, sex, AVG(total) AS avg_compensation
FROM total_compensation
GROUP BY employee_title, sex
```
CTE grain: one row per EMPLOYEE (bonuses summed).
Outer grain: one row per TITLE+SEX (employees averaged).

Can't be done in one query. You can't average totals that don't exist yet.

Also: carry through the columns the outer query needs (title, sex). Saves joining back to the source table.

## Chained CTEs
Each CTE can reference any CTE defined BEFORE it. Forwards only.

```sql
WITH customer_totals AS (
  SELECT cust_id, SUM(total_order_cost) AS total_spent
  FROM orders GROUP BY cust_id
),
avg_spending AS (
  SELECT AVG(total_spent) AS avg_total
  FROM customer_totals          -- reads the one above
)
SELECT ...
FROM customer_totals ct
CROSS JOIN avg_spending a
WHERE ct.total_spent > a.avg_total
```

Swap their order and it breaks. Each CTE is one step, building on the steps before it.

## When a CTE is NOT pulling its weight
A CTE earns its place when it TRANSFORMS something: aggregates, filters, reshapes.
One that only picks columns is a rename, not a step.

```sql
WITH cool_reviews AS (
    SELECT business_name, review_text, cool FROM yelp_reviews    -- pointless
)
```
Just query the table directly.

## CASE WHEN: text to rankable numbers
Signal: "highest severity", "worst", "best" on a TEXT column. Convert to numbers first, then MAX.

```sql
MAX(CASE WHEN risk_category = 'High Risk' THEN 3
         WHEN risk_category = 'Moderate Risk' THEN 2
         WHEN risk_category = 'Low Risk' THEN 1
         ELSE 0
    END) AS risk_level
```
Needs `END`, needs an alias, and it's one item in the SELECT list so it needs a comma after it.

## CASE WHEN: pivoting rows into columns
Turn one column of categories into several columns of counts.

```sql
SUM(CASE WHEN risk_level = 0 THEN 1 ELSE 0 END) AS no_risk,
SUM(CASE WHEN risk_level = 1 THEN 1 ELSE 0 END) AS low_risk,
SUM(CASE WHEN risk_level = 2 THEN 1 ELSE 0 END) AS moderate_risk,
SUM(CASE WHEN risk_level = 3 THEN 1 ELSE 0 END) AS high_risk,
COUNT(*) AS total
```
Each CASE gives 1 when it matches, 0 when it doesn't. SUM adds them up.

## Clause evaluation order
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

Consequences:
- WHERE CANNOT see SELECT aliases. SELECT runs later, the alias doesn't exist yet.
- ORDER BY CAN see them. It runs after SELECT.
- HAVING exists because you need a way to filter AFTER grouping.

To filter on a computed column, three options:
1. Repeat the whole expression in WHERE (works, but now it's written twice)
2. Wrap it in another CTE and filter outside (cleanest)
3. HAVING, but only when filtering an aggregate straight after a GROUP BY

## Integer division
`dept_size / total` truncates to 0 when both are ints. A trailing `* 100.0` is TOO LATE, the division already happened.

Fix: `CAST(dept_size AS FLOAT) / NULLIF(total, 0) * 100`

`dept_size * 100.0 / total` also works via precedence, but the CAST says what you mean, survives edits, and behaves the same across engines.

`NULLIF(x, 0)` guards divide-by-zero by turning 0 into NULL.

## Join gotcha
```sql
JOIN dept_avg d ON e.department = e.department     -- always true, silent cross join
```
Check the alias on BOTH sides of an ON clause. `e.x = e.x` is a cross join in disguise.

# Week 3 Friday: Intersection of Two Arrays, Plus One

## Intersection of Two Arrays (LC 349)
Two arrays, return elements in both. Result must be unique, order doesn't matter.

Brute force:
```python
ls = set()
for i in nums1:
    for j in nums2:
        if j == i:
            ls.add(j)
return list(ls)
```
O(n*m) time. Space O(min(n, m)) — the set can only hold values present in BOTH arrays, so it's capped by the smaller array.

Set version:
```python
hash_set = set(nums1)
result = set()
for i in nums2:
    if i in hash_set:
        result.add(i)
return list(result)
```
O(n + m) time: O(n) to build the set, O(m) for the loop. Sequential, so they add.
O(n) space.

Note: `i not in result` before `result.add(i)` is redundant. A set already ignores duplicate adds. Same class of mistake as using a dict when only the keys matter — let the data structure do its job.

One-liner:
```python
return list(set(nums1).intersection(nums2))
```
`.intersection()` takes any iterable, so no need to wrap nums2 in set() — that's O(m) space for nothing.
`set(nums1) & set(nums2)` is the operator form.

Interview approach: write the explicit version first to show the reasoning, THEN say "in production I'd use the built-in". You get credit for both.

## Follow-up: what if both arrays were sorted?
Then you don't need a set at all. Two pointers, one per array, O(1) space.

- Values EQUAL: it's a match, move both pointers
- Left value SMALLER: move the left pointer

Why the left value can be discarded: the right array is SORTED, so everything after the current right value is >= it. If the left value is smaller than the current right value, it can never appear later in the right array. Safe to skip forever.

That's the two-pointer invariant (week 4).

## Plus One (LC 66)
Array of digits, most significant first. Add one, return the new digit array.

```python
right = len(digits) - 1
carry = 1
while right >= 0:
    digits[right] += carry
    carry = 0
    if digits[right] == 10:
        carry = 1
    digits[right] %= 10
    if carry == 0:
        return digits
    right -= 1

if carry == 1:
    digits.insert(0, 1)
return digits
```
O(n) time, O(1) extra space.

The three cases:
- [1,2,3] -> [1,2,4]   no carry, returns after one step
- [1,2,9] -> [1,3,0]   one carry
- [9,9,9] -> [1,0,0,0] carry all the way out. THIS is the whole problem.

## Why it walks right to left
A carry flows LEFTWARD. When index 2 overflows, index 1 is affected.

Walking left to right, you'd process index 0 before knowing whether index 1 is going to send it a carry, so you'd have to go back and fix it.

SIGNAL WORTH REMEMBERING: when information flows in one direction, iterate AGAINST that direction. Same reasoning behind several later patterns.

## Why the all-nines case can't be handled inside the loop
After the loop, [9,9,9] has become [0,0,0] with carry still set. There's no index -1 to carry into, so the extra digit has to be prepended AFTER the loop ends.

Condition must be `if carry:`, not `if digits[0] == 0`.

The digits[0] version happens to pass on LeetCode because the constraints ban leading zeros, but it's correct by accident of the input rules rather than by logic. Feed it [0,9] and it breaks. Write the condition that says what you MEAN.

## Cost of the insert
`list.insert(0, x)` is O(n), everything shifts.

Inside the loop that would be O(n) x O(n) = O(n^2).
Outside the loop it runs at most ONCE: O(n) loop + O(n) insert = O(n).

Sequential blocks ADD, nested blocks MULTIPLY (Monday's rule).

## Space nuance for interviews
The insert creates a list of size n+1, but that's the OUTPUT, and output space isn't usually counted.
If pushed: "O(1) auxiliary, O(n) if you count the returned array."