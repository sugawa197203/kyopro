#include <stdio.h>
#include <stdlib.h>
#include <string>

int main()
{
	int N;
	scanf("%d", &N);
	int **L;
	int Li[100000];
	L = malloc(4 * N);

	for (int i = 0; i < N; i++)
	{
		int buf;
		scanf("%d ", &buf);
		Li[i] = buf;

		int *l = malloc(4 * buf);
		L[i] = l;

		for (int j = 0; j < buf; j++)
		{
			scanf("%d ", &L[i][j]);
		}
	}

	char noSameFlag[10000];
	int count = 0;

	for (int i = 0; i < N; i++)
	{
		memset(noSameFlag, 0, 10000);
		memset(noSameFlag, 1, i);
		for (int j = i; j < N; j++)
		{
			if (Li[i] != Li[j])
			{
				noSameFlag[j] = 1;
			}
		}

		for (int j = 0; j < Li[i]; j++)
		{
			for (int k = 0; k < Li[i]; k++)
			{

				if (noSameFlag[k])
					continue;

				if (L[i][j] != L[k][j])
				{
					noSameFlag[k] = 1;
				}
			}
		}

		for (int j = 0; j < Li[i]; j++)
		{
			if (!noSameFlag[j])
				count++;
		}
	}
}