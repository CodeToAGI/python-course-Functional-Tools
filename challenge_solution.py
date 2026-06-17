from functools import reduce
from operator import add

# ==================== YOUR CHALLENGE SOLUTION ====================

sales = [
    {"name": "Alice", "amount": 120, "region": "North"},
    {"name": "Bob", "amount": 85, "region": "South"},
    {"name": "Charlie", "amount": 250, "region": "North"},
    {"name": "Diana", "amount": 95, "region": "East"},
    {"name": "Eve", "amount": 180, "region": "North"},
]

# Step-by-step zero for-loop pipeline
valid_sales = filter(lambda r: r["amount"] >= 100, sales)

bonused = map(lambda r: {**r, "amount": r["amount"] * 1.1}, valid_sales)

ranked = sorted(bonused, key=lambda r: r["amount"], reverse=True)

leaderboard = list(enumerate(ranked, start=1))

grand_total = reduce(add, (r["amount"] for _, r in leaderboard), 0)

# Results
print("🏆 Leaderboard:")
for rank, sale in leaderboard:
    print(f"#{rank} {sale['name']:8} → ${sale['amount']:,.0f} ({sale['region']})")

print(f"\n💰 Grand Total (with bonus): ${grand_total:,.0f}")
