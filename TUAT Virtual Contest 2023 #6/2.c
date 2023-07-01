#include <stdio.h>
#include <stdlib.h>

int cmp(const int *a, const int *b)
{
	return *a < *b ? 1 : *a > *b ? -1
								 : 0;
}

int main()
{
	int N;
	int a[100];

	int Alice = 0, Bob = 0;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &a[i]);
	}

	qsort(a, N, sizeof(int), cmp);

	for (int i = 0; i < N; i++)
	{
		if (i % 2)
		{
			Bob += a[i];
		}
		else
		{
			Alice += a[i];
		}
	}

	printf("%d", Alice - Bob);
}