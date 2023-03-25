// find example
#include <algorithm> // find
#include <iostream>  // cout
#include <vector>    // vector

using namespace std;

int main() {
    // using find with array and pointer:
    int myints[] = {10, 20, 30, 40};

    // using find with vector and iterator:
    vector<int> myvector(myints, myints + 4);
    vector<int>::iterator it;

    it = find(myvector.begin(), myvector.end(), 30);
    if (it != myvector.end())
        cout << "Element found in myvector: " << *it << '\n';
    else
        cout << "Element not found in myvector\n";

    return 0;
}
