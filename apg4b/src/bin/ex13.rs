use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: i32,
        A:[i32; N]
    }

    let avg = A.iter().sum::<i32>() / N;

    for a in A {
        println!("{}", (a - avg).abs());
    }
}
