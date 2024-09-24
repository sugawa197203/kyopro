#include <iostream>

int main()
{
	std::cout << (1 && 1) << std::endl;
	std::cout << (0 && 1) << std::endl;
	std::cout << (1 && 2) << std::endl;
	std::cout << (1 && -2) << std::endl;
}