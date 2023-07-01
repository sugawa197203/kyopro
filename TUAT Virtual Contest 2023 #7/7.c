#include <stdio.h>

int main()
{
	int H, W;
	scanf("%d %d", &H, &W);

	char S[51][51] = {0};

	for (int i = 0; i < H; i++)
	{
		scanf("%s", S[i]);
	}

	for (int i = 0; i < H; i++)
	{
		for (int j = 0; j < W; j++)
		{
			if (S[i][j] == '.')
			{
				int count = 0;
				for (int k = -1; k <= 1; k++)
				{
					for (int l = -1; l <= 1; l++)
					{
						if (i + k >= 0 && i + k < H && j + l >= 0 && j + l < W)
						{
							if (S[i + k][j + l] == '#')
							{
								count++;
							}
						}
					}
				}
				S[i][j] = count + '0';
			}
		}
	}

	for (int i = 0; i < H; i++)
	{
		printf("%s\n", S[i]);
	}
}