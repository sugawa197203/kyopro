#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
void print(std::vector<double> const &input)
{
	for (int i = 0; i < input.size(); i++)
	{
		std::cout << input.at(i) << ' ';
	}
}
int main()
{
	std::vector<int> D, E;
	int d, e;

	while (std::cin >> d >> e)
	{
		D.push_back(d);
		E.push_back(e);
	}
	int l = D.size();

	for (int i = 0; i < l; i++)
	{
		int D_i = D[i];
		int E_i = E[i];
		if (D_i == 0 && E_i == 0)
		{
			return 0;
		}

		std::vector<double> cost;

		double harfX = (double)(D_i / 2.0);
		double harfY = (double)(D_i - harfX);

		for (int j = 0; j <= harfX; j++)
		{
			double x = (double)j;
			double y = (double)(D_i - j);

			cost.push_back(abs(sqrt(x * x + y * y) - (double)E_i));
		}

		std::cout << *min_element(cost.begin(), cost.end()) << std::endl;
	}
}