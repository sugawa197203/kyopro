#include <stdio.h>

static char _buf[10000000];
unsigned long c = 0;

int read_int()
{
	int r = 0;
	while (_buf[c] >= '0' && _buf[c] <= '9')
	{
		r = r * 10 + _buf[c++] - '0';
	}
	c++;
	return r;
}

int A[100000000];
int B[100000000];
int i, j;
int sum;
int main()
{
	int n, m, p;
	fread(_buf, 1, sizeof(_buf), stdin);
	long result = 0;
	n = read_int();
	m = read_int();
	p = read_int();

	read_int();
	for (i = 0; i < n; i++)
	{
		A[i] = read_int();
	}
	read_int();
	for (i = 0; i < m; i++)
	{
		B[i] = read_int();
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
		{
			sum = A[i] + B[j];
			if (sum > p)
			{
				result += p;
			}
			else
			{
				result += sum;
			}
		}
	}

	printf("%ld\n", result);
}