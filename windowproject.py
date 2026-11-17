"""
Row Optimizer
-------------
Given a count of x's and y's, figures out how to split them into rows
that sum to 5 (preferred) using these patterns:

    A: 0x + 5y   = 5   (all y's)
    B: 1x + 3y   = 5
    C: 2x + 1y   = 5
    D: 2x + 0y   = 4   (rare fallback — used AT MOST ONCE, only when
                         nothing else fits at the very end)

Places as many of the x's and y's into rows as possible (minimizing
leftover items first — you want everything used), and among the
options that achieve that, picks the one with the FEWEST rows, using
the rare fallback row only as a last resort.
"""


def solve_rows(x_count, y_count):
    best = None  # (leftover_items, total_rows, fallback, n2, n1, n0, x_left, y_left)

    max_n2 = x_count // 2
    for n2 in range(max_n2 + 1):           # C-rows: 2x + 1y
        rem_x = x_count - 2 * n2
        for n1 in range(rem_x + 1):        # B-rows: 1x + 3y
            x_used = 2 * n2 + n1
            y_needed = n2 * 1 + n1 * 3
            if y_needed > y_count:
                continue
            y_rem = y_count - y_needed
            n0 = y_rem // 5                # A-rows: 5y
            y_left = y_rem % 5

            x_left_after = x_count - x_used
            fallback = 1 if x_left_after >= 2 else 0   # D-row: 2x (rare, at most ONE)
            x_left = x_left_after - 2 * fallback

            total = n2 + n1 + n0 + fallback
            leftover_items = x_left + y_left
            candidate = (leftover_items, total, fallback, n2, n1, n0, x_left, y_left)

            if best is None or candidate < best:
                best = candidate

    _, total, fallback, n2, n1, n0, x_left, y_left = best
    return {
        "rows_2x_1y": n2,
        "rows_1x_3y": n1,
        "rows_5y": n0,
        "rows_fallback_2x": fallback,
        "total_rows": total,
        "leftover_x": x_left,
        "leftover_y": y_left,
    }


def print_breakdown(x_count, y_count, result):
    print(f"\nInput: {x_count} x's, {y_count} y's")
    print(f"Total rows: {result['total_rows']}\n")

    row_num = 1
    for _ in range(result["rows_2x_1y"]):
        print(f"  Row {row_num}: 2x + 1y  (sum 5)")
        row_num += 1
    for _ in range(result["rows_1x_3y"]):
        print(f"  Row {row_num}: 1x + 3y  (sum 5)")
        row_num += 1
    for _ in range(result["rows_5y"]):
        print(f"  Row {row_num}: 0x + 5y  (sum 5)")
        row_num += 1
    for _ in range(result["rows_fallback_2x"]):
        print(f"  Row {row_num}: 2x + 0y  (sum 4, rare fallback)")
        row_num += 1

    if result["leftover_x"] or result["leftover_y"]:
        print(f"\n  Leftover (not enough to form a full row): "
              f"{result['leftover_x']} x's, {result['leftover_y']} y's")
    else:
        print("\n  No leftovers — everything fit perfectly.")


def main():
    print("=== Row Optimizer ===")
    try:
        x_count = int(input("Enter number of x's: ").strip())
        y_count = int(input("Enter number of y's: ").strip())
    except ValueError:
        print("Please enter valid whole numbers.")
        return

    if x_count < 0 or y_count < 0:
        print("Counts can't be negative.")
        return

    result = solve_rows(x_count, y_count)
    print_breakdown(x_count, y_count, result)


if __name__ == "__main__":
    main()