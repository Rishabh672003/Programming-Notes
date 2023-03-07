// search algorithm example
#include <algorithm> // search
#include <iostream>  // cout
#include <vector>    // vector

using namespace std;

bool mypredicate(int i, int j) { return (i == j); }

int main() {
    vector<int> haystack;

    // set some values:        haystack: 10 20 30 40 50 60 70 80 90
    for (int i = 1; i < 10; i++)
        haystack.push_back(i * 10);

    // using default comparison:
    int needle1[] = {40, 50, 60, 70};
    vector<int>::iterator it;
    it = search(haystack.begin(), haystack.end(), needle1, needle1 + 4);

    if (it != haystack.end())
        cout << "needle1 found at position " << (it - haystack.begin()) << '\n';
    else
        cout << "needle1 not found\n";

    // using predicate comparison:
    int needle2[] = {20, 30, 50};
    it = search(haystack.begin(), haystack.end(), needle2, needle2 + 3,
                mypredicate);

    if (it != haystack.end())
        cout << "needle2 found at position " << (it - haystack.begin()) << '\n';
    else
        cout << "needle2 not found\n";

    return 0;
}
