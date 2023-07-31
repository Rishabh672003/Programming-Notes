- For one’s complement, we simply need to flip all bits.
- For 2’s complement, we first find one’s complement. We traverse the one’s complement starting from LSB (least significant bit), and look for 0.
- We flip all 1’s (change to 0) until we find a 0. Finally, we flip the found 0.
- For example, 2’s complement of “01000” is “11000” (Note that we first find one’s complement of 01000 as 10111).
- If there are all 1’s (in one’s complement), we add an extra 1 in the string. For example, 2’s complement of “000” is “1000” (1’s complement of “000” is “111”).


```cpp
// C++ program to print 1's and 2's complement of
// a binary number
#include <bits/stdc++.h>
using namespace std;

// Returns '0' for '1' and '1' for '0'
char flip(char c) {return (c == '0')? '1': '0';}

// Print 1's and 2's complement of binary number
// represented by "bin"
void printOneAndTwosComplement(string bin)
{
	int n = bin.length();
	int i;

	string ones, twos;
	ones = twos = "";

	// for ones complement flip every bit
	for (i = 0; i < n; i++)
		ones += flip(bin[i]);

	// for two's complement go from right to left in
	// ones complement and if we get 1 make, we make
	// them 0 and keep going left when we get first
	// 0, make that 1 and go out of loop
	twos = ones;
	for (i = n - 1; i >= 0; i--)
	{
		if (ones[i] == '1')
			twos[i] = '0';
		else
		{
			twos[i] = '1';
			break;
		}
	}

	// If No break : all are 1 as in 111 or 11111;
	// in such case, add extra 1 at beginning
	if (i == -1)
		twos = '1' + twos;


	cout << "1's complement: " << ones << endl;
	cout << "2's complement: " << twos << endl;
}

// Driver program
int main()
{
	string bin = "1100";
	printOneAndTwosComplement(bin);
	return 0;
}

```
