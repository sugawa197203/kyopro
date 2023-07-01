#include <stdio.h>
#include <string.h>

int main()
{
	char S[11];
	char T[11];
	char U[11];

	int A, B;

	scanf("%s %s", S, T);
	scanf("%d %d", &A, &B);
	scanf("%s", U);

	if (strcmp(S, U) == 0)
	{
		A--;
	}
	else if (strcmp(T, U) == 0)
	{
		B--;
	}

	printf("%d %d", A, B);
}