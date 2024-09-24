#include <iostream>
#include <vector>

int main()
{
	int N, D;
	std::string S;
	std::cin >> N >> D;
	S.resize(N);
	std::cin >> S;

	if (N == D)
	{
		std::cout << atoi(S.c_str()) << std::endl;
		return 0;
	}
	if (S[0] == '0')
	{
		for (int i = 0; i < D - N; i++)
		{
			std::cout << 1;
		}
		std::cout << S << std::endl;
		return 0;
	}
	if (S[0] == '1')
	{
		for (int i = 0; i < D - N; i++)
		{
			std::cout << 1;
		}
		std::cout << S << std::endl;
		return 0;
	}
	std::cout << S;
	for (int i = 0; i < D - N; i++)
	{
		std::cout << 1;
	}
	return 0;
}