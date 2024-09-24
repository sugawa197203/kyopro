#include <stdio.h>
#define BUFSIZE 11

#define AC() printf("AC")
#define WA() printf("WA")

#define rep(key, start, end) for (int key = start; key < end; key++)

int main()
{
	char S[BUFSIZE] = {0};

	scanf("%s", S);

	int len = strlen(S);

	if (S[0] != 'A')
	{
		WA();
		return 0;
	}

	int Ccount = 0;
	rep(i, 2, len - 1)
	{
		if (S[i] == 'C')
		{
			Ccount++;
		}
	}

	if (Ccount != 1)
	{
		WA();
		return 0;
	}

	rep(i, 1, len)
	{
		if (S[i] == 'C')
			continue;
		if (S[i] < 'a' || 'z' < S[i])
		{
			WA();
			return 0;
		}
	}

	AC();
}