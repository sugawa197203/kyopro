#include <stdio.h>
#include <errno.h>
#include <string.h>

int main()
{
	puts("abcdefg");
	perror("perror");
	FILE *f = fopen("unknow.txt", "r");

	if (f == NULL)
	{
		perror("f == NULL");
		perror(strerror(errno));
		return -1;
	}

	return 0;
}
