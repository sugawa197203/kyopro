#include <iostream>
using namespace std;

char buf[200001] = {0};
int buf_index = 0;

void add(char c){
	buf[buf_index] = c;
	buf_index++;
}

void dell_kakko(){
	while(buf[--buf_index] != '('){
		buf[buf_index] = 0;
	}
	buf[buf_index] = 0;
}

int main(){
	int N;
	cin >> N;
	char S[200001] = {0};
	cin >> S;
	int kakko = 0;

	for(int i = 0; i < N; i++){
		if (S[i] == '('){
			kakko++;
			add(S[i]);
		}
		else if (kakko > 0 && S[i] == ')'){
			kakko--;
			dell_kakko();
		}
		else{
			add(S[i]);
		}
	}
	
	cout << buf << endl;
}