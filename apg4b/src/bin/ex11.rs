use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        n: i32,
        mut a: i32
    }

    for i in 0..n {
        input! {
            op: String,
            b: i32
        }

        if op == "+" {
            a += b;
        } else if op == "-" {
            a -= b;
        } else if op == "*" {
            a *= b;
        } else if op == "/" {
            if b == 0 {
                println!("error");
                break;
            } else {
                a /= b;
            }
        }

        println!("{}:{}", i + 1, a);
    }
}
