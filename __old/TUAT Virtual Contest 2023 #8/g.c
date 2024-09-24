#include <stdio.h>

#define SIZE 400001
#define CENTER 200000

int main()
{
	int N;
	int a[CENTER];
	int b[SIZE];
	int end = CENTER;
	int start = CENTER;

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &a[i]);
	}

	char reflag = N % 2;

	for (int i = 0; i < N; i++)
	{
		if (i % 2)
		{
			b[end++] = a[i];
		}
		else
		{
			b[--start] = a[i];
		}
	}

	if (reflag)
	{
		for (int i = start; i < end; i++)
		{
			printf("%d ", b[i]);
		}
	}
	else
	{
		for (int i = end - 1; i >= start; i--)
		{
			printf("%d ", b[i]);
		}
	}
}