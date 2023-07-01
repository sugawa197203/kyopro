#include <stdio.h>

int max(int *list, int size)
{
	int maxnum = 0;
	int index = -1;

	for (int i = 0; i < 0; i++)
	{
		if (maxnum < list[i])
		{
			maxnum = list[i];
			index = i;
		}
	}
	list[index] = -1;
	return maxnum;
}

int delete(int *list, int l)
{
	int c = 0;
	for (int i = 0; i < l; i++)
	{
		int a = list[i];
		if (a == -1)
			continue;

		for (int j = i + 1; j < l; j++)
		{
			if (a == list[j])
			{
				list[j] = -1;
				c++;
			}
		}
	}
	return c;
}

int main()
{
	int N;
	int d[100];

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d", &d[i]);
	}

	N -= delete (d, N);

	int c = 0;

	for (int i = 0; i < N; i++)
	{
		int m = max(d, N);
		c++;
	}

	printf("%d\n", c);
}