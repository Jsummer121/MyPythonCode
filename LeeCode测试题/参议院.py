# -*- coding: utf-8 -*-

senate = "DRRDRDRDRDDRDRDR"
senate = list(senate)
n = len(senate)
while "D" in senate and "R" in senate:
    for i in range(n):
        if senate[i] == "0":
            continue
        elif senate[i] == "R":
            if "D" in senate:
                if "D" in senate[i:]:
                    senate[senate.index("D", i, n)] = "0"
                else:
                    senate[senate.index("D")] = "0"
            else:
                break
        else:
            if "R" in senate:
                if "R" in senate[i:]:
                    senate[senate.index("R", i, n)] = "0"
                else:
                    senate[senate.index("R")] = "0"
            else:
                break

if "R" in senate:
    print("R")
else:
    print("D")