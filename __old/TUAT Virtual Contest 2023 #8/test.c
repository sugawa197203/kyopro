#define YES()                         \
	do                                \
	{                                 \
		printf("Yes %d\n", __LINE__); \
	} while (0)

int main()
{
	YES();
	YES();
	YES();
}