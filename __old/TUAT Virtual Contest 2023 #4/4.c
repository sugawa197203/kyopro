#include <stdio.h>
#include <math.h>
int main()
{
	int A1, A2, A3;
	scanf("%d %d %d", &A1, &A2, &A3);

	int task2 = abs(A2 - A1);
	int task3 = abs(A3 - A1);

	int task23 = task2 + abs(A3 - A2);
	int task32 = task3 + abs(A2 - A3);

	if (task23 < task32)
	{
		printf("%d", task23);
	}
	else
	{
		printf("%d", task32);
	}
}