## KOKO Eating Bananas

**Problem Statement:** A monkey is given `n` piles of bananas, whereas the `ith` pile has `a[i]` bananas. An integer `h` is also given, which denotes the time (in hours) for all the bananas to be eaten.

Each hour, the monkey chooses a non-empty pile of bananas and eats `k` bananas. If the pile contains less than `k` bananas, then the monkey consumes all the bananas and won’t eat any more bananas in that hour.

Find the minimum number of bananas `k` to eat per hour so that the monkey can eat all the bananas within `h` hours.

---

### Examples

Example 1:
Input Format: N = 4, a[] = {7, 15, 6, 3}, h = 8
Result: 5
Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.

---

Example 2:
Input Format: N = 5, a[] = {25, 12, 8, 14, 19}, h = 5
Result: 25
Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.

---

Before moving on to the solution, let’s understand how Koko will eat the bananas. Assume, the given array is {3, 6, 7, 11} and the given time i.e. h is 8.

First of all, Koko cannot eat bananas from different piles. He should complete the pile he has chosen and then he can go for another pile.
Now, Koko decides to eat 2 bananas/hour. So, in order to complete the first he will take
3 / 2 = 2 hours. Though mathematically, he should take 1.5 hrs but it is clearly stated in the question that after completing a pile Koko will not consume more bananas in that hour. So, for the first pile, Koko will eat 2 bananas in the first hour and then he will consume 1 banana in another hour.

From here we can conclude that we have to take ceil of (3/2). Similarly, we will calculate the times for other piles.

    1st pile: ceil(3/2) = 2 hrs
    2nd pile: ceil(6/2) = 3 hrs
    3rd pile: ceil(7/2) = 4 hrs
    4th pile: ceil(11/2) = 6 hrs

Koko will take 15 hrs in total to consume all the bananas from all the piles.

---

**Observation**: Upon observation, it becomes evident that the maximum number of bananas (represented by 'k') that Koko can consume in an hour is obtained from the pile that contains the largest quantity of bananas. Therefore, the maximum value of 'k' corresponds to the maximum element present in the given array.

So, our answer i.e. the minimum value of ‘k’ lies between 1 and the maximum element in the array i.e. max(a[]).

---

### Solution :

```cpp
#include <bits/stdc++.h>
using namespace std;

long long calculateTotalHours(vector<int> &v, long long hourly) {
    long long totalH = 0;
    int n = v.size();
    for (int i = 0; i < n; i++) {
        totalH += (v[i] + hourly - 1) / hourly;
    }
    return totalH;
}

long long minimumRateToEatBananas(vector<int> &v, long long h) {
    long long low = 1, high = INT_MAX;

    while (low < high) {
        long long mid = low + (high - low) / 2;
        long long totalH = calculateTotalHours(v, mid);

        if (totalH <= h) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    return low;
}
```

---

### Explanation :

1. `calculateTotalHours` :
   This function calculates the total hours required to eat all the bananas at a given hourly rate. It uses integer division and rounds up to the nearest integer using `(v[i] + hourly - 1) / hourly`.

2. `minimumRateToEatBananas` :
   This function performs a **binary search** to find the minimum hourly rate required to eat all the bananas within h hours. It initializes a `low` rate as 1 and a `high` rate as a large integer.

   The binary search continues until low is less than high, and it updates the `mid` rate within this range.

   It then calculates the total hours required at the mid rate using the calculateTotalHours function. If the total hours are less than or equal to h, it updates high to mid, effectively searching in the lower half of the range; otherwise, it updates low to mid + 1, searching in the upper half.

---

The expression `(v[i] + hourly - 1) / hourly` with an example:

Suppose we have the following values:

    v[i] (the number of bananas to eat) = 12
    hourly (the hourly rate at which we can eat) = 5

Using the expression `(v[i] + hourly - 1) / hourly`:

    (12 + 5 - 1) / 5
    (16) / 5
    3.2

Now, let's break it down:

    12 + 5 - 1 equals 16. This step ensures that we add hourly - 1 to the numerator, which is necessary to ensure rounding up.
    16 / 5 equals 3.2. This is the result of dividing the numerator (16) by the denominator (5).

In this example, the result of `(v[i] + hourly - 1) / hourly` is 3.2. Since we want to round up to the nearest integer (**because you can't eat a fraction of a banana**), this value would be considered as 4 hours required to eat 12 bananas at a rate of 5 bananas per hour.
