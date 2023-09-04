## Find Number of Occurrence : Integers

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }

    // precompute
    int hash[n + 1] = {0};
    for(int i = 0; i < n; i++){
        // go to the index of hash array and do a +1
        hash[arr[i]]++;
    }

    //fetch
    int num; cin >> num;

    cout << hash[num] << endl;

    return 0;
}
```

```
output :
5  --> size of array
1 1 2 2 3  --> array elements
2  --> target element
2  --> number of it's occurrence
```

---

### A short explanation :

- We create an array `arr` of size `n`, and take input of the elements.

- The Precomputation is done by creating an hash array with size `n + 1`.

- `n + 1` because the hash array will keep count of **ith** element of `arr` at **i+1th** index in hash array.

- **Example** : if `arr[i] = 1`, then `hash[1]` will be incremented by 1 and so on.

---

## Find Number of Occurrence : Characters (LowerCase)

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s; cin >> s;

    // precompute
    int hash[26] = {0};
    for (int i = 0; i < s.size(); i++){
        hash[s[i] - 'a']++;
    }

    // fetch
    char c; cin >> c;

    cout << hash[c - 'a'] << endl;

    return 0;
}
```

---

### A short explanation :

- We create an string `s`, and take it's input.

- The Precomputation begins by creating an hash array with size 26. (index 0 to 25)

- Then we keep incrementing the count of every `s[i] - 'a'` in hash array.

- As we know that `s[i]` is a character and **ASCII** value of a is 97, hence we subtract the current character with 'a' to get an integer **ASCII** value equivalent to it's positon in hash array.

- **Example** : if s`[i] = 'c'`, then `'c' - 'a' = 99 - 97 = 2`, which then refers it's index (position) in hash array. (0 based indexing).

- While printing output, `hash[c - 'a']` refers to the index value which comes after subtracting character `c - 'a'`.

- **Example** : If `c = 'd'`, then `hash['d' - 'a'] == hash[100 - 97] == hash[3]`, which is the place where count of `'d'` is stored.

---

### Tags :

`#hashing` `#find-occurrence`
