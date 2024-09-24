#include <stdio.h>

#define inputInt(x) scanf("%d", &x)
#define inputStr(x) scanf("%s", x)

#define rep(key, start, end) for (int key = start; key < end; key++)

typedef int bool;

#define YES()          \
	do                 \
	{                  \
		printf("Yes"); \
		return 0;      \
	} while (0)

#define NO()          \
	do                \
	{                 \
		printf("No"); \
		return 0;     \
	} while (0)

#define SIZE 200000

int main()
{
	int N;
	inputInt(N);

	int x[SIZE], y[SIZE];
	int _x, _y;

	char S[SIZE] = {0};

	bool Lflags[SIZE] = {-1};
	bool Rflags[SIZE] = {-1};

	rep(i, 0, N)
	{

		scanf("%d %d", &_x, &_y);
		x[i] = _x;
		y[i] = _y;
	}

	inputStr(S);

	rep(i, 0, N)
	{
		if (S[i] == 'L')
		{
			if (y[x[i]] == 0)
			{
				NO();
			}
		}
		else
		{
			Rflags[i] = 1;
		}
	}
}