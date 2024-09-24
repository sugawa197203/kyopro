#include <stdio.h>
#include <math.h>

int max(int *list, int N)
{
	int max_num = list[0];

	for (int i = 1; i < N; i++)
	{
		if (max_num < list[i])
			max_num = list[i];
	}

	return max_num;
}

int main()
{
	int N;

	scanf("%d", &N);

	int x[100], y[100];
	int length[100][100] = {0};

	for (int i = 0; i < N; i++)
	{
		scanf("%d %d", &x[i], &y[i]);
	}

	for (int i = 0; i < N; i++)
	{
		int _x = x[i];
		int _y = y[i];

		for (int j = 0; j < N; j++)
		{
			int dx = _x - x[j];
			int dy = _y - y[j];

			length[i][j] = dx * dx + dy * dy;
		}
	}

	int buf[100] = {0};

	for (int i = 0; i < N; i++)
	{
		buf[i] = max(&length[i], N);
	}

	printf("%f", sqrt(max(buf, N)));
}