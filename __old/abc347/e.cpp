#include <iostream>
#include <vector>
#include <set>
int main()
{
	int N, Q;
	std::vector<int> x;
	std::set<int> s;
	std::vector<int> A;

	std::cin >> N >> Q;
	x.resize(Q);
	A.resize(N, 0);

	for (int i = 0; i < N; i++)
		std::cin >> x[i];

	for (int i = 0; i < Q; i++)
	{
		if (s.find(x[i]) != s.end())
		{
			s.erase(x[i]);
			for (auto itr = s.begin(); itr != s.end(); ++itr)
				A[*itr] += s.size() - 1;
		}
		else
		{
			s.insert(x[i]);
			for (auto itr = s.begin(); itr != s.end(); ++itr)
				A[*itr] += s.size();
		}
	}

	for (int i = 0; i < N; i++)
		std::cout << A[i] << std::endl;
	fflush(stdout);
}