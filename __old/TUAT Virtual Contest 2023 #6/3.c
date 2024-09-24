#include <stdio.h>

int main()
{
	int N, A, B;
	int count = 0;

	scanf("%d %d %d", &N, &A, &B);

	for (int n = N; 0 < n; n--)
	{
		int c = 0;
		int _n = n;
		while (0 < _n)
		{
			c += _n % 10;
			_n /= 10;
		}
		if (A <= c && c <= B)
			count += n;
	}

	printf("%d", count);
}