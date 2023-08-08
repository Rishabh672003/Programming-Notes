# Program to do binary addition and octal addition

### For binary addition

```cpp
#include <iostream>
#include <string>
using namespace std;

string addBinary(string a, string b) {
    int carry = 0;
    string result = "";

    // Make sure the binary numbers have the same length by padding zeros
    int maxLength = max(a.length(), b.length());
    a = string(maxLength - a.length(), '0') + a;
    b = string(maxLength - b.length(), '0') + b;

    // Iterate through the binary numbers from right to left
    for (int i = maxLength - 1; i >= 0; i--) {
        int bit1 = a[i] - '0';
        int bit2 = b[i] - '0';

        // Calculate the sum and carry
        int currentSum = bit1 + bit2 + carry;
        int currentBit = currentSum % 2;
        carry = currentSum / 2;

        // Add the current bit to the result
        result = to_string(currentBit) + result;
    }

    // If there is a carry left after the iteration, add it to the result
    if (carry) {
        result = "1" + result;
    }

    return result;
}

int main() {
    string num1 = "101";
    string num2 = "011";
    string result = addBinary(num1, num2);
    cout << "The sum of " << num1 << " and " << num2 << " is: " << result << endl;

    return 0;
}
```


### For octal to binary 

```cpp
#include <iostream>
#include <string>

using namespace std;

// Function to add two octal numbers
string addOctal(string num1, string num2) {
    // Convert the octal numbers to decimal
    int decimal1 = stoi(num1, nullptr, 8);
    int decimal2 = stoi(num2, nullptr, 8);

    // Add the decimal numbers
    int sum = decimal1 + decimal2;

    // Convert the sum back to octal
    string octalSum = to_string(sum);
    return "0" + octalSum;
}

int main() {
    string octal1 = "17"; // Octal number 17
    string octal2 = "43"; // Octal number 43

    string result = addOctal(octal1, octal2);

    cout << "Sum: " << result << endl;

    return 0;
}
```