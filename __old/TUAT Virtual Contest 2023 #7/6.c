#include <stdio.h>

int main()
{
	int alphabet[26] = {0};

	char c;

	while ((c = getchar()) != '\n')
	{
		alphabet[c - 'a']++;
	}

	for (int i = 0; i < 26; i++)
	{
		if (alphabet[i] % 2)
		{
			puts("No");
			return 0;
		}
	}

	puts("Yes");
	return 0;
}