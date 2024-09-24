#include <stdio.h>
#include <string.h>

int hasACGT(char *S, int len)
{
	for (int i = 0; i < len; i++)
	{
		if (S[i] != 'A' && S[i] != 'C' && S[i] != 'G' && S[i] != 'T')
		{
			return 0;
		}
	}
	return 1;
}

int main()
{
	char S[11] = {0};

	scanf("%s", S);
	int len = strlen(S);

	for (int i = len; i >= 1; i--)
	{
		for (int j = 0; j <= len - i; j++)
		{
			if (hasACGT(S + j, i))
			{
				printf("%d\n", i);
				return 0;
			}
		}
	}

	puts("0");
}