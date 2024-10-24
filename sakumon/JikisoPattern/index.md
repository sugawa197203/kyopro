# Jikiso Pattern

## 問題文

MCC 王国には $N$ 人の国民がいて、それぞれ $1$ から $N$ までの国民番号が割り振られています。MCC王国では、国民が王様に直訴することができます。しかし、王様は全員の意見を聞き入れることはできないので、以下のルールを設けました。

* $1$ 日のうちで、直訴してきた人の国民番号の和が $M$ で割り切れるとき、意見を聞き入れる

MCC 王国で 1 日に直訴して意見を聞き入れてもらえる国民の組み合わせはいくつあるか求めてください。

## 制約

- $1 \leq M \leq N \leq 10^6$
- $M$ は奇数で $N$ の約数

## 入力

入力は以下の形式で標準入力から与えられます。

<div class="code-math">

$N M$

</div>

## 出力

1 日に直訴して意見を聞き入れてもらえる国民の組み合わせの数

### 入力例 1

```
3 3
```

### 出力例 1

```
4
```

国民は $1, 2, 3$ で、考えられる 1 日に直訴しに来る組み合わせは $\{\}, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\}$ で、それぞれの和は $0, 1, 2, 3, 3, 4, 5, 6$ です。なので、直訴が聞き入れてもらえる組み合せは $\{\}, \{3\}, \{1, 2\}, \{1, 2, 3\}$ となるので正解は $4$ です。

### 入力例 1

```
6 3
```

### 出力例 1

```
24
```

## 解法

問題文を簡単にするとこんな感じ↓

$1 から N$ までの整数集合で和が $M$ で割り切れる部分集合の個数を求めよ。

計算したらこんな式が出てくる(証明は時間があるときに書きます)

$ans = \dfrac{2^N+(M-1)2^\frac{N}{M}}{M}$

<details>
<summary>証明</summary>

$f(x) = (1+x)(1+x^2)(1+x^3) \cdots (1+x^{N-2})(1+x^{N-1})(1+x^N)$

を展開すると、

$f(x) = 1 + \binom{1}{1}x + \binom{2}{1}x^2 + \binom{3}{1}x^3 + \cdots + \binom{N-2}{1}x^{N-2} + \binom{N-1}{1}x^{N-1} + \binom{N}{1}x^N + \binom{N}{2}x^{N+1} + \binom{N+1}{2}x^{N+2} + \cdots + \binom{2N-2}{N-1}x^{2N-2} + \binom{2N-1}{N-1}x^{2N-1} + \binom{2N}{N}x^{2N}$

となる。各項の係数に注目すると、 $x^n$ の係数は問題において、足して $n$ になる部分集合の個数になっている。

実際 N=3 (入力例1)では、

$f(x) = (1+x)(1+x^2)(1+x^3)$

を展開すると、

$f(x) = x^0 + x^1 + x^2 + 2x^3 + x^4 + x^5 + x^6$

となる。

$f(x) = c_0 x^0 + x_1 x^1 + c_2 x^2 + \cdots + c_{2N-1} x^{2N-1} + c_{2N} x^{2N} = \sum_{n=0}^{2N} c_n x^n$

と置くと、 $n$ が $M$ で割り切れる項の係数の和が求める答えになる。

ここで、 $x=1$ のとき、

$f(1) = 2^N$

である。

ここで、 $1$ の $M$ 乗根を $\omega$ とし、 $M$ は $N$ の約数であることに注意すると、

$f(\omega^0) = c_0 \omega^0 + c_1 \omega^0 + c_2 \omega^0 + \cdots + c_{M-1} \omega^0 + c_{M} \omega^0 + c_{M+1} \omega^0 + \cdots + c_{2M} \omega^0 + \cdots + c_{2N-1} \omega^0 + c_{2N} \omega^0$

