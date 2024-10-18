#include <stdio.h>
#include <string.h>

char S[100000000];
char T[100000000];

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    scanf("%s", S);
    scanf("%s", T);
    
    // 大文字に変換
    for (int i = 0; i < m; i++) {
        if (S[i] >= 'a'){
            S[i] = S[i] - 'a' + 'A';
        }
        if (T[i] >= 'a'){
            T[i] = T[i] - 'a' + 'A';
        }
    }

    // 文字数カウント
    int C[26];
    memset(C, 0, sizeof(C));
    for (int i = 0; i < n; i++) {
        C[S[i] - 'A']++;
    }

    // 文字数チェック
    for (int i = 0; i < m; i++) {
        C[T[i] - 'A']--;
        if (C[T[i] - 'A'] < 0) {
            printf("No\n");
            return 0;
        }
    }

    printf("Yes\n");

    return 0;
}