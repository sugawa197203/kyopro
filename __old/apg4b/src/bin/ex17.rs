use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: usize,
        S: i32,
        A: [i32; N],
        P: [i32; N],
    }

    let mut count = 0;

    for a in A.iter() {
        for p in P.iter() {
            if a + p == S {
                count += 1;
            }
        }
    }

    println!("{}", count);
}
