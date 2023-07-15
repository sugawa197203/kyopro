use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        a: usize,
        b: usize,
    }

    let kakko = "]";

    println!("A:{}", kakko.repeat(a));
    println!("B:{}", kakko.repeat(b));
}
