#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);

	char c;
	fgetc(stdin);

	while ((c = fgetc(stdin)) != EOF)
	{
		if (c == '\n')
			break;
		(c + N) > 'Z' ? putc((c + N) - ('Z' - 'A') - 1, stdout) : putc((c + N), stdout);
	}
}