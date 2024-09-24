#include <stdio.h>
#include <stdlib.h>

typedef int *array;
#define new_array(n) (array) malloc(sizeof(int) * (n))

#define rep(key, start, end) for (int key = start; key < end; key++)

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

int main()
{
	int N;
	scanf("%d", &N);
	array H = new_array(N);
	int max = 0;

	rep(i, 0, N)
	{
		scanf("%d", &H[i]);
	}

	if (N == 1)
	{
		YES();
	}

	if (N == 2)
	{
		if (H[0] <= H[1])
			YES();
		if (H[0] - H[1] == 1)
			YES();
		NO();
	}

	if (H[0] - H[1] > 1)
		NO();

	max = H[0];
	rep(i, 1, N)
	{
		if (max - H[i] > 1)
			NO();
		if (max < H[i])
			max = H[i];
	}

	YES();
}