#include<stdio.h>
#include<string>
#include<vector>
#include<iostream>
using namespace std;
int main(){
	int N, M, H, K;
	cin >> N >> M >> H >> K;

	string S;
	cin >> S;
	vector<tuple<int, int>> ITEM;

	int x, y;
	for (int i = 0; i < M; i++){
		cin >> x, y;
		ITEM.push_back((x, y));
	}
}
 
for i in range(M):
	x, y = [int(p) for p in input().split(" ")]
 
	ITEM.append((x, y))
 
def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default
 
X = 0
Y = 0
#print("----")
for s in S:
 
	#print("-")
	#print("X Y", X, Y)
	#print("H", H)
 
	if H == 0:
		print("No")
		exit(0)
	H -= 1
 
	if s == "R":
		X += 1
	elif s == "L":
		X -= 1
	elif s == "U":
		Y += 1
	elif s == "D":
		Y -= 1
 
	r = my_index(ITEM, (X, Y))
	
	if r:
		#print("ITEM")
		if H < K:
			ITEM.pop(r)
			#print("UP", H)
			H = K
	
print("Yes")