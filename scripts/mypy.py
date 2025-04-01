import datetime
import random
import sys

def main():
    results = f"""Script Execution Report
--------------------------------
Timestamp: {datetime.datetime.now()}
Random ID: {random.randint(1000, 9999)}
Status: Success
"""
    print(results)
    return results

if __name__ == "__main__":
    with open("scripts/output.txt", "w") as f:
        f.write(main())
