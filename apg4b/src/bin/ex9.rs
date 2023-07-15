use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        x: i32,
        a: i32,
        b: i32,
    }

    let mut result = x + 1;
    println!("{}", result);
    result *= a + b;
    println!("{}", result);
    result *= result;
    println!("{}", result);
    result -= 1;
    println!("{}", result);
}
