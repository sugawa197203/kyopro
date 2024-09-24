#include <stdio.h>

int sumDigitNum(int n)
{
	int sum = 0;
	while (n > 0)
	{
		sum += n % 10;
		n /= 10;
	}
	return sum;
}

int main()
{
	int N;
	scanf("%d", &N);

	int n = sumDigitNum(N);

	puts(N % n == 0 ? "Yes" : "No");
}