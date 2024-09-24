#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>

bool isend(std::vector<int> v)
{
	int count = 0;
	for (int a : v)
	{
		if (a)
		{
			count++;
		}
	}
	return count < 3 ? true : false;
}

int main()
{
	while (1)
	{
		int size;
		std::cin >> size;
		if (size == 0)
		{
			break;
		}

		std::vector<int> v;
		int temp;
		for (int i = 0; i < size; i++)
		{
			std::cin >> temp;
			v.push_back(temp);
		}

		int count = 0;
		int index = v.size() - 2;

		while (1)
		{
			sort(v.begin(), v.end());

			if (isend(v))
				break;
			int last = v.size() - 1;
			int sertchlast = last - 1;
		}

		std::cout << count << std::endl;
	}
}