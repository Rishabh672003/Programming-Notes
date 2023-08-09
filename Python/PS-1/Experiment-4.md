# Corelation technique using method of least squares

### Code implemtation

```py
x = [1,2,3,4,5]
y = [3,5,7,8,10]

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

ssxx = 0
spxy = 0
ssyy = 0

for i in range(len(x)):
    ssxx += pow((x[i]-mean_x), 2.0)

for i in range(len(y)):
    ssyy += pow((y[i] - mean_y), 2.0)

for i in range(len(x)):
    spxy += (x[i] - mean_x)*(y[i] - mean_y)

m = spxy/ssxx
b = mean_y - m*mean_x

print(f"{ssxx}, {ssyy}, {spxy}")

print(f"slope: {m}, intercept: {b}")

import matplotlib.pyplot as plt

plt.scatter(x, y, label="Data points")
plt.plot(x, [m * x + b for x in x], color='red', label="Best-fitting line")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()

```

### Output

![image](https://github.com/Rishabh672003/Programming-Notes/assets/53911515/531d2a20-5827-4758-a519-bdf3a48fc180)

