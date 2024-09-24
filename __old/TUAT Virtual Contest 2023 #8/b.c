#include <stdio.h>
#include <string.h>

#define N 101

#define TO_STRING(x) #x
#define YES TO_STRING(Yes)
#define NO TO_STRING(No)

#define TURE 1
#define FALSE 0

typedef int boolen;

#define rep(i, n) for (int i = 0; i < n; i++)

boolen isRUD(char c)
{
	if (c == 'R' || c == 'U' || c == 'D')
		return TURE;
	return FALSE;
}

boolen isLUD(char c)
{
	if (c == 'L' || c == 'U' || c == 'D')
		return TURE;
	return FALSE;
}

int main()
{
	char S[N] = {0};

	scanf("%s", S);

	int len = strlen(S);

	rep(i, len)
	{
		if (i % 2)
		{
			if (!isLUD(S[i]))
			{
				printf(NO);
				return 0;
			}
		}
		else
		{
			if (!isRUD(S[i]))
			{
				printf(NO);
				return 0;
			}
		}
	}
	printf(YES);
}