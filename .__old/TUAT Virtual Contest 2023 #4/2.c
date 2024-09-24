#include <stdio.h>

int main()
{
	char n[3];

	scanf("%s", n);

	for (int i = 0; i < 3; i++)
	{
		if (n[i] == '1')
			printf("9");
		else if (n[i] == '9')
			printf("1");
		else
			printf(n[i]);
	}
}