# Row Optimizer

A small Python tool that works out the fewest truck rows needed to load a mix of large and small window racks, while fitting as many parts as possible.

## Background

Built while working at Skyjack Inc. (Linamar) in Guelph, ON as a trailer-packing tool for loading mixed large and small window racks. It was presented to upper management.

## How it works

Each row holds a total size of 5. A large rack counts as 2 (`x`) and a small rack counts as 1 (`y`). Rows are built from these patterns:

| Pattern | Contents | Sum |
|---|---|---|
| A | 5y | 5 |
| B | 1x + 3y | 5 |
| C | 2x + 1y | 5 |
| D | 2x | 4 (fallback) |

Pattern D is a last resort. It is used at most once, only when nothing else fits.

The program tries every combination of patterns and picks the one that:

1. Leaves the fewest items unloaded
2. Uses the fewest rows
3. Avoids the fallback row where possible

## Usage

```
python3 row_optimizer.py
```

Enter the number of large racks (x) and small racks (y) when prompted.

## Example

Input: 3 x's, 5 y's

```
Total rows: 2

  Row 1: 2x + 1y  (sum 5)
  Row 2: 1x + 3y  (sum 5)

  Leftover (not enough to form a full row): 0 x's, 1 y's
```

## Requirements

Python 3, no external libraries.
