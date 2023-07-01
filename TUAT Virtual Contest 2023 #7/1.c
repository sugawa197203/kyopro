#include <stdio.h>

int main()
{
	char alphabet[26] = {0};

	for (int i = 0; i < 3; i++)
	{
		char c = getchar();
		alphabet[c - 'a']++;
	}

	for (int i = 0; i < 26; i++)
	{
		if (alphabet[i] == 1)
		{
			putchar(i + 'a');
			return 0;
		}
	}
	puts("-1");
}