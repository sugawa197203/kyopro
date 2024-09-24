#include <stdio.h>

int main()
{
	int cost = 700;

	if (fgetc(stdin) == 'o')
		cost += 100;
	if (fgetc(stdin) == 'o')
		cost += 100;
	if (fgetc(stdin) == 'o')
		cost += 100;

	printf("%d", cost);
}