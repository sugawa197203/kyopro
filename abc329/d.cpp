#include <iostream>
#include <vector>
#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
class Hyo
{
	int v;
	int id;

public:
	void setid(int id)
	{
		this->id = id;
	}

	int getV()
	{
		return this->v;
	}

	int getId()
	{
		return this->id;
	}

	void add()
	{
		this->v++;
	}
};

int compareId(const void *a, const void *b)
{
	Hyo **_A = (Hyo **)a;
	Hyo **_B = (Hyo **)b;
	Hyo *A = *_A;
	Hyo *B = *_B;

	if (A->getId() < B->getId())
	{
		return -1;
	}
	else if (A->getId() > B->getId())
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int compareV(const void *a, const void *b)
{
	Hyo **_A = (Hyo **)a;
	Hyo **_B = (Hyo **)b;
	Hyo *A = *_A;
	Hyo *B = *_B;

	if (A->getV() > B->getV())
	{
		return -1;
	}
	else if (A->getV() < B->getV())
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int main()
{
	// N M
	// A:list
	int N, M;
	cin >> N >> M;
	vector<int> A(M);
	rep(i, M) cin >> A[i];

	Hyo *tohyo = new Hyo[N];
	Hyo **sorter = new Hyo *[N];
	for (int i = 0; i < N; i++)
	{
		sorter[i] = &tohyo[i];
	}

	for (int i = 1; i <= N; i++)
	{
		tohyo[i].setid(i);
	}

	for (int i = 0; i < M; i++)
	{
		tohyo[A[i] - 1].add();
		qsort(sorter, N, sizeof(Hyo), compareId);
		qsort(sorter, N, sizeof(Hyo), compareV);

		// for (int i = 0; i < N; i++)
		// {
		// 	cout << (*sorter[i]).getV();
		// 	cout << (*sorter[i]).getId() + 1;
		// 	cout << endl;
		// }
		cout << (*sorter[0]).getId() + 1 << endl;
	}
}