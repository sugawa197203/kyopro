#include <stdio.h>
#include <math.h>

#define NIJO(x) (x * x)

int main()
{
	int N;
	scanf("%d", &N);

	int sq = sqrt(N);

	printf("%d\n", NIJO(sq));
}