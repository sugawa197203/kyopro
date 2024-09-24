use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        pattern: i32,
    }

    if pattern == 1 {
        input! {
            price: i32,
            N: i32,
        }

        println!("{}", price * N);
    } else {
        input! {
            text: String,
            price: i32,
            N: i32,
        }

        println!("{}!", text);
        println!("{}", price * N);
    }
}
