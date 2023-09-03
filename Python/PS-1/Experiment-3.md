## Pearson's Correlation coefficient.

### To measure linear relationship between two variables in a dataset.

#### The coefficient lies between -1 to +1, where -1 is negative (unlike) relationship, +1 is a positive (like) relationship and 0 is no relationship between those datasets

```py
## Pearson's Correlation - finding a coefficient with justifies relationship
import numpy as np

## generating random data for two variables.

np.random.seed(42)
dataset1 = np.random.rand(20)
dataset2 = 2 * dataset1 + 1 + 0.1 * np.random.randn(20) # simulating linear relationship with some noise

# calculating Pearson's Correlation coefficient
def pearson_correlation(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    numerator = np.sum((x - mean_x)*(y - mean_y))
    denominator = np.sqrt(np.sum((x - mean_x)**2)* np.sum((y -mean_y)**2))
    correlation_coefficient = numerator / denominator
    return correlation_coefficient

correlation_coefficient = pearson_correlation(dataset1, dataset2)

print("Dataset 1: ", dataset1)
print("Dataset 2: ", dataset2)
print("Pearson's Correlation Coefficient: ", correlation_coefficient)
```

**output :**

```
Dataset 1:  [0.5881308  0.89771373 0.89153073 0.81583748 0.03588959 0.69175758
 0.37868094 0.51851095 0.65795147 0.19385022 0.2723164  0.71860593
 0.78300361 0.85032764 0.77524489 0.03666431 0.11669374 0.7512807
 0.23921822 0.25480601 0.85762553 0.94977903 0.56168686 0.17878052
 0.77025193 0.49238104 0.63125307 0.83949792 0.4610394  0.49794007]
Dataset 2:  [2.28827483 2.92870528 2.75872758 2.61867188 1.06087743 2.53913381
 1.77023972 1.83032702 2.22735362 1.27724249 1.63791944 2.64319567
 2.47251342 2.53935626 2.60319676 0.91821854 1.2663488  2.38890874
 1.44458737 1.54170911 2.65502026 3.05403089 2.18807712 1.41688276
 2.58430632 2.12054098 2.38295726 2.81417546 1.97142252 1.72544362]
Pearson's Correlation Coefficient:  0.9804978183283416
```
