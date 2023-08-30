## Import Statistics and Numpy library:

```py
import statistics as st
import numpy as np
```

## Make a data storage:

```py
data = np.array([1, 2, 3, 4, 5, 6, 6, 7, 8, 9])
```

## Calculate by using Statistics functions:

```py
print("Mean:", st.mean(data))
print("Median:", st.median(data))
print("Mode:", st.mode(data))
print("Range:", max(data) - min(data))
print("Variance:", st.variance(data))
print("STD:", round(st.stdev(data)))
```

## Output:

```
Mean: 5
Median: 5.5
Mode: 6
Range: 8
Variance: 6
STD: 2
```
