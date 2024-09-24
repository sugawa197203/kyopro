#include <stdio.h>

int main()
{
	int A, P;

	scanf("%d %d", &A, &P);

	int peace = A * 3 + P;

	printf("%d\n", peace / 2);
}