$f(\omega^1) = c_0 \omega^0 + c_1 \omega^1 + c_2 \omega^2 + \cdots + c_{M-1} \omega^{M-1} + c_{M} \omega^0 + c_{M+1} \omega^1 + \cdots + c_{2M} \omega^0 +  \cdots + c_{2N-1} \omega^{M-1} + c_{2N} \omega^0$

$f(\omega^2) = c_0 \omega^0 + c_1 \omega^2 + c_2 \omega^4 + \cdots + c_{M-1} \omega^{2(M-1)} + c_{M} \omega^0 + c_{M+1} \omega^2 + \cdots + c_{2M} \omega^0 + \cdots + c_{2N-1} \omega^{2(M-1)} + c_{2N} \omega^0$

$\vdots$

$f(\omega^{M-1}) = c_0 \omega^0 + c_1 \omega^{M-1} + c_2 \omega^{2(M-1)} + \cdots + c_{M-1} \omega^{(M-1)(M-1)} + c_{M} \omega^0 + c_{M+1} \omega^{M-1} + \cdots + c_{2N-1} \omega^{(M-1)(M-1)} + c_{2N} \omega^0$

となる。

整数 $t (1 \leq t < M)$ について $M$ は奇数なので

$ \sum_{k=0}^{M-1} \omega^{kt} = 0$

となる。これは、 $\sum_{i=0}^{M-1} f(\omega^i)$ で、$c\omega^i (i \mod M \neq 0)$ のであることを意味する。なので、

$\sum_{i=0}^{M-1} f(\omega^i) = Mc_0\omega^0 + 0 + 0 + \cdots + 0 + Mc_M\omega^0 + 0 + \cdots + 0 + Mc_{2N}\omega^0\\
= M(c_0\omega^0 + c_M\omega^0 + c_{2M}\omega^0 + \cdots + c_{2N}\omega^0)\\
= M(c_0 + c_M + c_{2M} + \cdots + c_{2N})$

と表すことができる。よって $\frac{1}{M} \sum_{i=0}^{M-1} f(\omega^i)$ を計算することで答えが求まる。

ここで、$\omega$ は方程式 $z^M=1$ の解なので $z^M-1$ は

$z^M-1 = (z-\omega^0)(z-\omega^1)(z-\omega^2) \cdots (z-\omega^{M-1})$

と因数分解できる。この式に $z=-1$ を代入し、 $M$ が奇数であることに注意すると、


$(-1)^M-1 = (-1-\omega^0)(-1-\omega^1)(-1-\omega^2) \cdots (-1-\omega^{M-1})$

$2 = (1+\omega^0)(1+\omega^1)(1+\omega^2) \cdots (1+\omega^{M-1})$

となる。このことから $f(\omega^1)$ は

$f(\omega^1) = (1 + \omega^0)(1 + \omega^1)(1 + \omega^2) \cdots (1 + \omega^N)\\
= ((1+\omega^0)(1+\omega^1)(1+\omega^2) \cdots (1+\omega^{M-1}))^{\frac{N}{M}}\\
= 2^{\frac{N}{M}}$

となる。同様に、 $f(\omega^2), f(\omega^3), \cdots, f(\omega^{M-1})$ も $2^{\frac{N}{M}}$ となる。 $f(\omega^0)$ は $f(1)$ と同じなので $2^N$ である。よって、

$\sum_{i=0}^{M-1} f(\omega^i) = 2^N + (M-1)2^{\frac{N}{M}}$

となる。よって答えは

$ans = \dfrac{2^N+(M-1)2^\frac{N}{M}}{M}$

</details>

## 元ネタなど

$M$ は偶数でも可、$N$ の約数でなくても可のときの解法がわからん

あと $mod$ $98244353$ 取ったほうがいいか迷ってる

mod 取るんだったら $1 \leq M \leq N \leq 10^{18}$

O(1) で解ける(数字がでかいから実質O(n log n)) から、数字デカくしないでQ回答えてくださいがいいかも？

DP でも解けるっぽい？

Bit 全探索、DP、式化で部分点できそう
