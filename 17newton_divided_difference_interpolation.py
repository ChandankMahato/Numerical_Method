
def proterm(i, value, x):
	pro = 1;
	for j in range(i):
		pro = pro * (value - x[j]);
	return pro;

def dividedDiffTable(x, y, n):

	for i in range(1, n):
		for j in range(n - i):
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
									(x[j] - x[i + j]));
	return y;

def applyFormula(value, x, y, n):

	sum = y[0][0];

	for i in range(1, n):
		sum = sum + (proterm(i, value, x) * y[0][i]);
	
	return sum;

def printDiffTable(y, n):

	for i in range(n):
		for j in range(n - i):
			print(round(y[i][j], 4), "\t",
							end = " ");

		print("");

n = 4;
y = [[0 for i in range(10)]
		for j in range(10)];
x = [ 5, 6, 9, 11 ];

y[0][0] = 12;
y[1][0] = 13;
y[2][0] = 14;
y[3][0] = 16;


y=dividedDiffTable(x, y, n);

printDiffTable(y, n);

value = 7;

print("\nValue at", value, "is",
		round(applyFormula(value, x, y, n), 2))

