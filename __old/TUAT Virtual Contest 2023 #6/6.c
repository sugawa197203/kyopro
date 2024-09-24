#include <stdio.h>
#include <math.h>

int main()
{
	int N;
	int t, x, y;
	int _t = 0, _x = 0, _y = 0;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d %d %d", &t, &x, &y);
		int manhattan = abs(x - _x) + abs(y - _y);
		int time = t - _t;

		if (manhattan > time)
		{
			puts("No");
			return 0;
		}

		if ((time - manhattan) % 2)
		{
			puts("No");
			return 0;
		}

		_t = t;
		_x = x;
		_y = y;
	}

	puts("Yes");
}