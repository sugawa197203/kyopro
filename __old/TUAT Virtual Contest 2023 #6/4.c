#include <stdio.h>
#include <string.h>

int main()
{
	char A[102] = {0}, B[102] = {0};

	scanf("%s", A);
	scanf("%s", B);

	int lenA = strlen(A);
	int lenB = strlen(B);

	if (lenB < lenA)
	{
		puts("GREATER");
		return 0;
	}
	if (lenA < lenB)
	{
		puts("LESS");
		return 0;
	}

	for (int i = 0; i < lenA; i++)
	{
		if (B[i] < A[i])
		{
			puts("GREATER");
			return 0;
		}
		if (A[i] < B[i])
		{
			puts("LESS");
			return 0;
		}
	}

	puts("EQUAL");
}