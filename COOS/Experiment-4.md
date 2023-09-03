```cpp
#include <iostream>
using namespace std;

int flipFlops[4];

void initializeFlipFlops() {
  cout << "Enter a 4 bit value: ";
  for (int i = 0; i < 4; i++) {
    cin >> flipFlops[i];
  }
}

void leftShift() {
  // Shift the bits to the left
  cout << "After left shift, ";
  for (int i = 3; i > 0; i--) {
    flipFlops[i] = flipFlops[i - 1];
  }
// Set the least significant bit to 0
  flipFlops[0] = 0;
}

void rightShift() {
// Shift the bits to the right
  cout << "After right shift, ";
  int temp = flipFlops[0];
  for (int i = 0; i < 3; i++) {
    flipFlops[i] = flipFlops[i + 1];
  }
  // Set the most significant bit to 0
  flipFlops[3] = temp;
}

// Function to print the contents of the register
void printRegister() {
    cout << "Register stores: ";
  for (int i = 3; i >= 0; i--) {
    cout << flipFlops[i];
  }
  cout << endl;
}

int main() {
  initializeFlipFlops();

  printRegister();

  leftShift();

  printRegister();

  rightShift();

  printRegister();

  return 0;
}

```
