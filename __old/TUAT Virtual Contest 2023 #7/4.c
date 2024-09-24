#include <stdio.h>

int main()
{
	int A, B, C, X;
	scanf("%d", &A);
	scanf("%d", &B);
	scanf("%d", &C);
	scanf("%d", &X);

	int count = 0;
	for (int a = 0; a <= A; a++)
	{
		for (int b = 0; b <= B; b++)
		{
			for (int c = 0; c <= C; c++)
			{
				if (500 * a + 100 * b + 50 * c == X)
				{
					count++;
				}
			}
		}
	}

	printf("%d\n", count);
}