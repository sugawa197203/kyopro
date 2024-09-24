use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: i32,
        A: [i32; N],
        B: [i32; N],
        C: [i32; N]
    }

    println!(
        "{}",
        A.iter().sum::<i32>() * B.iter().sum::<i32>() * C.iter().sum::<i32>()
    );
}
