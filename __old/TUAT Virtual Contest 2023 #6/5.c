#include <stdio.h>

int main()
{
	char w[101] = {0};

	int c[26] = {0};

	scanf("%s", w);

	for (int i = 0; i < 100; i++)
	{
		c[w[i] - 'a']++;
	}

	for (int i = 0; i < 26; i++)
	{
		if (c[i] % 2)
		{
			puts("No");
			return 0;
		}
	}

	puts("Yes");
	return 0;
}