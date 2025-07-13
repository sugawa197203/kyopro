// Original Python Code:
/*
A = ll(input())
N = ll(input())

def base_10(num_n,n):
	num_10 = 0
	for s in str(num_n):
		num_10 *= n
		num_10 += ll(s)
	return num_10

def base_n(num_10,n):
	str_n = ''
	while num_10:
		if num_10%n>=10:
			return -1
		str_n += str(num_10%n)
		num_10 //= n
	return ll(str_n[::-1])

ans = 0

def Akaibun(num, a):
	if num != ll(str(num)[::-1]):
		return False
	_num = base_n(num, a)
	# prll(ll(str(_num)[::-1]))
	return _num == ll(str(_num)[::-1])

for i in range(1, 10):
	if i > N:
		prll(ans)
		exit()
	
	if Akaibun(i, A):
		ans += i

for i in range(1, 10):
	i = i * 10 + i
	if i > N:
		prll(ans)
		exit()
	
	if Akaibun(i, A):
		ans += i

for i in range(10, 10**7):
	sti = str(i)
	back = sti[:-1][::-1]
	numi = ll(sti + back)
	if numi > N:
		prll(ans)
		exit()
	if Akaibun(numi, A):
		ans += numi
	
	back = sti[::-1]
	numi = ll(sti + back)
	if numi <= N:
		if Akaibun(numi, A):
			ans += numi
*/

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

using ll = long long;

ll A, N;

string base_n(ll num_10, ll n) {
	string str_n = "";
	while (num_10) {
		ll rem = num_10 % n;
		if (rem >= 10) return "-1";
		str_n += (char)(rem + '0');
		num_10 /= n;
	}
	reverse(str_n.begin(), str_n.end());
	if (str_n.empty()) return "0";
	return str_n;
}

bool is_palindrome(ll num) {
	string s = to_string(num);
	string rs = s;
	reverse(rs.begin(), rs.end());
	return s == rs;
}

bool is_palindrome_string(const string& s) {
	string rs = s;
	reverse(rs.begin(), rs.end());
	return s == rs;
}

bool Akaibun(ll num, ll a) {
	if (!is_palindrome(num)) return false;
	string _num = base_n(num, a);
	if (_num == "-1") return false;
	if (!is_palindrome_string(_num)) return false;
	return true;
}

int main() {
	cin >> A >> N;
	ll ans = 0;

	for (ll i = 1; i < 10; ++i) {
		if (i > N) {
			cout << ans << endl;
			return 0;
		}
		if (Akaibun(i, A)) {
			ans += i;
		}
	}

	for (ll i = 1; i < 10; ++i) {
		ll x = i * 10 + i;
		if (x > N) {
			cout << ans << endl;
			return 0;
		}
		if (Akaibun(x, A)) {
			ans += x;
		}
	}

	for (ll i = 10; i < 10000000; ++i) {
		string sti = to_string(i);
		string back = sti.substr(0, sti.size() - 1);
		reverse(back.begin(), back.end());
		ll numi = stoll(sti + back);
		if (numi > N) {
			cout << ans << endl;
			return 0;
		}
		if (Akaibun(numi, A)) {
			ans += numi;
		}

		back = sti;
		reverse(back.begin(), back.end());
		numi = stoll(sti + back);
		if (numi <= N) {
			if (Akaibun(numi, A)) {
				ans += numi;
			}
		}
	}
	cout << ans << endl;
	return 0;
}
