import argparse
import re
import json

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", "-v", action="store_true", help="print individual costs")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("file", type=str, help="log file to read", nargs="?")
group.add_argument("--all", action="store_true", help="read all log files")

args = parser.parse_args()

def parse_log(file):
    with open(file, "r") as f:
        lines = f.read().split("\n")
    # split into logging events
    events = []
    linenums = []
    event = []
    linenum = -1
    for i, line in enumerate(lines):
        if "INFO" in line:
            events.append("\n".join(event))
            linenums.append(linenum)
            event = []
            linenum = i+1
        event += [line]
    events.append("\n".join(event))
    linenums.append(linenum)

    # find all events containing a cost
    idxs = []
    for i, event in enumerate(events):
        if "Cost Estimate:" in event:
            idxs.append(i)

    # parse costs
    costs = []
    contexts = []
    for idx in idxs:
        event = events[idx]
        # Cost Estimate: $0.0208
        match = re.search(r"Cost Estimate: \$([0-9.]+)", event)
        assert match is not None
        cost = float(match.group(1))
        costs.append(cost)
        contexts.append(linenums[idx])

    # total cost
    total = sum(costs)

    return total, costs, contexts

if args.file is not None:
    total, costs, contexts = parse_log(args.file)
    print(f"Total: ${total:.4f}")
    if args.verbose:
        for cost, context in sorted(zip(costs, contexts), reverse=True):
            print(f"${cost:.4f} in {args.file}:{context}")

elif args.all:
    import glob
    totals = []
    files = []
    for file in glob.glob("logs/*.log"):
        total, costs, context = parse_log(file)
        totals.append(total)
        files.append(file)
    
    all_total = sum(totals)
    print(f"Total: ${all_total:.4f}")
    if args.verbose:
        for total, file in sorted(zip(totals, files), reverse=True):
            print(f"${total:.4f} {file}")