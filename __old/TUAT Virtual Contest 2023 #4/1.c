#include <stdio.h>

int main()
{
	int M, H;
	scanf("%d %d", &M, &H);

	printf(H % M == 0 ? "Yes" : "No");
}